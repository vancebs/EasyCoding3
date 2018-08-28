#!/usr/bin/python
# coding=utf-8

import time

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer
from urllib.error import URLError
from urllib.request import Request
from urllib.request import urlopen
from script.CheckUpdate import set_last_check
from script.CheckUpdate import set_has_update


class version(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'get ec version',
    )

    # User Agent
    _UA_CHROME = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0)' \
                 ' AppleWebKit/535.11 (KHTML, like Gecko)' \
                 ' Chrome/17.0.963.56 Safari/535.11'

    # VERSION URL
    _URL_VERSION = 'https://raw.githubusercontent.com/vancebs/EasyCoding3/master/VERSION'

    def on_run(self, *params) -> bool:
        with open('%s/VERSION' % self.cfg.cfgProgramDir, 'r') as file:
            local_version = file.readline().strip()
        remote_version = version.http_get(version._URL_VERSION).strip()

        # check need update
        need_update = remote_version > local_version

        # do update if necessary
        if not need_update:
            msg = 'Up to date!! local: [%s], remote: [%s]' % (local_version, remote_version)
            set_last_check(int(time.time()), msg)

            # show message
            Printer.green_line(msg)
        else:
            msg = 'Need update! local: [%s], remote: [%s]' % (local_version, remote_version)
            set_last_check(int(time.time()), msg)
            set_has_update(remote_version)

            # show message
            Printer.yellow_line(msg)

            # run version cmd again to apply update
            self.cmd('version')

        return True

    @staticmethod
    def http_get(url: str) -> (None, str):
        try:
            request = Request(url=url, headers={'User-Agent': version._UA_CHROME})
            response = urlopen(request, timeout=5)
            return response.read().decode()
        except URLError:
            return None
