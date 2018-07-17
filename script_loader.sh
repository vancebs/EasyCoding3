#! /bin/bash

CTRL_C_DETECTED=FALSE

# load env script
# source ./env.sh # loaded outside

function load_script() {
    #############################
    # $1: PYTHON_BIN
    # $2: PYTHON_SCRIPT
    # $3-n: parameters
    #############################
    PYTHON_BIN=$1
    PYTHON_SCRIPT=$2
    shift
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