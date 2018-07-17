#! /bin/bash

SCRIPT_PATH=$(readlink -f "${BASH_SOURCE[0]}")
SCRIPT_DIR=$(dirname ${SCRIPT_PATH})

PYTHON_SCRIPT=${SCRIPT_DIR}/Launcher.py
EC_PATH=${SCRIPT_DIR}/ec3.sh

# load env script
source ./env.sh
source ./script_loader.sh

function launch() {
    # begin conda
    condaBegin

    # check python version
    pythonVersionCheck
    if [ $? != 0 ]; then
        return 1
    fi

    # check version an update
    load_script "${PYTHON_BIN}" "${PYTHON_SCRIPT}"

    # run ec
    source ${EC_PATH} $@

    # end conda
    condaEnd

    return 0
}

################################
# do launch
launch $@