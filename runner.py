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
                        help='Prompts for action if duplicates are found.',
                        dest='prompt_user')
    parser.add_argument('-v', '--verbose', action='store_true', required=False,
                        help='Show verbose output while processing files.',
                        dest='verbose_output')
    parser.add_argument('--version', action='version',
                        version='Subraminion %s' % __version__)
    args = parser.parse_args()

    # normalize the path into an absolute path.
    target_directory = os.path.abspath(args.directory)

    # start processing the files.
    s = Subraminion(target_directory)
    s.process_files(verbose=args.verbose_output)
    duplicate_file_list = s.get_duplicate_file_list()
    if len(duplicate_file_list) > 0:
        print 'Sets with Duplicates!'
    else:
        print 'No duplicates were found!'
    for i in xrange(len(duplicate_file_list)):
        print '- [set %s]' % (i + 1), '-' * 80
        for j in xrange(len(duplicate_file_list[i])):
            print '(%s) %s' % (j + 1, duplicate_file_list[i][j])
        print ''


if __name__ == '__main__':
    run()
