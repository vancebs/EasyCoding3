#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class addr2line(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'addr2line',
    )

    def on_run(self, *params) -> bool:
        # env
        if not self.env_setup():
            return False

        # addr2line
        self.shell('addr2line -C -f -e %s/symbols/%s %s' % (self.cfg.cfgProjectOutDir, params[1], params[0]))

        return True

