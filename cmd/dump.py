#!/usr/bin/python
# coding=utf-8

from cfg.base.Config import Config
from cmd.base.Cmd import Cmd
from script.util.Print import Print


class dump(Cmd):
    def on_run(self, cfg: Config, *params):
        Print.yellow('======> dump begin')
        Print.blue('EC')
        Print.green('  Dir: %s' % cfg.cfgProgramDir)
        Print.green('  cmd dir: %s' % cfg.cfgProgramCmdDir)
        Print.green('  cmd list: %s' % cfg.cfgProgramCmdList)
        Print.green('  cfg dir: %s' % cfg.cfgProgramCfgDir)
        Print.green('  cfg list: %s' % cfg.cfgProgramCfgList)
        Print.green('  cfg file: %s' % cfg.cfgProgramCfgFile)
        Print.blue('Global')
        Print.green('  base dir: %s' % cfg.cfgGlobalBaseDir)
        Print.green('  pull url: %s' % cfg.cfgGlobalUrlRepoPull)
        Print.green('  push url: %s' % cfg.cfgGlobalUrlRepoPush)
        Print.green('  user name: %s' % cfg.cfgGlobalUserName)
        Print.green('  user email: %s' % cfg.cfgGlobalUserEmail)
        Print.blue('Project')
        Print.green('  name: %s' % cfg.cfgProjectName)
        Print.green('  branch: %s' % cfg.cfgProjectBranch)
        Print.green('  root dir: %s' % cfg.cfgProjectRootDir)
        Print.green('  out dir: %s' % cfg.cfgProjectOutDir)
        Print.green('  env setup: %s' % cfg.cfgProjectEnvSetup)
        Print.green('  env config: %s' % cfg.cfgProjectEnvConfig)
        Print.green('  flash map: %s' % cfg.cfgProjectFlashMap)
        Print.green('  pull url: %s' % cfg.cfgProjectUrlRepoPull)
        Print.green('  push url: %s' % cfg.cfgProjectUrlRepoPush)
        Print.green('  repo bin: %s' % cfg.cfgProjectRepoBin)
        Print.yellow('<====== dump end')
