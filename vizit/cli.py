import os
import sys
from argparse import ArgumentParser

ABOUT_TEXT = 'A simple dependency visualisation tool'
CLI_VERSION_HELP = 'display version information'
CLI_DIR_HELP = 'root directory to search, by default this is the current directory'
CLI_LANG_HELP = 'programming language'
CLI_TO_JSON_DIR = 'location of a .json file to export graph data to for external display'

parser = ArgumentParser(description=ABOUT_TEXT)

def _get_parser():
    # command line argumens
    parser.add_argument('-v', action='version', version='v0.1.0', help=CLI_VERSION_HELP)
    parser.add_argument('-d', action='store', dest='directory', help=CLI_DIR_HELP)
    parser.add_argument('-l', action='store', dest='language', help=CLI_LANG_HELP)
    parser.add_argument('-j', action='store', dest='jsonfile', help=CLI_TO_JSON_DIR)
    return parser.parse_args()

def show_help(msg):
    parser.print_help()
    sys.exit('\n'+msg)

def get_args():
    args = _get_parser()
    dir = args.directory or os.getcwd()
    if args.language:
        return (dir, args.language, args.jsonfile)
    else:
        show_help('')
        