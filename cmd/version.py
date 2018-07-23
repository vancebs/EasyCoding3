#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print
from urllib.error import URLError
from urllib.request import Request
from urllib.request import urlopen


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
        Print.green('Local Version: %s' % local_version)

        remote_version = version.http_get(version._URL_VERSION).strip()
        Print.green('Remote Version: %s' % remote_version)

        return True

    @staticmethod
    def http_get(url: str) -> (None, str):
        try:
            request = Request(url=url, headers={'User-Agent': version._UA_CHROME})
            response = urlopen(request, timeout=5)
            return response.read().decode()
        except URLError:
            return None
