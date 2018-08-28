#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer

import os


class cbackup(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'switch to project backup dir',
    )

    def on_run(self, *params) -> bool:
        backup_dir = self.cfg.cfgProjectBackupDir
        if os.path.exists(backup_dir):
            return self.cd(backup_dir)
        else:
            Printer.red_line('backup path not exists. path: %s' % backup_dir)
            return False
