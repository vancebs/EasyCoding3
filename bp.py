#!/usr/bin/python
# coding=utf-8

import sys
from typing import Tuple

from script.util.Printer import Printer
from script.EasyCoding import EasyCoding


def on_launch(argv: list):
    ec = EasyCoding()
    ec.shell(argv)


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


def exec_func(cmd: str) -> Tuple[int, str]:
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


def launch():
    # parser args
    on_launch(sys.argv)

    # end
    print('==end==')


if __name__ == "__main__":
    launch()
