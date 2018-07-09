#!/usr/bin/python
# coding=utf-8

import re
from script.util.Log import Log
from script.util.Print import Print
from script.Env import Env

class EasyCoding(object):
    def shell(self, argv):
        # get program path
        program = argv[0].strip()
        argv = argv[1:] # update argv

        # check argv
        if (len(argv) <= 0):
            Print.red('No project input!!!')
            self.help()
            return

        # get print flag
        doPrint = False
        printFlag = argv[0].strip()
        if (printFlag == '--print' or printFlag == '-p' or printFlag == '-P'):
            doPrint = True
            argv = argv[1:]
        
        # check argv
        if (len(argv) <= 0):
            Print.red('No project input!!!')
            self.help()
            return
        
        # get project
        project = argv[0].strip() if doPrint else printFlag

        # get command
        command = ' '.join(argv[1:]).strip()

        # parser argv
        cmds = list(map(str.strip, command.split(',')))

        # env
        env = Env(printFlag)

        # load cfg
        cfg = env.loadCfg(project)
        if (cfg == None):
            Print.red('load config failed!!')
            return
        
        # load cmd & run
        for c in cmds:
            cmdParts = list(map(str.strip, c.split(' ')))
            cmdName = cmdParts[0]
            cmdParams = cmdParts[1:]

            cmd = env.loadCmd(cmdName)
            if (cmd is None):
                Print.yellow('invalid command %s. drop it.' % cmdName)
            else:
                cmd.run(cfg, *tuple(cmdParams))

    def help(self):
        Print.yellow('ec [--print|-p|-P] <project> CMD1 [PARAM1], [CMD2] [PARAM2]')
        Print.yellow('\t [--print|-p|-P]: print the command instead of execute on shell')
