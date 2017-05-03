#!/usr/bin/python3

import os.path
import sys
import argparse

VERSION = '0.1.0'
HOME_DIR = os.path.expanduser("~")


def map_ext2file(arglist):
    result = {}

    for arg in arglist:
        splits = arg.split(":")
        if len(splits) != 2:
            print('Error: invalid mapping {}'.format(arg))
            sys.exit(1)

        result[splits[0]] = splits[1]

    return result


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
    parser.add_argument('--esc-char',
        dest='esc',
        help='Escape character for template variables',
        default='$')
    parser.add_argument('--map-ext',
        nargs='*',
        dest='map_ext',
        help='map extension to certain template files',
        action='append',
        default=[])
    parser.add_argument('--search-dir',
        nargs='*',
        dest='search_dir',
        help='search directories to look for template files',
        action='append',
        default=[])

    myargs = sys.argv
    if os.path.exists(global_cfg):
        myargs = myargs + ['@' + global_cfg]

    cfg = parser.parse_args(myargs)
    if(cfg.config is not None):
        myargs = myargs + ['@' + cfg.config]
        cfg = parser.parse_args(myargs)

    cfg.map_ext = map_ext2file(cfg.map_ext)

    return cfg


def replace_macros(content, cfg):
    pass


def create_templates(cfg):
    for filename in cfg.files:
        ext = os.path.splitext(filename)[1]

        if ext not in cfg.map_ext:
            print("Warning: no template for extension .{}".format(ext))
            continue

        templ_name = cfg.map_ext[ext]
        templ_path = None

        for templ_dir in cfg.search_dir:
            templ_path = os.path.join(templ_dir, templ_name)
            if os.path.exists(templ_path):
                break

        if not os.path.exists(templ_path):
            print('Warning: no path found for {}'.format(templ_name))
            continue

        templ_content = ''
        with open(templ_path, 'r') as f:
            templ_content = f.read()

        templ_content = replace_macros(templ_content)

        with open(filename, 'w') as f:
            f.write(templ_content)


if __name__ == '__main__':
    cfg = parse_arguments()
    create_templates(cfg)
