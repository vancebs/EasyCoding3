#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class dump(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'dump configures',
    )

    def on_run(self, *params) -> bool:
        Printer.yellow_line('======> dump begin')
        Printer.blue_line('EC')
        Printer.green_line('  Dir: %s' % self.cfg.cfgProgramDir)
        Printer.green_line('  cmd dir: %s' % self.cfg.cfgProgramCmdDir)
        Printer.green_line('  cmd list: %s' % self.cfg.cfgProgramCmdList)
        Printer.green_line('  cfg dir: %s' % self.cfg.cfgProgramCfgDir)
        Printer.green_line('  cfg list: %s' % self.cfg.cfgProgramCfgList)
        Printer.green_line('  cfg file: %s' % self.cfg.cfgProgramCfgFile)
        Printer.blue_line('Global')
        Printer.green_line('  base dir: %s' % self.cfg.cfgGlobalBaseDir)
        Printer.green_line('  pull url: %s' % self.cfg.cfgGlobalUrlRepoPull)
        Printer.green_line('  push url: %s' % self.cfg.cfgGlobalUrlRepoPush)
        Printer.green_line('  user name: %s' % self.cfg.cfgGlobalUserName)
        Printer.green_line('  user email: %s' % self.cfg.cfgGlobalUserEmail)
        Printer.blue_line('Project')
        Printer.green_line('  name: %s' % self.cfg.cfgProjectName)
        Printer.green_line('  branch: %s' % self.cfg.cfgProjectBranch)
        Printer.green_line('  root dir: %s' % self.cfg.cfgProjectRootDir)
        Printer.green_line('  out dir: %s' % self.cfg.cfgProjectOutDir)
        Printer.green_line('  env setup: %s' % self.cfg.cfgProjectEnvSetup)
        Printer.green_line('  env config: %s' % self.cfg.cfgProjectEnvConfig)
        Printer.green_line('  flash map: %s' % self.cfg.cfgProjectFlashMap)
        Printer.green_line('  pull url: %s' % self.cfg.cfgProjectUrlRepoPull)
        Printer.green_line('  push url: %s' % self.cfg.cfgProjectUrlRepoPush)
        Printer.green_line('  repo bin: %s' % self.cfg.cfgProjectRepoBin)
        Printer.yellow_line('<====== dump end')

        return True
