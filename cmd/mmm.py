#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print


class mmm(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        # setup env
        if self.env_setup():
            return False

        # mma
        self.shell('mmm %s' % ' '.join(params))

        return True

    @staticmethod
    def help():
        Print.yellow('AOSP mmm')
