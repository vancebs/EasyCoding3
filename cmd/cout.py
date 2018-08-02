#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer

import os


class cout(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'switch to project out dir',
    )

    def on_run(self, *params) -> bool:
        out_dir = self.cfg.cfgProjectOutDir
        if os.path.exists(out_dir):
            return self.cd(out_dir)
        else:
            Printer.red_line('out path not exists. path: %s' % out_dir)
            return False
