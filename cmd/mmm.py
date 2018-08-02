#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class mmm(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'AOSP mmm',
    )

    def on_run(self, *params) -> bool:
        # setup env
        if not self.env_setup():
            return False

        # mma
        self.shell('mmm %s' % ' '.join(params))

        return True
