#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from cmd.env import env
from script.util.Print import Print


class mma(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        # setup env
        self.run_cmd(env())

        # mma
        self.shell('mma %s' % ' '.join(params))

        return True

    @staticmethod
    def help():
        Print.yellow('AOSP mma')
