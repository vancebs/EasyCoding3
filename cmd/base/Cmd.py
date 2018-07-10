#!/usr/bin/python
# coding=utf-8

from script.util.Print import Print
from cfg.base.Config import Config
import os


class Cmd(object):
    def run(self, cfg: Config, *params):
        self.on_run(cfg, *params)
    
    def on_run(self, cfg: Config, *params):
        Print.yellow('empty implement of run()# params: %s' % params)

    @staticmethod
    def shell(cfg: Config, cmd: str) -> int:
        if cfg.cfgGlobalFakeShell:
            Print.white(cmd)
            return 0
        else:
            return os.system(cmd)
