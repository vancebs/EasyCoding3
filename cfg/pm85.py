#!/usr/bin/python
# coding=utf-8

from cfg.base.Config import Config


class pm85(Config):
    cfgProjectName = 'PM85'
    cfgProjectRootDirName = 'pm85'
    cfgProjectBranch = 'pm85'
    cfgProjectEnvConfig = 'choosecombo 1 %s userdebug' % cfgProjectName
    cfgProjectUrlRepoRepository = 'quicl'
