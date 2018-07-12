#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print


class flash(Cmd):
    _INIT_WORK_DIR: bool = True
    _RESTORE_WORK_DIR: bool = True

    def on_run(self, *params) -> bool:
        # assign path
        flash_path = self.cfg.cfgProjectOutDir
        if len(params) > 0 and (params[0] == '--path' or params[0] == '-p'):
            if len(params) < 2:
                Print.red('invalid format of command')
                self.help()
                return False
            flash_path = params[1]
            params = params[2:]
        
        # get flash list
        flash_dict = self.cfg.cfgProjectFlashMap
        if len(params) > 0:
            tmp_dict = dict()
            for p in params:
                if p in flash_dict:
                    tmp_dict[p] = flash_dict[p]
                else:
                    Print.red('unknown partition: %s' % p)
                    self.help()
                    return False
            flash_dict = tmp_dict

        # do flash
        self.shell('sudo adb reboot bootloader')
        for partition, img in flash_dict.items():
            self.shell('sudo fastboot flash %s %s/%s' % (partition, flash_path, img))
        self.shell('sudo fastboot reboot')

        return True
    
    @staticmethod
    def help():
        Print.yellow('flash [-p|--path] [partition1] [partition2] ...')
