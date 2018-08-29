#!/usr/bin/python
# coding=utf-8

import os
from typing import List

from cfg.base.Config import Config
from cmd.base.Cmd import Cmd


class Env(object):
    _PROGRAM_DIR = '%s/..'

    cfgProgramDir: str = None
    cfgProgramCmdDir: str = None
    cfgProgramCfgDir: str = None
    cfgProgramCmdList: list = None
    cfgProgramCfgList: list = None
    cfgProgramCfgFile: str = None

    def __init__(self):
        # get dirs
        self.cfgProgramDir = Env.get_program_dir()
        self.cfgProgramCmdDir = Env.get_program_cmd_dir()
        self.cfgProgramCfgDir = Env.get_program_cfg_dir()
        self.cfgProgramCmdList = Env.get_program_cmd_list()
        self.cfgProgramCfgList = Env.get_program_cfg_list()

    def load_cfg(self, project: str) -> Config:
        cfg = self._load_class('cfg', project)

        # init cfg
        if cfg is not None:
            cfg.cfgProgramDir = self.cfgProgramDir
            cfg.cfgProgramCmdDir = self.cfgProgramCmdDir
            cfg.cfgProgramCfgDir = self.cfgProgramCfgDir
            cfg.cfgProgramCmdList = self.cfgProgramCmdList
            cfg.cfgProgramCfgList = self.cfgProgramCfgList
            cfg.cfgProgramCfgFile = os.path.abspath('%s/%s' % (self.cfgProgramCfgDir, project))

        return cfg

    def load_cmd(self, cmd: str) -> Cmd:
        loaded_cmd = self._load_class('cmd', cmd)
        loaded_cmd.env = self  # set env
        return loaded_cmd

    @staticmethod
    def _load_class(module: str, clazz: str):
        available_list = Env.get_program_module_list(Env.get_program_module_dir(module))
        if clazz not in available_list:
            return None

        # load module
        root_module = __import__(module, globals(), locals(), [clazz, ])
        class_module = getattr(root_module, clazz)
        target_class = getattr(class_module, clazz)
        obj = target_class()
        return obj

    @staticmethod
    def get_program_dir() -> str:
        return os.path.abspath(Env._PROGRAM_DIR % os.path.dirname(__file__))

    @staticmethod
    def get_program_cmd_dir() -> str:
        return Env.get_program_module_dir('cmd')

    @staticmethod
    def get_program_cfg_dir() -> str:
        return Env.get_program_module_dir('cfg')

    @staticmethod
    def get_program_module_dir(module: str) -> str:
        return os.path.abspath((Env._PROGRAM_DIR + '/' + module) % os.path.dirname(__file__))

    @staticmethod
    def get_program_module_list(module: str) -> List[str]:
        file_list = list(filter(lambda name: not os.path.isdir('%s/%s' % (module, name)) and '__init__.py' != name,
                                os.listdir(module)))
        name_list = list(map(lambda name: name.split('.')[0], file_list))
        return name_list

    @staticmethod
    def get_program_cmd_list() -> List[str]:
        return Env.get_program_module_list(Env.get_program_cmd_dir())

    @staticmethod
    def get_program_cfg_list() -> List[str]:
        return Env.get_program_module_list(Env.get_program_cfg_dir())
