#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class end(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'end focus mode',
    )

    def on_run(self, *params) -> bool:
        # alias for ec
        for cmd in self.cfg.cfgProgramCmdList:
            self.shell('unalias ec-%s' % cmd)

        self.shell('unset EC_BEGIN')

        return True
