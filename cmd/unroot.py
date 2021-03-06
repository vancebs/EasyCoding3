#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class unroot(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'Root user device. This command only available for device before MP.',
    )

    def on_run(self, *params) -> bool:
        self.shell('adb enable-verity')
        self.shell('adb shell setprop ro.secure 1')
        self.shell('adb shell setprop ro.debuggable 0')
        self.shell('adb shell setprop ro.allow.mock.location 0')
        self.shell('adb shell /system/bin/setenforce 1')
        self.shell('eval result=`adb shell ps | grep adbd`')
        self.shell('eval pid=`echo $result | awk -F " " \'{print $2}\'`')
        self.shell('eval adb shell kill $pid')
        self.shell('unset result')
        self.shell('unset pid')

        Printer.green_line('Unrooted')

        return True
