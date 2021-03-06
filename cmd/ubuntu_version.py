#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class ubuntu_version(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'get version of ubuntu',
    )

    def on_run(self, *params) -> bool:
        self.shell('lsb_release -a')

        return True
