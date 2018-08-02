#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Printer import Printer

import os
import re


class gitpush(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'push this module to remote repository by git',
        '',
        'gitpush [path]',
        '  path: path under project root',
        '',
        'i.e. gitpush',
        'i.e. gitpush packages/apps/Settings',
    )

    _LINE_PATTERN = re.compile('\s*<project\s*name="([\S]+)"\s*path="([\S]+)"\s*/>\s*')

    def on_run(self, *params) -> bool:
        project_root = os.path.abspath(self.cfg.cfgProjectRootDir)
        project_root_dir = '%s/' % project_root

        # get pwd
        pwd = os.path.abspath(self.pwd())
        if len(params) == 1:
            pwd = os.path.abspath('%s/%s' % (self.cfg.cfgProjectRootDir, params[0]))
            if not os.path.exists(pwd):
                Printer.red_line('Path to push not exists')
                Printer.red_line('  Path: %s' % pwd)
                self.help()
                return False

        # check pwd
        if not pwd.startswith(project_root_dir):
            Printer.red_line('Current path is not valid. Please enter the dir of repository to push')
            Printer.red_line('  Current path: %s' % pwd)
            Printer.red_line('  Project path: %s' % project_root)
            self.help()
            return False

        # get local path under project root dir
        local_path = pwd.replace(project_root_dir, '')

        # check manifest
        manifest = '%s/.repo/manifest.xml' % project_root
        if not os.path.exists(manifest):
            Printer.red_line('manifest not exists.')
            Printer.red_line('  Path: %s' % manifest)
            self.help()
            return False

        # search in manifest
        remote_path = None
        with open(manifest, 'r') as file:
            for line in file:
                match = self._LINE_PATTERN.fullmatch(line)
                if match is None:
                    continue

                git_remote_path = match[1].strip()
                git_local_path = match[2].strip()

                if git_local_path == local_path:
                    remote_path = git_remote_path
                    break

        # check remote path
        if remote_path is None:
            Printer.red_line('Path not find in manifest.')
            Printer.red_line('  Path: %s' % local_path)
            self.help()
            return False

        # do push
        push_url = '%s/%s.git' % (self.cfg.cfgProjectUrlRepoPush, remote_path)
        head = 'HEAD:refs/for/%s' % self.cfg.cfgProjectBranch
        self.shell('git push %s %s' % (push_url, head))

        return True
