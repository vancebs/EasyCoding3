#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd


class Python2(object):
    _mCondaAvailable: bool = False
    _mCmd: Cmd = None
    _mActivate: str = None
    _mDeactivate: str = None
    _mEnv2: str = None

    def __init__(self, cmd: Cmd):
        self._mCmd = cmd
        self._CondaAvailable = self._mCmd.func('eval echo $CONDA_PATH') != ''
        if self._CondaAvailable:
            self._mActivate = self._mCmd.func('eval echo $CONDA_ACTIVATE').strip()
            self._mDeactivate = self._mCmd.func('eval echo $CONDA_DEACTIVATE').strip()
            self._mEnv2 = self._mCmd.func('eval echo $CONDA_ENV_NAME_2').strip()

    def __enter__(self):
        self.enter_python_2()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit_python_2()

    def enter_python_2(self):
        if self._CondaAvailable:
            self._mCmd.shell('source %s %s' % (self._mActivate, self._mEnv2))

    def exit_python_2(self):
        if self._CondaAvailable:
            self._mCmd.shell('source %s' % self._mDeactivate)