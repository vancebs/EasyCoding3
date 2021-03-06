#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer
import os


class setup(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'setup adb & fastboot for this project',
    )

    def on_run(self, *params) -> bool:
        # create link
        result = True
        result &= self.link('/opt/bin/adb', '%s/out/host/linux-x86/bin/adb' % self.cfg.cfgProjectRootDir)
        result &= self.link('/opt/bin/fastboot', '%s/out/host/linux-x86/bin/fastboot' % self.cfg.cfgProjectRootDir)

        # restart adb
        if result:
            self.shell('adb kill-server')
            self.shell('sudo adb devices')

        return True

    def link(self, link: str, target: str) -> bool:
        if os.path.exists(target):
            self.shell('rm -rf %s' % link)  # remove old link
            self.shell('ln -s %s %s' % (target, link))  # create new link
            Printer.green_line('create link: %s => %s' % (link, target))
            return True
        else:
            Printer.yellow_line('target [%s] not exists. ignore it' % target)
            return False
