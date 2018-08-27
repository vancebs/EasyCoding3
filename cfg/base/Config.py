#!/usr/bin/python
# coding=utf-8

from GlobalConfig import GlobalConfig


class Config(GlobalConfig):
    # global config
    # cfgGlobalBaseDir = 'NA'
    # cfgGlobalUrlRepoPull = 'NA'
    # cfgGlobalUrlRepoPush = 'NA'
    # cfgGlobalUserName = 'NA'
    # cfgGlobalUserEmail = 'NA'
    cfgGlobalBackupDir = 'NA'  # generated by __init__()

    # program config. auto generated
    cfgProgramDir = 'NA'
    cfgProgramCmdDir = 'NA'
    cfgProgramCfgDir = 'NA'
    cfgProgramCmdList = 'NA'
    cfgProgramCfgList = 'NA'
    cfgProgramCfgFile = 'NA'

    # project config. configured by cfg
    cfgProjectName = 'NA'
    cfgProjectBranch = 'NA'
    cfgProjectRootDir = 'NA'  # generated by __init__()
    cfgProjectRootDirName = 'NA'
    cfgProjectOutDir = 'NA'  # generated by __init__()
    cfgProjectBackupDir = 'NA'  # generated by __init__()
    cfgProjectEnvSetup = './build/envsetup.sh'
    cfgProjectEnvConfig = 'NA'
    cfgProjectFlashMap = {
        'modem': 'NON-HLOS.bin',
        'sbl1': 'sbl1.mbn',
        'sbl2': 'sbl2.mbn',
        'sbl3': 'sbl3.mbn',
        'tz': 'tz.mbn',
        'rpm': 'rpm.mbn',
        'boot': 'boot.img',
        'cache': 'cache.img',
        'system': 'system.img',
        'persist': 'persist.img',
        'userdata': 'userdata.img',
        'recovery': 'recovery.img',
        'custpack': 'custpack.img',
        'vendor': 'vendor.img'
    }
    cfgProjectUrlRepoPull = 'NA'  # generated by __init__()
    cfgProjectUrlRepoPush = 'NA'  # generated by __init__()
    cfgProjectUrlRepoPullManifest = 'manifests'
    cfgProjectUrlRepoRepository = 'quicl'
    cfgProjectRepoBin = 'repo'

    def __init__(self):
        # global
        self.cfgGlobalBackupDir = '%s/backup' % self.cfgGlobalBaseDir

        # project
        self.cfgProjectRootDir = '%s/%s' % (self.cfgGlobalBaseDir, self.cfgProjectRootDirName)
        self.cfgProjectOutDir = '%s/out/target/product/%s' % (self.cfgProjectRootDir, self.cfgProjectName)
        self.cfgProjectBackupDir = '%s/%s' % (self.cfgGlobalBackupDir, self.cfgProjectName)
        self.cfgProjectUrlRepoPull = '%s%s/%s.git' % (self.cfgGlobalUrlRepoPull,
                                                      self.cfgProjectUrlRepoRepository,
                                                      self.cfgProjectUrlRepoPullManifest)
        self.cfgProjectUrlRepoPush = '%s%s' % (self.cfgGlobalUrlRepoPush, self.cfgProjectUrlRepoRepository)

