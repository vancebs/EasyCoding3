#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print


class croot(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        return self.cd(self.cfg.cfgProjectRootDir)

    @staticmethod
    def help():
        Print.yellow('switch to project root dir')