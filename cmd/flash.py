#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer

import os


class flash(Cmd):
    _INIT_WORK_DIR: bool = True
    _RESTORE_WORK_DIR: bool = True

    _HELP_MESSAGE = (
        'flash [-p|--path] [partition1] [partition2] ...',
    )

    def on_run(self, *params) -> bool:
        # assign path
        flash_path = self.cfg.cfgProjectOutDir
        if len(params) > 0 and (params[0] == '--path' or params[0] == '-p'):
            if len(params) < 2:
                Printer.red_line('invalid format of command')
                self.help()
                return False
            flash_path = os.path.abspath(params[1])
            params = params[2:]
        
        # get flash list
        flash_dict = self.cfg.cfgProjectFlashMap
        if len(params) > 0:
            tmp_dict = dict()
            for p in params:
                if p in flash_dict:
                    tmp_dict[p] = flash_dict[p]
                else:
                    Printer.red_line('unknown partition: %s' % p)
                    self.help()
                    return False
            flash_dict = tmp_dict

        # do flash
        flashed = False
        self.shell('sudo adb reboot bootloader')
        for partition, img in flash_dict.items():
            path = '%s/%s' % (flash_path, img)
            if os.path.exists(path):
                flashed = True
                Printer.green_line('flashing [%s] ...' % img)
                self.shell('sudo fastboot flash %s %s' % (partition, path))
                Printer.green_line('Done')
        self.shell('sudo fastboot reboot')

        # warning for not flash
        if not flashed:
            Printer.yellow_line('No img found to be flashed!!')

        return True
