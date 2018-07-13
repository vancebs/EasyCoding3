#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from cmd.env import env
from script.util.Print import Print


class mm(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        # setup env
        if self.run_cmd(env()):
            return False

        # mm
        self.shell('mm %s' % ' '.join(params))

        return True

    @staticmethod
    def help():
        Print.yellow('AOSP mm')
