#!/usr/bin/env bash

export EC_PATH=$(readlink -f ${BASH_SOURCE[0]})
export EC_DIR=$(dirname ${EC_PATH})
export BASH_DIR=${EC_DIR}/bash
export PYTHON_DIR=${EC_DIR}/script

# load bp system
source ${EC_DIR}/bp.sh $@

# release
unset EC_PATH
unset EC_DIR
unset BASH_DIR
unset PYTHON_DIR