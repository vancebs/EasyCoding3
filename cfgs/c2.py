#!/usr/bin/python
# coding=utf-8

from cfgs.base.BaseConfig import BaseConfig

class c2(BaseConfig):
    cfgProjectName = 'c2'
    cfgProjectRootDirName = 'c2'
    cfgProjectBranch = 'n8996_t2m_m01_c2'
    cfgProjectEnvConfig = 'choosecombo 1 %s userdebug 2 2' % cfgProjectName
    cfgProjectUrlRepoRepository = 'quicl'
