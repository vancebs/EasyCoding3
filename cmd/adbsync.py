#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print
from cmd.env import env


class adbsync(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        if not self.run_cmd(env()):
            return False

        self.shell('adb root')
        self.shell('adb wait-for-device')
        self.shell('adb shell setenforce 0')
        self.shell('adb remount')
        self.shell('adb disable-verity')

        self.shell('adb sync')

        return True

    @staticmethod
    def help():
        Print.yellow('adb sync')
