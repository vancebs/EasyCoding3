#!/usr/bin/python
# coding=utf-8

from cfg.base.Config import Config
from cmd.base.Cmd import Cmd


class mma(Cmd):
    def on_run(self, cfg: Config, *params):
        self.shell(cfg, 'mma %s' % ' '.join(params))
