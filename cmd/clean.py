#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer

import os


class clean(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'clean temp file of module',
        '',
        'clean <module>',
        'i.e. clean Settings',
    )

    def on_run(self, *params) -> bool:
        if len(params) < 1:
            Printer.red_line('please input the module to clean')
            help()
            return False

        if len(params) > 1:
            Printer.red_line('only one module is supported')
            help()
            return False

        module = params[0]
        root = self.cfg.cfgProjectRootDir
        name = self.cfg.cfgProjectName
        out = self.cfg.cfgProjectOutDir

        # app temp out folder
        self.remove('%s/out/target/common/obj/APPS/%s_intermediates' % (root, module))

        # custpack out folder for old platform
        self.remove('%s/out/target/common/jrdResCust/packages/apps/%s' % (root, module))

        # custpack out folder for packages/apps
        self.remove('%s/out/target/perso/%s/jrdResAssetsCust/packages/apps/%s' % (root, name, module))

        # custpack out folder for vendor/tct/source/apps
        self.remove('%s/out/target/perso/%s/jrdResAssetsCust/vendor/tct/source/apps/%s' % (root, name, module))

        # custpack out folder for frameworks/base/packages
        self.remove('%s/out/target/perso/%s/jrdResAssetsCust/frameworks/base/packages/%s' % (root, name, module))

        # custpack out folder for frameworks/base/services
        self.remove('%s/out/target/perso/%s/jrdResAssetsCust/frameworks/base/services/%s' % (root, name, module))

        # custpack out folder for packages/providers
        self.remove('%s/out/target/perso/%s/jrdResAssetsCust/packages/providers/%s' % (root, name, module))

        # apk under system/app
        self.remove('%s/system/app/%s' % (out, module))

        # apk under system/priv-app
        self.remove('%s/system/priv-app/%s' % (out, module))

        return True

    def remove(self, path: str):
        if os.path.exists(path):
            self.shell('rm -rf %s' % path)
            Printer.green_line('Removed: %s' % path)
