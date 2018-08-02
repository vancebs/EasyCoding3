#!/usr/bin/python
# coding=utf-8

import sys

from script.util.Printer import Printer


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
        Printer.green_line('=====> open shell')

    @staticmethod
    def close():
        Printer.green_line('=====> stop shell')
        print('==end==')

    def exec(self, cmd: str) -> int:
        if self._mFakeExec:
            cmd = cmd.replace('\r', '\\\\r')
            Printer.white_line(cmd)
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

    # @staticmethod
    # def shell_exec(cmd: str) -> int:
    #     # send command
    #     print('%s%s' % (Shell._PREFIX_CMD, cmd))
    #
    #     # receive exit code
    #     line = input()
    #
    #     # get exit code
    #     try:
    #         return int(line)
    #     except ValueError:
    #         return 10086  # unknown error

    # @staticmethod
    # def shell_func(cmd: str) -> str:
    #     # send command
    #     print('%s%s' % (Shell._PREFIX_FUNC, cmd))
    #
    #     # receive output
    #     output = []
    #     line = input().strip()
    #     while not line == '==end==':
    #         output.append(line)
    #         line = input().strip()
    #
    #     # get result
    #     return '\n'.join(output).strip()

    @staticmethod
    def exec_cmd(cmd: str) -> int:
        # exec
        sys.stdout.write('cmd:%s\n' % cmd)
        sys.stdout.flush()

        # get cmd exit code
        str_code = sys.stdin.readline().strip()
        try:
            code = int(str_code)
        except ValueError:
            code = 1

        return code

    @staticmethod
    def exec_func(cmd: str) -> tuple:
        # exec
        sys.stdout.write('func:%s\n' % cmd)
        sys.stdout.flush()

        # get cmd exit code
        str_code = sys.stdin.readline().strip()
        try:
            code = int(str_code)
        except ValueError:
            code = 1

        # receive cmd output
        outputs = []
        line = sys.stdin.readline().strip()
        while line != '==end==':
            outputs.append(line)
            line = sys.stdin.readline().strip()
        output = '\n'.join(outputs)

        # return
        return code, output

    @staticmethod
    def shell_exit():
        print('==end==')
