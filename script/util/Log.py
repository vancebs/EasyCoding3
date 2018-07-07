#!/usr/bin/python
# coding=utf-8

from script.util.Print import Print

class Log(object):
    def _makeMessage(tag, msg):
        return '%s: %s' % (tag, msg)

    def i(tag, msg):
        Print.green(Log._makeMessage(tag, msg))
    
    def w(tag, msg):
        Print.yellow(Log._makeMessage(tag, msg))
    
    def e(tag, msg):
        Print.red(Log._makeMessage(tag, msg))
    
    def d(tag, msg):
        Print.blue(Log._makeMessage(tag, msg))
    
    def v(tag, msg):
        Print.white(Log._makeMessage(tag, msg))
   
