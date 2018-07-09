#!/usr/bin/python
# coding=utf-8

from script.util.Print import Print
import os

class BaseCmd(object):
    cfg = None

    def run(self, cfg, *params):
        self.cfg = cfg

        self.onRun(*params)
    
    def onRun(self, *params):
        Print.yellow('empty implement of run()# params: %s' % params)

    def shell(self, cmd):
        if (self.cfg.cfgGlobalFakeShell):
            Print.white(cmd)
        else:
            os.system(cmd)
