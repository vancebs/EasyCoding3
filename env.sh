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
PYTHON_BIN="python"

CTRL_C_DETECTED=FALSE

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
        unset CONDA_PATH
        return 1
    fi

    # init path
    CONDA_DIR=$(dirname ${CONDA_PATH})
    CONDA_ACTIVATE=${CONDA_DIR}/activate
    CONDA_DEACTIVATE=${CONDA_DIR}/deactivate

    # check conda env by a fast way
    if [ ! ${CONDA_ENV_READY} ]; then
        local ENV_PATH_2="${CONDA_DIR}/envs/${CONDA_ENV_NAME_2}"
        local ENV_PATH_3="${CONDA_DIR}/envs/${CONDA_ENV_NAME_3}"
        if [ -e ${ENV_PATH_2} -a -e ${ENV_PATH_3} ]; then
            CONDA_ENV_READY=True
        fi
    fi

    # setup conda env
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

    return 0
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

function load_script() {
    #############################
    # $1: PYTHON_SCRIPT
    # $2-n: parameters
    #############################
    PYTHON_SCRIPT=$1
    shift

    # init pipe
    initPipeIn_6
    initPipeOut_7

    # start script
    enterPython3
    OUT=$(${PYTHON_BIN} ${PYTHON_SCRIPT} $@ >&6 <&7 &)
    leavePython3

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
    releasePipeIn_6
    releasePipeOut_7
}

function onCtrlC () {
    CTRL_C_DETECTED=TRUE
}

trap "onCtrlC" INT