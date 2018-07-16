#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print


class sys(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'execute bash command',
    )

    def on_run(self, *params) -> bool:
        self.shell(' '.join(params))

        return True
