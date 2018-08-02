#!/usr/bin/python
# coding=utf-8

from script.util.Printer import Printer


class Log(object):
    @staticmethod
    def _make_message(tag: str, msg: str) -> str:
        return '%s: %s' % (tag, msg)

    @staticmethod
    def i(tag: str, msg: str):
        Printer.green_line(Log._make_message(tag, msg))

    @staticmethod
    def w(tag: str, msg: str):
        Printer.yellow_line(Log._make_message(tag, msg))

    @staticmethod
    def e(tag: str, msg: str):
        Printer.red_line(Log._make_message(tag, msg))

    @staticmethod
    def d(tag: str, msg: str):
        Printer.blue_line(Log._make_message(tag, msg))

    @staticmethod
    def v(tag: str, msg: str):
        Printer.white_line(Log._make_message(tag, msg))
