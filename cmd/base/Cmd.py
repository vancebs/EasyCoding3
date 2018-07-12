#!/usr/bin/python
# coding=utf-8


from script.util.Print import Print
from cfg.base.Config import Config
from script.Shell import Shell
import os


class Cmd(object):
    _INIT_WORK_DIR: bool = True
    _RESTORE_WORK_DIR: bool = True

    _mShell: Shell
    cfg: Config

    def run(self, shell: Shell, cfg: Config, *params) -> bool:
        # save cfg & shell
        self._mShell = shell
        self.cfg = cfg

        # save pwd & switch to project root dir
        pwd = os.environ['PWD']
        if self._INIT_WORK_DIR:
            self.cd(self.cfg.cfgProjectRootDir)

        # run command
        success = self.on_run(*params)

        # restore pwd
        if self._RESTORE_WORK_DIR:
            self.cd(pwd)

        return success
    
    def on_run(self, *params) -> bool:  # True: success, False: failed
        Print.yellow('empty implement of run()# params: %s' % params)
        return True

    def shell(self, cmd: str) -> int:
        return self._mShell.exec(cmd)

    def run_cmd(self, cmd, *params):
        cmd.run(self._mShell, self.cfg, *params)

    def cd(self, path: str) -> bool:
        path = os.path.abspath(path)
        if os.path.exists(path) and os.path.isdir(path):
            self.shell('cd %s' % path)
            os.environ['PWD'] = path
            return True
        else:
            return False
