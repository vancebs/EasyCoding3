#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class help(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        count = len(params)
        if count <= 0:
            Printer.red_line('please input a command for help.')
            self.help()
            return False
        elif count > 1:
            Printer.red_line('only 1 command is accepted.')
            self.help()
            return False
        else:  # count == 1
            if params[0] not in self.cfg.cfgProgramCmdList:
                Printer.red_line('invalid command.')
                self.help()
                return False

        # get command
        cmd = self.env.load_cmd(params[0])
        cmd.cfg = self.cfg
        cmd.help()

        return True

    def help(self):
        Printer.yellow_line('Show help of the command')
        Printer.yellow_line('')
        Printer.yellow_line('cmd: %s' % self.cfg.cfgProgramCmdList)
