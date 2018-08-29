#!/usr/bin/python
# coding=utf-8

from cfg.base.ConfigSh import ConfigSh


class apollo(ConfigSh):
    cfgProjectName = 'apollo'
    cfgProjectRootDirName = 'apollo'
    cfgProjectBranch = 'apollo-o660-dev'
    cfgProjectEnvConfig = 'choosecombo 1 %s userdebug 2 2 2' % cfgProjectName
    cfgProjectUrlRepoRepository = 'soul'
