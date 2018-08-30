#! /bin/bash

if [ -z ${_ENV_SH_} ]; then
export _ENV_SH_=1

source ${BASH_DIR}/util.sh

CONDA_ENV_NAME_2="EasyCoding3_2"
CONDA_ENV_NAME_3="EasyCoding3_3"

MIN_PYTHON_VERSION=3.6
export PYTHON_BIN="python"

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
    CONDA_ENV_DIR=${CONDA_DIR}/../envs

    # check conda env by a fast way
    if [ -z ${CONDA_ENV_READY} ]; then
        local ENV_PATH_2="${CONDA_ENV_DIR}/${CONDA_ENV_NAME_2}"
        local ENV_PATH_3="${CONDA_ENV_DIR}/${CONDA_ENV_NAME_3}"

        if [ -e ${ENV_PATH_2} -a -e ${ENV_PATH_3} ]; then
            CONDA_ENV_READY=TRUE
        fi
    fi

    # setup conda env
    if [ -z ${CONDA_ENV_READY} ]; then
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
            echo "y" | ${CONDA_PATH} create -n ${CONDA_ENV_NAME_2} python=2.7.15 pil
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

fi  # _ENV_SH_
