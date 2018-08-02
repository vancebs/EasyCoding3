#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer
import os


class env(Cmd):
    _INIT_WORK_DIR: bool = True
    _RESTORE_WORK_DIR: bool = True

    _HELP_MESSAGE = (
        'env setup and choosecombo',
    )

    def on_run(self, *params) -> bool:
        target_product = self.cfg.cfgProjectName
        current_product = os.environ.get('ENV_PRODUCT')
        if current_product == target_product:
            Printer.yellow_line('Already initialized for %s!!!' % current_product)
            return True
        elif current_product is not None and current_product != '':
            Printer.red_line('Already initialized for [%s]. Please start a new terminal.' % current_product)
            return False
        else:
            # notify start
            Printer.green_line('Initializing for [%s] ...' % target_product)

            # begin env setup
            self.shell('source %s' % self.cfg.cfgProjectEnvSetup)
            self.shell('%s' % self.cfg.cfgProjectEnvConfig)

            # save current product
            self.shell('export ENV_PRODUCT=%s' % target_product)

            # notify done
            Printer.green_line('Done => Current Project: [%s]' % target_product)

            return True
