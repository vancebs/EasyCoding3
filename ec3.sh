#!/usr/bin/env bash

# get script path
SCRIPT_PATH=$(readlink -f "${BASH_SOURCE[0]}")
SCRIPT_DIR=$(dirname ${SCRIPT_PATH})
#PYTHON_BIN=python
PYTHON_SCRIPT=${SCRIPT_DIR}/ec3.py
PIPE_IN_PATH=/tmp/$$.in.fifo
PIPE_OUT_PATH=/tmp/$$.out.fifo
CTRL_C_DETECTED=FALSE

MIN_PYTHON_VERSION=3.6
CONDA_ENV_NAME_2="EasyCoding3_2"
CONDA_ENV_NAME_3="EasyCoding3_3"

COLOR_RED=31
COLOR_GREEN=32
COLOR_YELLOW=33
COLOR_BLUE=34
COLOR_WHITE=37

# load config
source ${SCRIPT_DIR}/GlobalBashConfig.sh

function print() {
    # $1 color index
    # $2 text
    echo -e "\033[${1}m${2}\033[0m"
}

function condaBegin() {
    CONDA_PATH=$(which conda)
    if [ $? != 0 ]; then
        print ${COLOR_YELLOW}  "Conda not installed, use default python path: ${PYTHON_BIN}"
        CONDA_PATH=""
        return
    fi

    # init path
    CONDA_DIR=$(dirname ${CONDA_PATH})
    CONDA_ACTIVATE=${CONDA_DIR}/activate
    CONDA_DEACTIVATE=${CONDA_DIR}/deactivate

    if [[ ${CONDA_ENV_READY} != TRUE ]]; then
        # check whether has ec env
        local has_env_2=FALSE
        local has_env_3=FALSE
        ${CONDA_PATH} env list | while read line; do
            if [[ ${line} == ${CONDA_ENV_NAME_2}* ]]; then
                has_env_2=TRUE
            elif [[ ${line} == ${CONDA_ENV_NAME_3}* ]]; then
                has_env_3=TRUE
            fi
        done

        # create env if env not exists
        if [[ ${has_env_2} == FALSE ]]; then
            echo "y" | ${CONDA_PATH} create -n ${CONDA_ENV_NAME_2} python=2.7.15
        fi
        if [[ ${has_env_3} == FALSE ]]; then
            echo "y" | ${CONDA_PATH} create -n ${CONDA_ENV_NAME_3} python=3.7.0
        fi

        # set conda ready flag
        export CONDA_ENV_READY=TRUE
    fi


    # switch conda env
    source ${CONDA_ACTIVATE} ${CONDA_ENV_NAME_3}
    PYTHON_BIN="python"
}

function condaEnd() {
    if [ ${CONDA_PATH} == "" ]; then
        # conda not installed
        unset CONDA_PATH
        return
    fi

    # restore conda env
    source ${CONDA_DEACTIVATE}

    # unset var
    unset CONDA_PATH
    unset CONDA_DIR
    unset CONDA_ACTIVATE
    unset CONDA_DEACTIVATE
}

function pythonVersionCheck() {
    local version=$(${PYTHON_BIN} --version 2>&1)
    local code=0

    # Get version. The last section of version string
    i=0
    for v in ${version}; do
        if [ ${i} == 1 ]; then
            code=${v}
            break
        fi
        #echo ${code}
        i=$((i + 1))
    done

    # check version code
    if [[ ${code} < ${MIN_PYTHON_VERSION} ]]; then
        print ${COLOR_RED} "Python version [$code] is lower than min request [${MIN_PYTHON_VERSION}]"
        return 1
    else
        print ${COLOR_GREEN} "Valid python version"
        return 0
    fi
}

function execScript() {
    # begin conda
    condaBegin

    # check python version
    pythonVersionCheck
    if [ $? != 0 ]; then
        return 1
    fi

    # init pipe in
    mkfifo ${PIPE_IN_PATH}
    exec 6<>${PIPE_IN_PATH}
    rm ${PIPE_IN_PATH}

    # init pipe out
    mkfifo ${PIPE_OUT_PATH}
    exec 7<>${PIPE_OUT_PATH}
    rm ${PIPE_OUT_PATH}

    # start script
    OUT=$(${PYTHON_BIN} ${PYTHON_SCRIPT} $@ >&6 <&7 &)

    # read and exec
    while [[ TRUE ]]; do
        # read command from python script
        read -u6 line

        # check command end
        if [[ ${line} == "==end==" ]]; then
            break
        fi

        # check Ctrl+C
        if [[ ${CTRL_C_DETECTED} == TRUE ]]; then
            print ${COLOR_GREEN} "=====> cancel by [Ctrl+C]"
            break
        fi

        # run command
        if [[ ${line} == "cmd:"* ]]; then
            # run command
            ${line#cmd:}

            # feedback exit code
            echo "$?" >&7
        elif [[ ${line} == "func:"* ]]; then
            # run command & get output
            result=$(${line#func:})

            # feedback output
            echo ${result} >&7
            echo "==end==" >&7
        else
            # echo message
            echo "${line}"
        fi
    done

    # release pipe
    exec 6>&-
    exec 7>&-

    # end conda
    condaEnd
}

function onCtrlC () {
    CTRL_C_DETECTED=TRUE
}

########################
# entry
trap "onCtrlC" INT

execScript $@


# unset
unset SCRIPT_PATH
unset SCRIPT_DIR
unset PYTHON_BIN
unset PYTHON_SCRIPT
unset PIPE_IN_PATH
unset PIPE_OUT_PATH
unset CTRL_C_DETECTED

unset COLOR_RED
unset COLOR_GREEN
unset COLOR_YELLOW
unset COLOR_BLUE
unset COLOR_WHITE
unset CONDA_ENV_NAME_2
unset CONDA_ENV_NAME_3
