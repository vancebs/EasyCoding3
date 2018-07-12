#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from cmd.env import env


class mm(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        # setup env
        self.run_cmd(env())

        # mm
        self.shell('mm %s' % ' '.join(params))

        return True
