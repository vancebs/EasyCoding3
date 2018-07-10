#!/usr/bin/python
# coding=utf-8

from cfg.base.Config import Config


class pm45(Config):
    cfgProjectName = 'pm45'
    cfgProjectRootDirName = 'pm45'
    cfgProjectBranch = 'm8996_pm90'
    cfgProjectEnvConfig = 'choosecombo 1 %s userdebug 2 2' % cfgProjectName
    cfgProjectUrlRepoRepository = 'quicl'
