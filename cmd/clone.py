#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Python2 import Python2
from script.util.Print import Print

import datetime
import os
import re


class clone(Cmd):
    _INIT_WORK_DIR: bool = True
    _RESTORE_WORK_DIR: bool = True

    _HELP_MESSAGE = (
        'clone AOSP project by repo',
        '',
        'clone [-j4]',
    )

    def on_run(self, *params) -> bool:
        Print.green('clone ...')

        project_dir = self.cfg.cfgProjectRootDir
        date_file = '.date'
        date = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        temp_dir = '%s/%s' % (self.cfg.cfgProjectBackupDir, date)

        # check -j*
        pattern = re.compile('-j[\d]+')
        thread_param = None
        for p in params:
            if pattern.fullmatch(p):
                thread_param = p
                params = list(params)
                params.remove(p)

        # prepare temp dir under backup dir
        self.shell('mkdir -p %s' % temp_dir)
        self.cd(temp_dir)  # switch to temp dir
        self.shell('eval echo "%s" > ./%s' % (date, date_file))  # create .date file

        # copy file from old project
        self.shell('cp -f "%s/.classpath" "%s/.classpath"' % (project_dir, temp_dir))
        self.shell('cp -f "%s/.project" "%s/.project"' % (project_dir, temp_dir))
        self.shell('cp -rf "%s/.vscode" "%s/.vscode"' % (project_dir, temp_dir))

        # prepare the input text & repo command
        repo_input = '%s\r%s\ry\r' % (self.cfg.cfgGlobalUserName, self.cfg.cfgGlobalUserEmail)
        repo_cmd = '%s init -u %s -m %s.xml --depth=1 --config-name' % (self.cfg.cfgProjectRepoBin,
                                                                        self.cfg.cfgProjectUrlRepoPull,
                                                                        self.cfg.cfgProjectBranch)

        # start clone
        with Python2(self):
            self.shell('eval echo %s | %s' % (repo_input, repo_cmd))
            self.shell('%s sync %s' % (self.cfg.cfgProjectRepoBin, '-j4' if thread_param is None else thread_param))
            self.shell('%s start %s --all' % (self.cfg.cfgProjectRepoBin, self.cfg.cfgProjectBranch))

        # move project dir to backup
        old_date = '%s_backup' % date
        old_date_path = '%s/%s' % (self.cfg.cfgProjectRootDir, date_file)
        if os.path.exists(old_date_path) and os.path.isfile(old_date_path):
            with open(old_date_path) as date_file:
                old_date = date_file.readline().strip()
        backup_dir = '%s/%s' % (self.cfg.cfgProjectBackupDir, old_date)
        self.shell('eval mv -f "%s" "%s"' % (project_dir, backup_dir))

        # move temp dir to project dir
        self.shell('eval mv -f "%s" "%s"' % (temp_dir, project_dir))

        # apply ccache
        self.cd(project_dir)
        self.shell('%s/prebuilts/misc/linux-x86/ccache/ccache -M 50G' % project_dir)

        Print.green('done')
        return True
