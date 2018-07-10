#!/usr/bin/python
# coding=utf-8

from script.util.Print import Print


class Log(object):
    @staticmethod
    def _make_message(tag: str, msg: str) -> str:
        return '%s: %s' % (tag, msg)

    @staticmethod
    def i(tag: str, msg: str):
        Print.green(Log._make_message(tag, msg))

    @staticmethod
    def w(tag: str, msg: str):
        Print.yellow(Log._make_message(tag, msg))

    @staticmethod
    def e(tag: str, msg: str):
        Print.red(Log._make_message(tag, msg))

    @staticmethod
    def d(tag: str, msg: str):
        Print.blue(Log._make_message(tag, msg))

    @staticmethod
    def v(tag: str, msg: str):
        Print.white(Log._make_message(tag, msg))
