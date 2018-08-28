#!/usr/bin/python
# coding=utf-8

from cfg.base.Config import Config


class pm85(Config):
    cfgProjectName = 'sdm450'  # on pm85 choosecombo project name is different with real project name
    cfgProjectRootDirName = 'pm85'
    cfgProjectBranch = 'pm85'
    cfgProjectEnvConfig = 'choosecombo 1 %s userdebug 2' % 'PM85'
    cfgProjectUrlRepoRepository = 'quicl'
