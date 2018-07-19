#! /bin/bash

SCRIPT_PATH=$(readlink -f "${BASH_SOURCE[0]}")
SCRIPT_DIR=$(dirname ${SCRIPT_PATH})

PYTHON_SCRIPT=${SCRIPT_DIR}/Launcher.py
CHECK_UPDATE_SCRIPT=${SCRIPT_DIR}/CheckUpdate.py
EC_PATH=${SCRIPT_DIR}/ec3.sh
CHECK_PATH=${SCRIPT_DIR}/.check
UPDATE_PATH=${SCRIPT_DIR}/.update

# load env script
source ${SCRIPT_DIR}/env.sh

function launch() {
    # begin conda
    condaBegin
    if [ $? != 0 ]; then
        print ${COLOR_RED}  "Conda not installed, please install first."
        return $?
    fi

    # show last update message
    if [ -e ${CHECK_PATH} ]; then
        (
            l=$(line)  # drop first line

            while l=$(line); do
                print ${COLOR_GREEN} "${l}"
            done
        ) < ${CHECK_PATH}
    fi

    # do update if necessary
    if [ -e ${UPDATE_PATH} ]; then
        _PWD=${PWD}
        cd ${SCRIPT_DIR}  # switch to EC root dir
        git pull
        cd ${_PWD}  # restore pwd

        # remote update check info
        rm -f ${CHECK_PATH}
        rm -f ${UPDATE_PATH}
    fi

    # run check update
    (
        (
            enterPython3
            ${PYTHON_BIN} ${CHECK_UPDATE_SCRIPT}
            leavePython3
        ) &
    )

    # run ec
    source ${EC_PATH} $@

    # end conda
    condaEnd

    return 0
}

################################
# do launch
launch $@