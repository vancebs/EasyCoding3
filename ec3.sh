#!/usr/bin/env bash

# get script path
SCRIPT_PATH=$(readlink -f "${BASH_SOURCE[0]}")
SCRIPT_DIR=$(dirname ${SCRIPT_PATH})
#PYTHON_BIN=python
PYTHON_SCRIPT=${SCRIPT_DIR}/ec3.py
PIPE_IN_PATH=/tmp/$$.in.fifo
PIPE_OUT_PATH=/tmp/$$.out.fifo
CTRL_C_DETECTED=FALSE

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

function execScript {
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
