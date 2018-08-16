#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class current(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'Show current of the device',
    )

    def on_run(self, *params) -> bool:
        self.shell('adb shell cat /sys/class/power_supply/battery/current_now')

        return True
