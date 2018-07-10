#!/usr/bin/python
# coding=utf-8

from cfg.base.Config import Config
from cmd.base.Cmd import Cmd
from script.util.Print import Print


class flash(Cmd):
    def on_run(self, cfg: Config, *params):
        # assign path
        flash_path = cfg.cfgProjectOutDir
        if len(params) > 0 and (params[0] == '--path' or params[0] == '-p'):
            if len(params) < 2:
                Print.red('invalid format of command')
                self.help()
                return
            flash_path = params[1]
            params = params[2:]
        
        # get flash list
        flash_dict = cfg.cfgProjectFlashMap
        if len(params) > 0:
            tmp_dict = dict()
            for p in params:
                if p in flash_dict:
                    tmp_dict[p] = flash_dict[p]
                else:
                    Print.red('unknown partition: %s' % p)
                    self.help()
                    return
            flash_dict = tmp_dict

        # do flash
        self.shell(cfg, 'sudo adb reboot bootloader')
        for partition, img in flash_dict.items():
            self.shell(cfg, 'sudo fastboot flash %s %s/%s' % (partition, flash_path, img))
        self.shell(cfg, 'sudo fastboot reboot')
    
    @staticmethod
    def help():
        Print.yellow('flash [-p|--path] [partition1] [partition2] ...')
