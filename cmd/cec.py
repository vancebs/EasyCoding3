#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer

import os


class cec(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'switch to ec root dir',
    )

    def on_run(self, *params) -> bool:
        ec_dir = self.cfg.cfgProgramDir
        if os.path.exists(ec_dir):
            return self.cd(ec_dir)
        else:
            Printer.red_line('ec path not exists. path: %s' % ec_dir)
            return False
