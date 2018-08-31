#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer


class begin(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'begin focus mode',
    )

    def on_run(self, *params) -> bool:
        # alias for ec
        project = self.cfg.cfgName
        for cmd in self.cfg.cfgProgramCmdList:
            self.shell('alias ec-%s="ec %s %s"' % (cmd, project, cmd))
            self.shell('alias ec-p-%s="ec -p %s %s"' % (cmd, project, cmd))

        self.shell('export EC_BEGIN=%s' % project)

        # show project on cmd line
        ec_ps1 = self.func('echo $EC_PS1')
        if ec_ps1 == '':
            self.shell('export EC_PS1=$PS1')
        self.shell('export PS1="\033[36m[%s]\033[0m $EC_PS1"' % self.cfg.cfgName)

        return True
