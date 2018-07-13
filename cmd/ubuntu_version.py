#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print


class ubuntu_version(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        self.shell('lsb_release -a')

        return True

    @staticmethod
    def help():
        Print.yellow('get version of ubuntu')
