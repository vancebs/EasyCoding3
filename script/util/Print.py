#!/usr/bin/python
# coding=utf-8

import platform


class Print(object):
    _sImpl = None

    BLUE = None
    GREEN = None
    RED = None
    YELLOW = None
    WHITE = None

    @staticmethod
    def _get_impl():
        if Print._sImpl is None:
            if 'Windows' in platform.system():
                Print._sImpl = Print.PrintWindows()
            else:
                Print._sImpl = Print.PrintLinux()
            
            # init color
            Print.BLUE = Print._sImpl.FOREGROUND_BLUE
            Print.GREEN = Print._sImpl.FOREGROUND_GREEN
            Print.RED = Print._sImpl.FOREGROUND_RED
            Print.YELLOW = Print._sImpl.FOREGROUND_YELLOW
            Print.WHITE = Print._sImpl.FOREGROUND_WHITE

        return Print._sImpl

    @staticmethod
    def print(msg: str, color: int=WHITE):
        Print._get_impl().print(msg, color)

    @staticmethod
    def red(msg: str):
        Print._get_impl().red(msg)

    @staticmethod
    def green(msg: str):
        Print._get_impl().green(msg)

    @staticmethod
    def blue(msg: str):
        Print._get_impl().blue(msg)

    @staticmethod
    def yellow(msg: str):
        Print._get_impl().yellow(msg)

    @staticmethod
    def white(msg: str):
        Print._get_impl().white(msg)

    class PrintWindows(object):
        import sys
        import ctypes

        _STD_INPUT_HANDLE = -10
        _STD_OUTPUT_HANDLE = -11
        _STD_ERROR_HANDLE = -12

        FOREGROUND_BLUE = 0x01
        FOREGROUND_GREEN = 0x02
        FOREGROUND_RED = 0x04
        FOREGROUND_YELLOW = FOREGROUND_GREEN | FOREGROUND_RED
        FOREGROUND_WHITE = FOREGROUND_GREEN | FOREGROUND_RED | FOREGROUND_BLUE
        FOREGROUND_INTENSITY = 0x08
        BACKGROUND_BLUE = 0x10
        BACKGROUND_GREEN = 0x20
        BACKGROUND_RED = 0x40
        BACKGROUND_YELLOW = BACKGROUND_GREEN | BACKGROUND_RED
        BACKGROUND_WHITE = BACKGROUND_GREEN | BACKGROUND_RED | BACKGROUND_BLUE
        BACKGROUND_INTENSITY = 0x80

        _stdOutHandle = None

        def __init__(self):
            self._stdOutHandle = self.ctypes.windll.kernel32.GetStdHandle(self._STD_OUTPUT_HANDLE)

        def _set_cmd_color(self, color: int):
            return Print.PrintWindows.ctypes.windll.kernel32.SetConsoleTextAttribute(self._stdOutHandle, color)

        def _reset_cmd_color(self):
            self._set_cmd_color(Print.PrintWindows.FOREGROUND_WHITE)

        def print(self, msg: str, color: int=FOREGROUND_WHITE):
            self._set_cmd_color(color)
            Print.PrintWindows.sys.stdout.write('%s\n' % msg)
            self._reset_cmd_color()
        
        def red(self, msg: str):
            self.print(msg, self.FOREGROUND_RED)
        
        def green(self, msg: str):
            self.print(msg, self.FOREGROUND_GREEN)
        
        def blue(self, msg: str):
            self.print(msg, self.FOREGROUND_BLUE)
        
        def yellow(self, msg: str):
            self.print(msg, self.FOREGROUND_YELLOW)
        
        def white(self, msg: str):
            self.print(msg, self.FOREGROUND_WHITE)

    class PrintLinux(object):
        FOREGROUND_BLUE = 34
        FOREGROUND_GREEN = 32
        FOREGROUND_RED = 31
        FOREGROUND_YELLOW = 33
        FOREGROUND_WHITE = 37

        @staticmethod
        def print(msg: str, color: int=FOREGROUND_WHITE):
            print('\033[%dm%s\033[0m' % (color, msg))
        
        def red(self, msg: str):
            self.print(msg, self.FOREGROUND_RED)
        
        def green(self, msg: str):
            self.print(msg, self.FOREGROUND_GREEN)
        
        def blue(self, msg: str):
            self.print(msg, self.FOREGROUND_BLUE)
        
        def yellow(self, msg: str):
            self.print(msg, self.FOREGROUND_YELLOW)
        
        def white(self, msg: str):
            self.print(msg, self.FOREGROUND_WHITE)
