#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print


class setup(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        # init path
        link_adb = '/opt/bin/adb'
        link_fastboot = '/opt/bin/fastboot'
        target_adb = '%s/out/host/linux-x86/bin/adb' % self.cfg.cfgProjectRootDir
        target_fastboot = '%s/out/host/linux-x86/bin/fastboot' % self.cfg.cfgProjectRootDir

        # remove old link
        self.shell('rm -rf %s' % link_adb)
        self.shell('rm -rf %s' % link_fastboot)

        # new link
        self.shell('ln -s %s %s' % (target_adb, link_adb))
        self.shell('ln -s %s %s' % (target_fastboot, link_fastboot))

        # restart adb
        self.shell('adb kill-server')
        self.shell('sudo adb devices')

        return True

    @staticmethod
    def help():
        Print.yellow('AOSP mmm')
