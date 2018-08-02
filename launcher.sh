#! /bin/bash

export EC_PATH=$(readlink -f ${BASH_SOURCE[0]})
export EC_DIR=$(dirname ${EC_PATH})
export BASH_DIR=${EC_DIR}/bash
export PYTHON_DIR=${EC_DIR}/script

PYTHON_SCRIPT=${EC_DIR}/Launcher.py
CHECK_UPDATE_SCRIPT=${EC_DIR}/script/CheckUpdate.py
EC_PATH=${EC_DIR}/ec3.sh
CHECK_PATH=${EC_DIR}/.check
UPDATE_PATH=${EC_DIR}/.update

# load env script
source ${BASH_DIR}/env.sh

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
        cd ${EC_DIR}  # switch to EC root dir
        git pull
        cd ${_PWD}  # restore pwd

        # remote update check info
        rm -f ${CHECK_PATH}
        rm -f ${UPDATE_PATH}

        # unset VAR to make bash script reloaded
        unset _ENV_SH_
        unset _UTIL_SH_
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