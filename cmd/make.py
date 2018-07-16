#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print

import datetime


class make(Cmd):
    _INIT_WORK_DIR: bool = True
    _RESTORE_WORK_DIR: bool = True

    _HELP_MESSAGE = (
        'make AOSP project',
    )

    _MAKE_RESULT_FILE = './make_result'

    def on_run(self, *params) -> bool:
        # setup env
        if not self.env_setup():
            return False

        # do make
        force_make = False
        if '-f' in params:
            force_make = True
            params = list(params)
            params.remove('-f')

        self.log_begin()
        while self.shell('make %s' % ' '.join(params)) != 0 and self.log_result() and force_make:
            # remove out dir
            self.shell('rm -rf %s/out' % self.cfg.cfgProjectRootDir)

            # repo sync
            self.shell('repo sync')

        self.log_end()
        return True

    def log_begin(self):
        self.shell('eval echo "%s: ==== Begin make ====" > %s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                                  self._MAKE_RESULT_FILE))
        return True

    def log_end(self):
        self.shell('eval echo "%s: ==== End make ====" >> %s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                                 self._MAKE_RESULT_FILE))
        return True

    def log_result(self):
        self.shell('eval echo "%s: result $?" >> %s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                        self._MAKE_RESULT_FILE))
        return True
