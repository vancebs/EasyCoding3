#!/usr/bin/python
# coding=utf-8

from script.util.Print import Print


class Shell(object):
    _mFakeExec: bool

    def __init__(self, fake_exec: bool=False):
        self._mFakeExec = fake_exec

    def __enter__(self):
        self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def fake_exec(self, fake_exec: bool):
        self._mFakeExec = fake_exec

    @staticmethod
    def open():
        Print.green('=====> open shell')

    @staticmethod
    def close():
        Print.green('=====> stop shell')
        print('==end==')

    def exec(self, cmd: str):
        if self._mFakeExec:
            cmd = cmd.replace('\r', '\\\\r')
            print('echo %s' % cmd)
        else:
            print(cmd)
