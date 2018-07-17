#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print

import sys
import os
from urllib.request import Request
from urllib.request import urlopen

# User Agent
UA_CHROME = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0)' \
            ' AppleWebKit/535.11 (KHTML, like Gecko)' \
            ' Chrome/17.0.963.56 Safari/535.11'

# VERSION URL
URL_VERSION = 'https://raw.githubusercontent.com/vancebs/EasyCoding3/master/VERSION'

# VERSION_FILE
LOCAL_VERSION = '%s/VERSION' % os.path.dirname(__file__)


def launch():
    Print.green('Check version ...')

    # get local version
    local_version: str = '-1'
    if os.path.exists(LOCAL_VERSION):
        local_version = open(LOCAL_VERSION, "r").readline().strip()

    # get remote version
    remote_version = http_get(URL_VERSION).strip()

    # check need update
    need_update = remote_version == local_version

    # do update if necessary
    if not need_update:
        Print.green('Done. Up to date!!')
    else:
        Print.green('Done. Need update! local: [%s], remote: [%s]' % (local_version, remote_version))
        Print.green('Updating ...')
        print('cmd:git pull')
        Print.green('Done.')

    # exit shell
    exit_shell()


def http_get(url: str) -> str:
    request = Request(url=url, headers={'User-Agent': UA_CHROME})
    response = urlopen(request)
    return response.read()


def exit_shell():
    print('==end==')


if __name__ == "__main__":
    launch()
