#!/usr/bin/python3

import os.path
import sys
import argparse

VERSION = '0.1.0'
HOME_DIR = os.path.expanduser("~")
argcfg = None


class MapAction(argparse.Action):

    def __init__(self):
        super(MapAction, self).__init__()

    def __call__(self, parser, namespace, values, option_string=None):
        pass


def parse_arguments():
    global_cfg = os.path.join(HOME_DIR, '.codetemplrc')

    parser = argparse.ArgumentParser(prog='codetempl',
        description='Generate code files from templates.',
        fromfile_prefix_chars='@')
    parser.add_argument('files', help='files to create', nargs='+')
    parser.add_argument('--config', help='read configuration from file')
    parser.add_argument('-v', '--version', help='shows version number',
        action='version',
        version=('codetempl Version ' + VERSION))

    parser.add_argument('--template',
        help='template file to parse')
    parser.add_argument('--esc-char',
        help='escape character for template vars',
        default='$')
    parser.add_argument('--map-ext',
        nargs='*',
        help='map extension to certain template files',
        action=MapAction)
    parser.add_argument('--search-dir',
        nargs='*',
        help='search directories to look for template files')

    myargs = sys.argv
    if os.path.exists(global_cfg):
        myargs = myargs + ['@' + global_cfg]

    argcfg = parser.parse_args(myargs)
    if(argcfg.config is not None):
        myargs = myargs + ['@' + argcfg.config]
        argcfg = parser.parse_args(myargs)


if __name__ == '__main__':
    parse_arguments()
