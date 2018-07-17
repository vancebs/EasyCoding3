#!/usr/bin/python
# coding=utf-8


import time
import os
from urllib.request import Request
from urllib.request import urlopen
from script.util.Print import Print

_PREFIX_CMD = 'cmd:'
_PREFIX_FUNC = 'func:'
UPDATE_DURATION = 3600

# User Agent
UA_CHROME = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0)' \
            ' AppleWebKit/535.11 (KHTML, like Gecko)' \
            ' Chrome/17.0.963.56 Safari/535.11'

# VERSION URL
URL_VERSION = 'https://raw.githubusercontent.com/vancebs/EasyCoding3/master/VERSION'

# VERSION_FILE
LOCAL_VERSION = '%s/VERSION' % os.path.dirname(__file__)


def shell_exec(cmd: str) -> int:
    # send command
    print('%s%s' % (_PREFIX_CMD, cmd))

    # receive exit code
    line = input()

    # get exit code
    try:
        return int(line)
    except ValueError:
        return 10086  # unknown error


def shell_func(cmd: str) -> str:
    # send command
    print('%s%s' % (_PREFIX_FUNC, cmd))

    # receive output
    output = []
    line = input().strip()
    while not line == '==end==':
        output.append(line)
        line = input().strip()

    # get result
    return '\n'.join(output).strip()


def launch():
    # get last update time
    str_last_update_time = shell_func('eval echo ${EC3_LAST_UPDATE_TIME}').strip()
    last_update_time = 0
    if str_last_update_time != '':
        last_update_time = int(str_last_update_time)

    # get current time
    curr_update_time = int(time.time())

    # check update duration
    delta_time = curr_update_time - last_update_time
    if delta_time <= UPDATE_DURATION:
        # unnecessary to update
        Print.green('Unnecessary to update. Next update window after %ss' % (UPDATE_DURATION - delta_time))
        exit_shell()
        return

    # save last update time to shell
    shell_exec('export EC3_LAST_UPDATE_TIME=%s' % curr_update_time)

    # start version check
    Print.green('Check version ...')

    # get local version
    local_version: str = '-1'
    if os.path.exists(LOCAL_VERSION):
        local_version = open(LOCAL_VERSION, "r").readline().strip()

    # get remote version
    remote_version = http_get(URL_VERSION).strip()

    # check need update
    need_update = remote_version != local_version

    # do update if necessary
    if not need_update:
        Print.green('Done. Up to date!!')
    else:
        Print.green('Done. Need update! local: [%s], remote: [%s]' % (local_version, remote_version))
        Print.green('Updating ...')
        shell_exec('git pull')
        Print.green('Done.')

    # exit shell
    exit_shell()


def http_get(url: str) -> str:
    request = Request(url=url, headers={'User-Agent': UA_CHROME})
    response = urlopen(request, timeout=3)
    return response.read().decode()


def exit_shell():
    print('==end==')


if __name__ == "__main__":
    launch()
