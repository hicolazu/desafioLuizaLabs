import configparser
import sys
import os

__profile = os.environ.get('PROFILE') or sys.argv[1]
__config = configparser.ConfigParser()
__config.read('ConfigFile.ini')


def get_property(key):
    return __config[__profile][key]


def get_profile():
    return __profile
