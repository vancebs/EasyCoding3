#!/usr/bin/env bash

# get script path
SCRIPT_PATH=$(readlink -f "${BASH_SOURCE[0]}")
SCRIPT_DIR=$(dirname ${SCRIPT_PATH})
PYTHON_SCRIPT=${SCRIPT_DIR}/ec3.py

source ./env.sh

function execScript() {
    # begin conda
    condaBegin
    if [ $? != 0 ]; then
        print ${COLOR_RED}  "Conda not installed, please install first."
        return $?
    fi

    # enter python 2 for AOSP make
    enterPython2

    load_script "${PYTHON_SCRIPT}" $@

    # leave python 2
    leavePython2

    # end conda
    condaEnd

    return 0
}


########################
# entry
execScript $@

