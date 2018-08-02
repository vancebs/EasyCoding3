#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class root(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'Root user device. This command only available for device before MP.',
    )

    def on_run(self, *params) -> bool:
        self.shell('adb shell setprop ro.secure 0')
        self.shell('adb shell setprop ro.debuggable 1')
        self.shell('adb shell setprop ro.allow.mock.location 1')
        self.shell('adb shell setprop persist.sys.usb.config mtp,adb')
        self.shell('adb wait-for-device')
        self.shell('adb root')
        self.shell('adb wait-for-device')
        self.shell('adb shell /system/bin/setenforce 0')
        self.shell('adb remount')
        self.shell('adb disable-verity')

        Printer.green_line('Rooted')

        return True
