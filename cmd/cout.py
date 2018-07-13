#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print

import os


class cout(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        out_dir = self.cfg.cfgProjectOutDir
        if os.path.exists(out_dir):
            return self.cd(out_dir)
        else:
            Print.red('out path not exists. path: %s' % out_dir)
            return False

    @staticmethod
    def help():
        Print.yellow('switch to project out dir')
