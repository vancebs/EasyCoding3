#!/usr/bin/python
# coding=utf-8

from cfg.base.Config import Config
from cmd.base.Cmd import Cmd


class make(Cmd):
    def on_run(self, cfg: Config, *params):
        force_make = False
        if '-f' in params:
            force_make = True
            params = list(params)
            params.remove('-f')

        while self.shell(cfg, 'make %s' % ' '.join(params)) != 0 and force_make:
            # remove out dir
            self.shell(cfg, 'rm -rf %s/out' % cfg.cfgProjectRootDir)

            # repo sync
            self.shell(cfg, 'repo sync')
