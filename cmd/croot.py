#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print

import os


class croot(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'switch to project root dir',
    )

    def on_run(self, *params) -> bool:
        root_dir = self.cfg.cfgProjectRootDir
        if os.path.exists(root_dir):
            return self.cd(root_dir)
        else:
            Print.red('root path not exists. path: %s' % root_dir)
            return False
