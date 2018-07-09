#!/usr/bin/python
# coding=utf-8

import os
from script.util.Print import Print

class Env(object):
    _PROGRAM_DIR = '%s/..'

    cfgProgramDir = None
    cfgProgramCmdDir = None
    cfgProgramCfgDir = None
    cfgProgramCmdList = None
    cfgProgramCfgList = None
    cfgProgramCfgFile = None
    cfgGlobalFakeShell = None

    def __init__(self, fakeShell):
        # get dirs
        self.cfgProgramDir = Env.getProgramDir()
        self.cfgProgramCmdDir = Env.getProgramCmdDir()
        self.cfgProgramCfgDir = Env.getProgramCfgDir()
        self.cfgProgramCmdList = Env.getProgramCmdList()
        self.cfgProgramCfgList = Env.getProgramCfgList()
        self.cfgGlobalFakeShell = fakeShell

    def loadCfg(self, project):
        cfg = self._loadClass('cfgs', project)

        cfg.cfgProgramDir = self.cfgProgramDir
        cfg.cfgProgramCmdDir = self.cfgProgramCmdDir
        cfg.cfgProgramCfgDir = self.cfgProgramCfgDir
        cfg.cfgProgramCmdList = self.cfgProgramCmdList
        cfg.cfgProgramCfgList = self.cfgProgramCfgList
        cfg.cfgProgramCfgFile = os.path.abspath('%s/%s' % (self.cfgProgramCfgDir, project))
        cfg.cfgGlobalFakeShell = self.cfgGlobalFakeShell

        return cfg
    
    def loadCmd(self, cmd):
        return self._loadClass('cmds', cmd)

    def _loadClass(self, module, clazz):
        availableList = Env.getProgramModuleList(Env.getProgramModuleDir(module))
        if (not clazz in availableList):
            Print.red('invalid module: [%s] or class: [%s]' % (module, clazz))
            Print.red('available clazz are: %s' % availableList)
            return None
        
        # load module
        rootModule = __import__(module, globals(), locals(), (clazz,))
        classModule = getattr(rootModule, clazz)
        targetClass = getattr(classModule, clazz)
        obj = targetClass()
        return obj


    def getProgramDir():
        return os.path.abspath(Env._PROGRAM_DIR % os.path.dirname(__file__))
    
    def getProgramCmdDir():
        return Env.getProgramModuleDir('cmds')
    
    def getProgramCfgDir():
        return Env.getProgramModuleDir('cfgs')
    
    def getProgramModuleDir(module):
        return os.path.abspath((Env._PROGRAM_DIR + '/' + module) % os.path.dirname(__file__))

    def getProgramModuleList(dir):
        fileList = list(filter(lambda name: not os.path.isdir('%s/%s' % (dir, name)) and '__init__.py' != name, os.listdir(dir)))
        nameList = list(map(lambda name: name.split('.')[0], fileList))
        return nameList

    def getProgramCmdList():
        return Env.getProgramModuleList(Env.getProgramCmdDir())
    
    def getProgramCfgList():
        return Env.getProgramModuleList(Env.getProgramCfgDir())