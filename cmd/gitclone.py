#!/usr/bin/python
# coding=utf-8

from cmd.base.Cmd import Cmd
from script.util.Print import Print

import re
import os


class gitclone(Cmd):
    _INIT_WORK_DIR: bool = False
    _RESTORE_WORK_DIR: bool = False

    _HELP_MESSAGE = (
        'clone a single repository by git',
        '',
        'gitclone <path> [target]',
        '  path: the path under project root. i.e. packages/apps/Settings',
        '  target: target path to clone. can be ignore. if ignored, repository will be saved under dir single',
        '',
        'i.e.  gitclone packages/apps/Settings',
        '      gitclone packages/apps/Settings ./Settings',
    )

    _LINE_PATTERN = re.compile('\s*<project\s*name="([\S]+)"\s*path="([\S]+)"\s*/>\s*')
    _DEFAULT_LOCAL_DIR = 'single'

    def on_run(self, *params) -> bool:
        # get parameters
        # local_path: str = None
        # target_path: str = None
        if len(params) == 1:
            local_path = params[0].strip()
            target_path = os.path.abspath('%s/%s/%s' % (self.cfg.cfgProjectRootDir,
                                                        self._DEFAULT_LOCAL_DIR, local_path))
        elif len(params) == 2:
            local_path = params[0].strip()
            target_path = params[1].strip()
        else:
            Print.red('Invalid number of parameters. Only 2 is accepted.')
            self.help()
            return False

        # check parameter
        if local_path is None or local_path == '':
            Print.red('Invalid parameter 1')
            self.help()
            return False
        if target_path is None or target_path == '':
            Print.red('Invalid parameter 2')
            self.help()
            return False

        # check manifest
        manifest = '%s/.repo/manifest.xml' % self.cfg.cfgProjectRootDir
        if not os.path.exists(manifest):
            Print.red('manifest not exists.')
            Print.red('  Path: %s' % manifest)
            self.help()
            return False

        # search in manifest
        remote_path: str = None
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
            Print.red('Path not find in manifest.')
            Print.red('  Path: %s' % local_path)
            self.help()
            return False

        # clone
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        clone_url = '%s/%s.git' % (self.cfg.cfgProjectUrlRepoPush, remote_path)
        self.shell('git clone %s -b %s %s' % (clone_url, self.cfg.cfgProjectBranch, target_path))

        return True
