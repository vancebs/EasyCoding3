#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print

import os


class showbackup(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'Show backup of the project',
    )

    def on_run(self, *params) -> bool:
        backup_list = list(os.listdir(self.cfg.cfgProjectBackupDir))

        Print.green('%s backup found.' % len(backup_list))
        for i in backup_list:
            Print.green('[%s] => %s/%s' % (i, self.cfg.cfgProjectBackupDir, i))

        return True
