#! /bin/bash

SCRIPT_PATH=$(readlink -f "${BASH_SOURCE[0]}")
SCRIPT_DIR=$(dirname ${SCRIPT_PATH})

PYTHON_SCRIPT=${SCRIPT_DIR}/Launcher.py
EC_PATH=${SCRIPT_DIR}/ec3.sh

# load env script
source ${SCRIPT_DIR}/env.sh

function launch() {
    # begin conda
    condaBegin
    if [ $? != 0 ]; then
        print ${COLOR_RED}  "Conda not installed, please install first."
        return $?
    fi

    # check version an update
    load_script "${PYTHON_SCRIPT}"

    # run ec
    source ${EC_PATH} $@

    # end conda
    condaEnd

    return 0
}

################################
# do launch
launch $@