#!/usr/bin/python
# coding=utf-8

from cfg.base.Config import Config


class viva(Config):
    cfgProjectName = 'viva'
    cfgProjectRootDirName = 'viva'
    cfgProjectBranch = 'm8996_viva'
    cfgProjectEnvConfig = 'choosecombo 1 %s userdebug 2 2' % cfgProjectName
    cfgProjectUrlRepoRepository = 'quicl'
