import os
import sys
from argparse import ArgumentParser

ABOUT_TEXT = 'A simple dependency visualisation tool'
CLI_VERSION_HELP = 'display version information'
CLI_DIR_HELP = 'root directory to search, by default this is the current directory'
CLI_LANG_HELP = 'programming language'
CLI_JS = 'display graph in browser rather than using pyplot'

parser = ArgumentParser(description=ABOUT_TEXT)

def _get_parser():
    parser.add_argument('-v', '--version', action='version', version='v0.2.3', help=CLI_VERSION_HELP)
    parser.add_argument('-d', '--dir', action='store', dest='directory', help=CLI_DIR_HELP)
    parser.add_argument('-l', '--language', action='store', dest='language', required=True, help=CLI_LANG_HELP)
    parser.add_argument('-j', '--javascript', action='store_true', dest='js', help=CLI_JS)
    return parser.parse_args()

def show_help(msg):
    parser.print_help()
    sys.exit('\n'+msg)

def get_args():
    args = _get_parser()
    dir = args.directory or os.getcwd()
    return (dir, args.language, args.js)
        