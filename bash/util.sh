#!/usr/bin/env bash

if [ -z ${_UTIL_SH_} ]; then
export _UTIL_SH_=1

############################
# pipe
PIPE_IN_PATH=/tmp/$$.in.6.fifo
PIPE_OUT_PATH=/tmp/$$.out.7.fifo
PIPE_TMP_8_PATH=/tmp/$$.tmp.8.fifo
PIPE_TMP_9_PATH=/tmp/$$.tmp.9.fifo

function initPipeIn_6() {
    mkfifo ${PIPE_IN_PATH}
    exec 6<>${PIPE_IN_PATH}
    rm ${PIPE_IN_PATH}
}

function releasePipeIn_6() {
    exec 6>&-
}

function initPipeOut_7() {
    mkfifo ${PIPE_OUT_PATH}
    exec 7<>${PIPE_OUT_PATH}
    rm ${PIPE_OUT_PATH}
}

function releasePipeOut_7() {
    exec 7>&-
}

function initPipeTmp_8() {
    mkfifo ${PIPE_TMP_8_PATH}
    exec 8<>${PIPE_TMP_8_PATH}
    rm ${PIPE_TMP_8_PATH}
}

function releasePipeTmp_8() {
    exec 8>&-
}

function initPipeTmp_9() {
    mkfifo ${PIPE_TMP_9_PATH}
    exec 9<>${PIPE_TMP_9_PATH}
    rm ${PIPE_TMP_9_PATH}
}

function releasePipeTmp_9() {
    exec 9>&-
}

##############################
# print
COLOR_RED=31
COLOR_GREEN=32
COLOR_YELLOW=33
COLOR_BLUE=34
COLOR_WHITE=37

function print() {
    # $1 color index
    # $2 text
    echo -e "\033[${1}m${2}\033[0m"
}

fi #_UTIL_SH_