#!/usr/bin/env bash

PYTHON_SCRIPT=${EC_DIR}/bp.py
CTRL_C_DETECTED=FALSE

source ${BASH_DIR}/util.sh
source ${BASH_DIR}/env.sh
#source bash/util.sh
#source bash/env.sh

function execScript() {
    # begin conda
    condaBegin
    if [ $? != 0 ]; then
        print ${COLOR_RED}  "Conda not installed, please install first."
        return $?
    fi

    # enter python 2 for AOSP make
    enterPython2

    #################################
    # begin script

    # init pipe
    initPipeIn_6
    initPipeOut_7

    # start script
    ({
        enterPython3
        ${PYTHON_BIN} ${PYTHON_SCRIPT} $@ >&6 <&7
        leavePython3
    } &)

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
            eval ${line#cmd:}

            # feedback exit code
            echo "$?" >&7
        elif [[ ${line} == "func:"* ]]; then
            # run command & get output
            result=$(eval ${line#func:})

            # feedback output
            echo "$?" >&7
            echo ${result} >&7
            echo "==end==" >&7
        else
            # echo message
            echo -e "${line}"
        fi
    done

    # release pipe
    releasePipeIn_6
    releasePipeOut_7

    # end script
    ###############################

    # leave python 2
    leavePython2

    # end conda
    condaEnd

    return 0
}

########################
# entry
function onCtrlC () {
    CTRL_C_DETECTED=TRUE
}

trap "onCtrlC" INT

execScript $@

