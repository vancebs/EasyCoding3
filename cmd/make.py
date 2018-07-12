#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from cmd.env import env
from script.util.Print import Print

import datetime


class make(Cmd):
    _INIT_WORK_DIR: bool = True
    _RESTORE_WORK_DIR: bool = True

    _MAKE_RESULT_FILE = './make_result'

    def on_run(self, *params) -> bool:
        # setup env
        self.run_cmd(env())

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
        self.shell('echo "%s: ==== Begin make ====" > %s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                             self._MAKE_RESULT_FILE))
        return True

    def log_end(self):
        self.shell('echo "%s: ==== End make ====" >> %s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                            self._MAKE_RESULT_FILE))
        return True

    def log_result(self):
        self.shell('echo "%s: result $?" >> %s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                   self._MAKE_RESULT_FILE))
        return True

    @staticmethod
    def help():
        Print.yellow('make AOSP project')