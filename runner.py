# -*- coding: utf-8 -*-
# Copyright (c) 2014 Sandeep Raju. See LICENSE.txt for details.
import os
import sys
import argparse
import signal

from subraminion import Subraminion, __version__

# define & register SIGINT handlers


def signal_handler_for_SIGINT(signal, frame):
    """
    """
    # exit normally
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler_for_SIGINT)


def run():
    """
    """
    # define the CLI
    parser = argparse.ArgumentParser(
        description='Subraminion v%s' % __version__)
    parser.add_argument('directory', help=('Path to the directory where '
                                           'duplicates are to be found.'))
    parser.add_argument('-t', '--type', action='store', required=False,
                        help='The file type to match (ex: mp3, mp4, txt, pdf, etc.).',
                        dest='file_type')
    parser.add_argument('-d', '--delete', action='store_true', required=False,
                        help='Delete the duplicates automatically if found.',
                        dest='delete_duplicates')
    parser.add_argument('-p', '--prompt', action='store_true', required=False,
                        help=('Prompts for action if duplicates are found. '
                              'This option can be used only with -d | --delete'),
                        dest='prompt_user')
    parser.add_argument('-v', '--verbose', action='store_true', required=False,
                        help='Show verbose output while processing files.',
                        dest='verbose_output')
    parser.add_argument('--version', action='version',
                        version='Subraminion %s' % __version__)
    args = parser.parse_args()

    # check the preconditions.
    if not args.delete_duplicates and args.prompt_user:
        # prompt cannot be given without -d | --delete option
        # this should ideally be handled using an argparse custom action
        # http://stackoverflow.com/a/5165960/1044366 - ignoring for now.
        print 'subraminion: error: --prompt can be used only with --delete'
        return
    # normalize the path into an absolute path.
    target_directory = os.path.abspath(args.directory)

    # start processing the files.
    s = Subraminion(target_directory, file_type=args.file_type)
    s.process_files(
        verbose=args.verbose_output,
        delete_duplicates=args.delete_duplicates,
        prompt_user=args.prompt_user
    )

if __name__ == '__main__':
    run()
