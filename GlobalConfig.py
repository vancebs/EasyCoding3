#!/usr/bin/python
# coding=utf-8

##########################################
# Easy Coding 3 global config File       #
##########################################


class GlobalConfig(object):
    # The dir where you keep all your projects
    cfgGlobalBaseDir = '/home/hufan/platforms'

    # URL where you download your project
    # Example:
    #     URL: "ssh://fan.hu@172.16.11.162:29418/quic/manifests.git"
    #     SET: "ssh://fan.hu@172.16.11.162:29418/"
    #
    #     URL: "git@172.16.11.162:quic/manifests.git"
    #     SET: "git@172.16.11.162:"
    cfgGlobalUrlRepoPull = 'git@172.16.11.162:'

    # URL where you push your code.
    # Example:
    #     URL: "ssh://fan.hu@172.16.11.162:29418/quic/manifests.git"
    #     SET: "ssh://fan.hu@172.16.11.162:29418/"
    #
    #     URL: "git@172.16.11.162:quic/manifests.git"
    #     SET: "git@172.16.11.162:"
    cfgGlobalUrlRepoPush = 'ssh://fan.hu@172.16.11.162:29418/'

    # Name which is required to input by repo
    cfgGlobalUserName = 'fan.hu'

    # Email which is required to input by repo
    cfgGlobalUserEmail = 'fan.hu@t2mobile.com'
