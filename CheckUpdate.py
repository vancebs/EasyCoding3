#!/usr/bin/python
# coding=utf-8


import time
import os

from urllib.error import URLError
from urllib.request import Request
from urllib.request import urlopen
from script.util.Print import Print


UPDATE_DURATION = 3600

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))

# User Agent
UA_CHROME = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0)' \
            ' AppleWebKit/535.11 (KHTML, like Gecko)' \
            ' Chrome/17.0.963.56 Safari/535.11'

# VERSION URL
URL_VERSION = 'https://raw.githubusercontent.com/vancebs/EasyCoding3/master/VERSION'

# VERSION_FILE
LOCAL_VERSION = '%s/VERSION' % SCRIPT_DIR

# Config file
LAST_CHECK_FILE = '%s/.check' % SCRIPT_DIR
HAS_UPDATE_FILE = '%s/.update' % SCRIPT_DIR


def launch():
    # check has update file
    if os.path.exists(HAS_UPDATE_FILE):
        #  Print.green('Update already detected')
        return  # already found update

    # get current time & last check time
    curr_time = int(time.time())
    last_time = get_last_check()[0]

    # check whether should do update check
    delta_time = curr_time - last_time
    if delta_time <= UPDATE_DURATION:
        # set_last_check(last_time,
        #                'Unnecessary to update. Next update window after %ss' % (UPDATE_DURATION - delta_time))
        return  # unnecessary to update

    # update last check time
    set_last_check(curr_time, 'Checking version...')

    # get local version
    local_version: str = get_last_version()

    # get remote version
    remote_version = http_get(URL_VERSION).strip()
    if remote_version is None:
        set_last_check(last_time, 'Get remote version failed! Check again next time.')  # failed. save last check time
        return

    # check need update
    need_update = remote_version != local_version

    # do update if necessary
    if not need_update:
        set_last_check(curr_time, 'Up to date!!')
    else:
        set_last_check(curr_time, 'Need update! local: [%s], remote: [%s]' % (local_version, remote_version))
        set_has_update(remote_version)


def get_last_version() -> str:
    if os.path.exists(LOCAL_VERSION):
        with open(LOCAL_VERSION, 'r') as file:
            return file.readline().strip()
    else:
        return '0'


def get_last_check() -> (int, str):
    if os.path.exists(LAST_CHECK_FILE):
        with open(LAST_CHECK_FILE, 'r') as file:
            return int(file.readline().strip()), file.readline().strip()
    else:
        return 0, '<File not found>'


def set_last_check(timestamp: int, msg: str):
    with open(LAST_CHECK_FILE, 'w') as file:
        file.write('%s\n%s\n' % (timestamp, msg))


def set_has_update(version: str):
    with open(HAS_UPDATE_FILE, 'w') as file:
        file.write('%s\n' % version)


def http_get(url: str) -> str:
    try:
        request = Request(url=url, headers={'User-Agent': UA_CHROME})
        response = urlopen(request, timeout=5)
        return response.read().decode()
    except URLError:
        return str(None)


if __name__ == "__main__":
    import time
    time.sleep(1)
    launch()
