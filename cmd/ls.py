#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class ls(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'adb shell ls --color -CF <PATH>',
    )

    def on_run(self, *params) -> bool:
        self.shell('adb shell ls --color -CF %s' % ' '.join(params))

        return True
