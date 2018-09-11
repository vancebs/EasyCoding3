#!/usr/bin/python
# coding=utf-8
from typing import List

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class gms_enable(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'enable gms',
    )

    def get_gms_pkg_list(self) -> List[str]:
        str_pkg = self.func('adb shell pm list package').strip()
        pkg_list = list(map(lambda pkg: pkg.split(':')[1].strip(), str_pkg.split(' ')))
        gms_list = list(filter(lambda pkg: (pkg.startswith('com.google')
                                            and pkg != 'com.google.android.setupwizard'
                                            and pkg != 'com.google.android.packageinstaller')
                                           or pkg == 'com.android.chrome'
                                           or pkg == 'com.android.vending', pkg_list))

        return gms_list

    def on_run(self, *params) -> bool:
        self.cmd('root')

        gms_list = self.get_gms_pkg_list()

        for pkg in gms_list:
            code = self.shell('adb shell pm enable %s' % pkg)
            if code != 0:
                Printer.red_line('Enable gms pkg: %s FAILED' % pkg)

        return True
