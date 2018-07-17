#!/usr/bin/python
# coding=utf-8

from cfg.base.Config import Config


class c2(Config):
    cfgProjectName = 'c2'
    cfgProjectRootDirName = 'c2'
    cfgProjectBranch = 'n8996_t2m_m01_c2'
    cfgProjectEnvConfig = 'choosecombo 1 %s userdebug 2 2 2' % cfgProjectName
    cfgProjectUrlRepoRepository = 'quicl'
