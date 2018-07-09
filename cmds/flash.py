#!/usr/bin/python
# coding=utf-

from cmds.base.BaseCmd import BaseCmd
from script.util.Print import Print

class flash(BaseCmd):
    def onRun(self, *params):
        # assign path
        flashPath = self.cfg.cfgProjectOutDir
        if (len(params) > 0 and (params[0] == '--path' or params[0] == '-p')):
            if (len(params) < 2):
                Print.red('invalid format of command')
                self.help()
                return
            flashPath = params[1]
            params = params[2:]
        
        # get flash list
        flashDict = self.cfg.cfgProjectFlashMap
        if (len(params) > 0):
            tmpDict = dict()
            for p in params:
                if (p in flashDict):
                    tmpDict[p] = flashDict[p]
                else:
                    Print.red('unknown paration: %s' % p)
                    self.help()
                    return
            flashDict = tmpDict

        # do flash
        self.shell('sudo adb reboot bootloader')
        for partition, img in flashDict.items():
            self.shell('sudo fastboot flash %s %s/%s' % (partition, flashPath, img))
        self.shell('sudo fastboot reboot')
    
    def help(self):
        Print.yellow('flash [-p|--path] [partition1] [partition2] ...')
