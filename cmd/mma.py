#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class mma(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'AOSP mma',
    )

    def on_run(self, *params) -> bool:
        # setup env
        if not self.env_setup():
            return False

        # mma
        self.shell('mma %s' % ' '.join(params))

        return True
