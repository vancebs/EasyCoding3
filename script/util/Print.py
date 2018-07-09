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

    def _getImpl():
        if (Print._sImpl == None):
            if ('Windows' in platform.system()):
                Print._sImpl =  Print._PrintWindows()
            else:
                Print._sImpl =  Print._PrintLinux()
            
            # init color
            Print.BLUE = Print._sImpl._FOREGROUND_BLUE
            Print.GREEN = Print._sImpl._FOREGROUND_GREEN
            Print.RED = Print._sImpl._FOREGROUND_RED
            Print.YELLOW = Print._sImpl._FOREGROUND_YELLOW
            Print.WHITE = Print._sImpl._FOREGROUND_WHITE

        return Print._sImpl
    
    def print(msg, color = WHITE):
        Print._getImpl().print(msg, color)
    
    def red(msg):
        Print._getImpl().red(msg)
    
    def green(msg):
        Print._getImpl().green(msg)
    
    def blue(msg):
        Print._getImpl().blue(msg)
    
    def yellow(msg):
        Print._getImpl().yellow(msg)
    
    def white(msg):
        Print._getImpl().white(msg)

    class _PrintWindows(object):
        import sys
        import ctypes

        _STD_INPUT_HANDLE = -10
        _STD_OUTPUT_HANDLE = -11
        _STD_ERROR_HANDLE = -12

        _FOREGROUND_BLUE = 0x01
        _FOREGROUND_GREEN = 0x02
        _FOREGROUND_RED = 0x04
        _FOREGROUND_YELLOW = _FOREGROUND_GREEN | _FOREGROUND_RED
        _FOREGROUND_WHITE = _FOREGROUND_GREEN | _FOREGROUND_RED | _FOREGROUND_BLUE
        _FOREGROUND_INTENSITY = 0x08
        _BACKGROUND_BLUE = 0x10
        _BACKGROUND_GREEN = 0x20
        _BACKGROUND_RED = 0x40
        _BACKGROUND_YELLOW = _BACKGROUND_GREEN | _BACKGROUND_RED
        _BACKGROUND_WHITE = _BACKGROUND_GREEN | _BACKGROUND_RED | _BACKGROUND_BLUE
        _BACKGROUND_INTENSITY = 0x80

        _stdOutHandle = None
        def __init__(self):
            self._stdOutHandle = self.ctypes.windll.kernel32.GetStdHandle(self._STD_OUTPUT_HANDLE)

        def _setCmdColor(self, color, handle):
            return Print._PrintWindows.ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)

        def _resetCmdColor(self):
            self._setCmdColor(Print._PrintWindows._FOREGROUND_WHITE, self._stdOutHandle)

        def print(self, msg, color = _FOREGROUND_WHITE):
            self._setCmdColor(color, self._stdOutHandle)
            Print._PrintWindows.sys.stdout.write('%s\n' % msg)
            self._resetCmdColor()
        
        def red(self, msg):
            self.print(msg, self._FOREGROUND_RED)
        
        def green(self, msg):
            self.print(msg, self._FOREGROUND_GREEN)
        
        def blue(self, msg):
            self.print(msg, self._FOREGROUND_BLUE)
        
        def yellow(self, msg):
            self.print(msg, self._FOREGROUND_YELLOW)
        
        def white(self, msg):
            self.print(msg, self._FOREGROUND_WHITE)
        
    class _PrintLinux(object):
        _FOREGROUND_BLUE = 34
        _FOREGROUND_GREEN = 32
        _FOREGROUND_RED = 31
        _FOREGROUND_YELLOW = 33
        _FOREGROUND_WHITE = 37

        def print(self, msg, color = _FOREGROUND_WHITE):
            print ('\033[%dm%s\033[0m' % (color, msg))
        
        def red(self, msg):
            self.print(msg, self._FOREGROUND_RED)
        
        def green(self, msg):
            self.print(msg, self._FOREGROUND_GREEN)
        
        def blue(self, msg):
            self.print(msg, self._FOREGROUND_BLUE)
        
        def yellow(self, msg):
            self.print(msg, self._FOREGROUND_YELLOW)
        
        def white(self, msg):
            self.print(msg, self._FOREGROUND_WHITE)
