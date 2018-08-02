#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class adbsync(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'adb sync',
    )

    def on_run(self, *params) -> bool:
        if not self.env_setup():
            return False

        self.shell('adb root')
        self.shell('adb wait-for-device')
        self.shell('adb shell setenforce 0')
        self.shell('adb remount')
        self.shell('adb disable-verity')

        self.shell('adb sync')

        return True
