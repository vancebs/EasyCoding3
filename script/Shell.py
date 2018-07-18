#!/usr/bin/python
# coding=utf-8

from script.util.Print import Print


class Shell(object):
    _mFakeExec: bool

    _PREFIX_CMD = 'cmd:'
    _PREFIX_FUNC = 'func:'

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

    def exec(self, cmd: str) -> int:
        if self._mFakeExec:
            cmd = cmd.replace('\r', '\\\\r')
            Print.white(cmd)
            return 0
        else:
            # print(cmd)
            return self._exec_internal(cmd)

    def _exec_internal(self, cmd: str) -> int:
        # send command
        print('%s%s' % (self._PREFIX_CMD, cmd))

        # receive exit code
        line = input()

        # get exit code
        try:
            return int(line)
        except ValueError:
            return 10086  # unknown error

    def func(self, cmd: str) -> str:
        # send command
        print('%s%s' % (self._PREFIX_FUNC, cmd))

        # receive output
        output = []
        line = input().strip()
        while not line == '==end==':
            output.append(line)
            line = input().strip()

        # get result
        return '\n'.join(output).strip()

    @staticmethod
    def shell_exec(cmd: str) -> int:
        # send command
        print('%s%s' % (Shell._PREFIX_CMD, cmd))

        # receive exit code
        line = input()

        # get exit code
        try:
            return int(line)
        except ValueError:
            return 10086  # unknown error

    @staticmethod
    def shell_func(cmd: str) -> str:
        # send command
        print('%s%s' % (Shell._PREFIX_FUNC, cmd))

        # receive output
        output = []
        line = input().strip()
        while not line == '==end==':
            output.append(line)
            line = input().strip()

        # get result
        return '\n'.join(output).strip()

    @staticmethod
    def shell_exit():
        print('==end==')
