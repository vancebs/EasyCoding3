#!/usr/bin/python
# coding=utf-8
from typing import Union

from script.util.Printer import Printer
from cfg.base.Config import Config
from script.Shell import Shell

import os


class Cmd(object):
    _INIT_WORK_DIR: bool = True
    _RESTORE_WORK_DIR: bool = True
    _HELP_MESSAGE = (
        'Empty implement!!!',
    )

    _mShell: Shell
    cfg: Config
    env = None

    def run(self, shell: Shell, cfg: Config, *params) -> bool:
        # save cfg & shell
        self._mShell = shell
        self.cfg = cfg

        # save pwd & switch to project root dir
        pwd = self.pwd()
        if self._INIT_WORK_DIR:
            self.cd(self.cfg.cfgProjectRootDir)

        # run command
        success = self.on_run(*params)

        # restore pwd
        if self._RESTORE_WORK_DIR:
            self.cd(pwd)

        return success

    def on_run(self, *params) -> bool:  # True: success, False: failed
        Printer.yellow_line('empty implement of run()# params: %s' % params)
        return True

    def shell(self, cmd: str) -> int:
        return self._mShell.exec(cmd)

    def func(self, cmd: str) -> str:
        return self._mShell.func(cmd)

    def cmd(self, cmd: str, *params) -> bool:
        loaded_cmd = self.env.load_cmd(cmd)
        return loaded_cmd.run(self._mShell, self.cfg, *params)

    def run_cmd(self, cmd, *params) -> bool:
        cmd.env = self.env
        return cmd.run(self._mShell, self.cfg, *params)

    def cd(self, path: str) -> bool:
        path = os.path.abspath(path)
        if os.path.exists(path) and os.path.isdir(path):
            self.shell('cd %s' % path)
            os.environ['PWD'] = path
            return True
        else:
            return False

    @staticmethod
    def pwd() -> str:
        return os.environ['PWD']

    def env_setup(self) -> bool:
        return self.cmd('env')

    def help(self):
        for line in self._HELP_MESSAGE:
            Printer.yellow_line(line)

    def data_dir(self):
        return '%s/data/%s' % (self.cfg.cfgProgramDir, self.__class__.__name__)

