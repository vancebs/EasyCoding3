#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print


class dump(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'dump configures',
    )

    def on_run(self, *params) -> bool:
        Print.yellow('======> dump begin')
        Print.blue('EC')
        Print.green('  Dir: %s' % self.cfg.cfgProgramDir)
        Print.green('  cmd dir: %s' % self.cfg.cfgProgramCmdDir)
        Print.green('  cmd list: %s' % self.cfg.cfgProgramCmdList)
        Print.green('  cfg dir: %s' % self.cfg.cfgProgramCfgDir)
        Print.green('  cfg list: %s' % self.cfg.cfgProgramCfgList)
        Print.green('  cfg file: %s' % self.cfg.cfgProgramCfgFile)
        Print.blue('Global')
        Print.green('  base dir: %s' % self.cfg.cfgGlobalBaseDir)
        Print.green('  pull url: %s' % self.cfg.cfgGlobalUrlRepoPull)
        Print.green('  push url: %s' % self.cfg.cfgGlobalUrlRepoPush)
        Print.green('  user name: %s' % self.cfg.cfgGlobalUserName)
        Print.green('  user email: %s' % self.cfg.cfgGlobalUserEmail)
        Print.blue('Project')
        Print.green('  name: %s' % self.cfg.cfgProjectName)
        Print.green('  branch: %s' % self.cfg.cfgProjectBranch)
        Print.green('  root dir: %s' % self.cfg.cfgProjectRootDir)
        Print.green('  out dir: %s' % self.cfg.cfgProjectOutDir)
        Print.green('  env setup: %s' % self.cfg.cfgProjectEnvSetup)
        Print.green('  env config: %s' % self.cfg.cfgProjectEnvConfig)
        Print.green('  flash map: %s' % self.cfg.cfgProjectFlashMap)
        Print.green('  pull url: %s' % self.cfg.cfgProjectUrlRepoPull)
        Print.green('  push url: %s' % self.cfg.cfgProjectUrlRepoPush)
        Print.green('  repo bin: %s' % self.cfg.cfgProjectRepoBin)
        Print.yellow('<====== dump end')

        return True
