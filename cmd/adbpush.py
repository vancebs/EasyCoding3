#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print

import os


class adbpush(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    def on_run(self, *params) -> bool:
        if len(params) < 1:
            Print.red('please input the module to push')
            help()
            return False

        if len(params) > 1:
            Print.red('only one module is supported')
            help()
            return False

        # root device
        self.shell('adb root')
        self.shell('adb wait-for-device')
        self.shell('adb shell setenforce 0')
        self.shell('adb disable-verity')
        self.shell('adb remount')

        # push
        out_dir = self.cfg.cfgProjectOutDir
        module = params[0]
        self.adb_push('[/system/app] APK',
                      '%s/system/app/%s/%s.apk' % (out_dir, module, module),
                      '/system/app/%s' % module)
        self.adb_push('[/system/app] ODEX',
                      '%s/system/app/%s/oat/arm64/%s.odex' % (out_dir, module, module),
                      '/system/app/%s/oat/arm64' % module)
        self.adb_push('[/system/priv-app] APK',
                      '%s/system/priv-app/%s/%s.apk' % (out_dir, module, module),
                      '/system/priv-app/%s' % module)
        self.adb_push('[/system/priv-app] ODEX',
                      '%s/system/priv-app/%s/oat/arm64/%s.odex' % (out_dir, module, module),
                      '/system/priv-app/%s/oat/arm64' % module)
        self.adb_push('[/system/framework] JAR',
                      '%s/system/framework/%s.jar' % (out_dir, module),
                      '/system/framework')
        self.adb_push('[/system/framework] APK',
                      '%s/system/framework/%s.apk' % (out_dir, module),
                      '/system/framework')
        self.adb_push('[/system/framework] ODEX',
                      '%s/system/framework/oat/arm64/%s.odex' % (out_dir, module),
                      '/system/framework/oat/arm64')
        self.adb_push('[/system/vendor/app] APK',
                      '%s/system/vendor/app/%s/%s.apk' % (out_dir, module, module),
                      '/system/vendor/app/%s' % module)
        self.adb_push('[/system/vendor/app] ODEX',
                      '%s/system/vendor/app/%s/oat/arm64/%s.odex' % (out_dir, module, module),
                      '/system/vendor/app/%s/oat/arm64' % module)
        self.adb_push('[system/bin] BIN',
                      '%s/system/bin/%s' % (out_dir, module),
                      '/system/bin')

        if module == 'framework':
            self.adb_push('[/system/framework] ART',
                          '%s/dex_bootjars/system/framework/arm/boot.art' % out_dir,
                          '/system/framework/arm')
            self.adb_push('[/system/framework] ART64',
                          '%s/dex_bootjars/system/framework/arm64/boot.art' % out_dir,
                          '/system/framework/arm64')

        return True

    def adb_push(self, msg, src, dst):
        if os.path.exists(src):
            Print.green('Pushing %s ...' % msg)
            self.shell('adb shell mkdir -p %s' % dst)
            self.shell('adb push %s %s' % (src, dst))
            Print.green('Done')
            return True
        else:
            return False

    @staticmethod
    def help():
        Print.yellow('adb push the module to device')
        Print.yellow('adbpush <module>')
        Print.yellow('i.e. adbpush Settings')
