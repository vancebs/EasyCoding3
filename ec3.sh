#!/usr/bin/env bash

# get script path
SCRIPT_PATH=$(readlink -f "${BASH_SOURCE[0]}")
SCRIPT_DIR=$(dirname ${SCRIPT_PATH})
PYTHON_SCRIPT=${SCRIPT_DIR}/ec3.py
CTRL_C_DETECTED=FALSE

source env.sh

function execScript() {
    # begin conda
    condaBegin

    # check python version
    pythonVersionCheck
    if [ $? != 0 ]; then
        return 1
    fi

    # enter python 2 for AOSP make
    enterPython2

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

    # leave python 2
    leavePython2

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

