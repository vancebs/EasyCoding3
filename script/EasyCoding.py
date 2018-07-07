#!/usr/bin/python
# coding=utf-8

import re
from script.util.Log import Log
from script.util.Print import Print

class EasyCoding(object):
    def shell(self, argv):
        argc = len(argv)
        print(argv, argc)
        if (argc < 3):
            self.help()
            return # command should be at least 3 parts

        # parser argv
        program = argv[0].strip()
        project = argv[1].strip()
        command = ' '.join(argv[2:]).strip()
        cmds = list(map(str.strip, command.split(',')))

        # load cfg
        cfg = self.loadCfg(program, project)

        # run cmds
        self.runs(cfg, cmds)
    
    def loadCfg(self, program, project):
        print('loadCfg', program, project)
        return None

    def runs(self, cfg, cmds):
        print (cmds)

    def help(self):
        Print.red('Wrong command!!!')
        Print.yellow('ec <project> CMD1 [PARAM1], [CMD2] [PARAM2]')
