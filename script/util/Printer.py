#!/usr/bin/python
# coding=utf-8

import sys


class Printer(object):
    BLACK = '\033[30m'  # 红色
    RED = '\033[31m'  # 红色
    GREEN = '\033[32m'  # 绿色
    YELLOW = '\033[33m'  # 黄色
    BLUE = '\033[34m'  # 蓝色
    PURPLE = '\033[35m'  # 紫红色
    CYAN = '\033[36m'  # 青蓝色
    WHITE = '\033[37m'  # 白色

    #: no color
    RESET = '\033[0m'  # 终端默认颜色

    @staticmethod
    def print(msg: str):
        sys.stdout.write(msg)
        sys.stdout.write('\\\\c\n')
        sys.stdout.flush()

    @staticmethod
    def print_line(msg: str):
        sys.stdout.write(msg)
        sys.stdout.write('\\\\n\\\\c\n')
        sys.stdout.flush()

    @staticmethod
    def next_line():
        sys.stdout.write('\\\\n\\\\c\n')
        sys.stdout.flush()

    @staticmethod
    def return_line():
        sys.stdout.write('\\\\r\\\\c\n')
        sys.stdout.flush()

    @staticmethod
    def color(color: str, msg: str):
        Printer.print('%s%s%s' % (color, msg, Printer.RESET))

    @staticmethod
    def color_line(color: str, msg: str):
        Printer.print_line('%s%s%s' % (color, msg, Printer.RESET))

    @staticmethod
    def red(msg: str):
        Printer.color(Printer.RED, msg)

    @staticmethod
    def red_line(msg: str):
        Printer.color_line(Printer.RED, msg)

    @staticmethod
    def green(msg: str):
        Printer.color(Printer.GREEN, msg)

    @staticmethod
    def green_line(msg: str):
        Printer.color_line(Printer.GREEN, msg)

    @staticmethod
    def yellow(msg: str):
        Printer.color(Printer.YELLOW, msg)

    @staticmethod
    def yellow_line(msg: str):
        Printer.color_line(Printer.YELLOW, msg)

    @staticmethod
    def blue(msg: str):
        Printer.color(Printer.BLUE, msg)

    @staticmethod
    def blue_line(msg: str):
        Printer.color_line(Printer.BLUE, msg)

    @staticmethod
    def purple(msg: str):
        Printer.color(Printer.PURPLE, msg)

    @staticmethod
    def purple_line(msg: str):
        Printer.color_line(Printer.PURPLE, msg)

    @staticmethod
    def cyan(msg: str):
        Printer.color(Printer.CYAN, msg)

    @staticmethod
    def cyan_line(msg: str):
        Printer.color_line(Printer.CYAN, msg)

    @staticmethod
    def white(msg: str):
        Printer.color(Printer.WHITE, msg)

    @staticmethod
    def white_line(msg: str):
        Printer.color_line(Printer.WHITE, msg)

    @staticmethod
    def black(msg: str):
        Printer.color(Printer.BLACK, msg)

    @staticmethod
    def black_line(msg: str):
        Printer.color_line(Printer.BLACK, msg)
