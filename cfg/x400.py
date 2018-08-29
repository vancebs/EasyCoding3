#!/usr/bin/python
# coding=utf-8

from cfg.base.ConfigSh import ConfigSh


class apollo(ConfigSh):
    cfgProjectName = 'x400'
    cfgProjectRootDirName = 'x400'
    cfgProjectBranch = 'dtx400-devel'
    cfgProjectEnvConfig = 'choosecombo 1 %s userdebug 2 2 2' % cfgProjectName
    cfgProjectUrlRepoRepository = 'soul'
