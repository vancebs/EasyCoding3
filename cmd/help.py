#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print


class help(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        count = len(params)
        if count <= 0:
            Print.red('please input a command for help.')
            self.help()
            return False
        elif count > 1:
            Print.red('only 1 command is accepted.')
            self.help()
            return False
        else:  # count == 1
            if params[0] not in self.cfg.cfgProgramCmdList:
                Print.red('invalid command.')
                self.help()
                return False

        # get command
        cmd = self.env.load_cmd(params[0])
        cmd.help()

        return True

    def help(self):
        Print.yellow('Command help')
        Print.yellow('  cmd: %s' % self.cfg.cfgProgramCmdList)
