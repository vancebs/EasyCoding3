#! /bin/bash

COLOR_RED=31
COLOR_GREEN=32
COLOR_YELLOW=33
COLOR_BLUE=34
COLOR_WHITE=37

CONDA_ENV_NAME_2="EasyCoding3_2"
CONDA_ENV_NAME_3="EasyCoding3_3"

PIPE_IN_PATH=/tmp/$$.in.fifo
PIPE_OUT_PATH=/tmp/$$.out.fifo
PIPE_TMP_PATH=/tmp/$$.tmp.fifo

MIN_PYTHON_VERSION=3.6

# load config
source ./GlobalBashConfig.sh

function print() {
    # $1 color index
    # $2 text
    echo -e "\033[${1}m${2}\033[0m"
}

function initPipeIn_6() {
    mkfifo ${PIPE_IN_PATH}
    exec 6<>${PIPE_IN_PATH}
    rm ${PIPE_IN_PATH}
}

function releasePipeIn_6() {
    exec 6>&-
}

function initPipeOut_7() {
    mkfifo ${PIPE_OUT_PATH}
    exec 7<>${PIPE_OUT_PATH}
    rm ${PIPE_OUT_PATH}
}

function releasePipeOut_7() {
    exec 7>&-
}

function initPipeTmp_8() {
    mkfifo ${PIPE_TMP_PATH}
    exec 8<>${PIPE_TMP_PATH}
    rm ${PIPE_TMP_PATH}
}

function releasePipeTmp_8() {
    exec 8>&-
}

function condaBegin() {
    CONDA_PATH=$(which conda)
    if [ $? != 0 ]; then
        print ${COLOR_YELLOW}  "Conda not installed, use default python path: ${PYTHON_BIN}"
        unset CONDA_PATH
        return
    fi

    # init path
    CONDA_DIR=$(dirname ${CONDA_PATH})
    CONDA_ACTIVATE=${CONDA_DIR}/activate
    CONDA_DEACTIVATE=${CONDA_DIR}/deactivate

    if [ ! ${CONDA_ENV_READY} ]; then
        # check whether has ec env
        has_env_2=FALSE
        has_env_3=FALSE

        # init pipe tmp
        initPipeTmp_8

        # check result
        ${CONDA_PATH} env list >&8
        echo "==end==" >&8
        while read line; do
            if [[ ${line} == "==end==" ]]; then
                break
            elif [[ ${line} == ${CONDA_ENV_NAME_2}* ]]; then
                has_env_2=TRUE
            elif [[ ${line} == ${CONDA_ENV_NAME_3}* ]]; then
                has_env_3=TRUE
            fi
        done <&8

        # close pipe tmp
        releasePipeTmp_8

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

    # set python bin
    PYTHON_BIN="python"
}

function condaEnd() {
    if [ ! ${CONDA_PATH} ]; then
        # conda not installed
        unset CONDA_PATH
        return
    fi

    # unset var
    unset CONDA_PATH
    unset CONDA_DIR
    unset CONDA_ACTIVATE
    unset CONDA_DEACTIVATE
}

function enterPython2() {
    if [ ! ${CONDA_PATH} ]; then
        # conda not installed
        return
    fi

    # switch conda env to python 2
    source ${CONDA_ACTIVATE} ${CONDA_ENV_NAME_2}
}

function leavePython2() {
    if [ ! ${CONDA_PATH} ]; then
        # conda not installed
        return
    fi

    # restore conda env
    source ${CONDA_DEACTIVATE}
}

function enterPython3() {
    if [ ! ${CONDA_PATH} ]; then
        # conda not installed
        return
    fi

    # switch conda env to python 3
    source ${CONDA_ACTIVATE} ${CONDA_ENV_NAME_3}
}

function leavePython3() {
    if [ ! ${CONDA_PATH} ]; then
        # conda not installed
        return
    fi

    # restore conda env
    source ${CONDA_DEACTIVATE}
}

function pythonVersionCheck() {
    if [ ${CONDA_PATH} ]; then
        # conda installed, we can switch version freely.
        print ${COLOR_GREEN} "Conda installed. Python version can be switched."
        return 0
    fi

    # conda not installed. so check python version. if lower than required, script cannot run.
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
        print ${COLOR_GREEN} "Valid python version: ${code}"
        return 0
    fi
}
