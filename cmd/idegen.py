#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class idegen(Cmd):
    _INIT_WORK_DIR: bool = True
    _RESTORE_WORK_DIR: bool = True

    _HELP_MESSAGE = (
        'generate IDE files',
    )

    def on_run(self, *params) -> bool:
        # setup env
        if not self.env_setup():
            return False

        # make project files
        self.shell('mmma development/tools/idegen')
        self.shell('development/tools/idegen/idegen.sh')

        return True
