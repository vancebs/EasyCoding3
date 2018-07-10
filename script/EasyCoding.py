#!/usr/bin/python
# coding=utf-8

from script.util.Print import Print
from script.Env import Env


class EasyCoding(object):
    def shell(self, argv):
        # ignore program path
        argv = argv[1:]

        # check argv
        if len(argv) <= 0:
            Print.red('No project input!!!')
            self.help()
            return

        # get print flag
        do_print = False
        print_flag = argv[0].strip()
        if print_flag == '--print' or print_flag == '-p':
            do_print = True
            argv = argv[1:]

        # check argv
        if len(argv) <= 0:
            Print.red('No project input!!!')
            self.help()
            return

        # get project
        project = argv[0].strip() if do_print else print_flag

        # get command
        command = ' '.join(argv[1:]).strip()

        # parser argv
        cmd_list = list(map(str.strip, command.split(',')))

        # env
        env = Env(print_flag)

        # load cfg
        cfg = env.load_cfg(project)
        if cfg is None:
            Print.red('invalid project: %s' % project)
            Print.yellow('available project: %s' % env.cfgProgramCfgList)
            return

        # check cmd
        cmd_checked = []
        for c in cmd_list:
            cmd_parts = list(map(str.strip, c.split(' ')))
            cmd_name = cmd_parts[0]
            cmd_params = cmd_parts[1:]

            cmd = env.load_cmd(cmd_name)
            if cmd is None:
                Print.red('invalid command: %s.' % cmd_name)
                Print.yellow('available cmd: %s' % env.cfgProgramCmdList)
                return
            else:
                cmd_checked.append({'cmd': cmd, 'params': cmd_params})

        # run cmd
        for c in cmd_checked:
            c['cmd'].run(cfg, *tuple(c['params']))

    @staticmethod
    def help():
        Print.yellow('ec [--print|-p|-P] <project> CMD1 [PARAM1], [CMD2] [PARAM2]')
        Print.yellow('\t [--print|-p|-P]: print the command instead of execute on shell')
