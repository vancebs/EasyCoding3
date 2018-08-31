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
            self.shell('unalias ec-p-%s' % cmd)

        self.shell('unset EC_BEGIN')

        # recover cmd line
        ec_ps1 = self.func('echo $EC_PS1')
        if ec_ps1 != '':
            self.shell('PS1=$EC_PS1')

        return True
