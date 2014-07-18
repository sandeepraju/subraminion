# -*- coding: utf-8 -*-
# Copyright (c) 2014 Sandeep Raju. See LICENSE.txt for details.
import os
import sys
import re
import hashlib
import traceback
from collections import defaultdict


class Subraminion(object):

    """
    """

    def __init__(self, base_path, file_type=None):
        """
        """
        self._sha1_file_map = defaultdict(list)
        self._duplicate_file_list = []
        self._base_path = base_path
        self._file_type_regex = re.compile(
            r'\.%s$' % file_type) if file_type else None

    def process_files(self, verbose=False, delete_duplicates=False, prompt_user=False):
        """
        """
        # http://stackoverflow.com/a/16974952/1044366
        for root, dirs, files in os.walk(self._base_path):
            for f in files:
                if self._file_type_regex and not self._file_type_regex.search(f):
                    # ignore files that do not come under the filter
                    continue
                file_path = os.path.join(root, f)
                if not os.path.isfile(file_path):
                    # ignore any non regular files.
                    continue
                if verbose:
                    print '[processing] %s' % file_path
                try:
                    file_sha1 = self._calculate_sha1(file_path)
                except IOError as e:
                    print str(e)
                    continue
                except Exception as e:
                    # print traceback
                    traceback.print_exc(file=sys.stdout)
                    sys.exit(1)  # abnormal exit
                self._sha1_file_map[file_sha1].append(file_path)

        # generate a duplicate list from the sha file map.
        self._duplicate_file_list = filter(
            lambda x: True if len(x) > 1 else False, self._sha1_file_map.values())

        if delete_duplicates and not prompt_user:
            # exterminator mode!
            self._delete_duplicate_files()
            return

        if delete_duplicates and prompt_user:
            # prompt before deleting
            for i in xrange(len(self._duplicate_file_list)):
                print '- [set %s]' % (i + 1), '-' * 80
                for j in xrange(len(self._duplicate_file_list[i])):
                    print '(%s) %s' % (j + 1, self._duplicate_file_list[i][j])
                print ''
                print 'What do we do now?'
                print '[1] Delete all duplicates.'
                print '[2] Let me pick the ones to delete.'
                exit_flag = False
                while not exit_flag:
                    choice = raw_input('Your choice: ')
                    if choice not in ('1', '2'):
                        print 'Invalid option! Try again...'
                    else:
                        if choice == '1':
                            for file_path in self._duplicate_file_list[i][1:]:
                                print '[deleting] %s' % file_path
                                os.remove(file_path)
                        elif choice == '2':
                            print 'Enter the file id (space separated for multiple)'
                            while True:
                                choice = raw_input('>>')
                                if not set(choice).issubset(set(list('0123456789 '))):
                                    # invalid input
                                    print 'Invalid option! Try again...'
                                else:
                                    # ugly hacks for user input validation :\
                                    choice_list = list(
                                        set((choice + ' ').split(' ')))
                                    # get the null str to the start
                                    choice_list.sort()
                                    choice_list = [int(x)
                                                   for x in choice_list[1:]]
                                    delete_list = list(
                                        set(range(1, len(self._duplicate_file_list[i]) + 1)) & set(choice_list))
                                    invalid_list = list(
                                        set(choice_list) - set(range(1, len(self._duplicate_file_list[i]) + 1)))
                                    for j in invalid_list:
                                        print '[ignoring] Invalid option %s.' % str(j)
                                    for j in delete_list:
                                        # as j starts with 1
                                        print '[deleting] %s' % self._duplicate_file_list[i][j - 1]
                                        os.remove(
                                            self._duplicate_file_list[i][j - 1])
                                    break
                        exit_flag = True
            return

        # just list the duplicate files.
        self._pretty_print_duplicate_file_list()

    def _pretty_print_duplicate_file_list(self):
        """
        """
        if len(self._duplicate_file_list) > 0:
            print 'Duplicate files were found!'
        else:
            print 'No duplicates were found!'
            return
        for i in xrange(len(self._duplicate_file_list)):
            print '- [set %s]' % (i + 1), '-' * 80
            for j in xrange(len(self._duplicate_file_list[i])):
                print '(%s) %s' % (j + 1, self._duplicate_file_list[i][j])
            print ''

    def _delete_duplicate_files(self):
        """
        """
        for file_set in self._duplicate_file_list:
            # delete all copies except the first one.
            for file_path in file_set[1:]:
                print '[deleting] %s' % file_path
                os.remove(file_path)

        self._duplicate_file_list = []  # all duplicates are removed.

    def _calculate_sha1(self, file_path):
        """
        """
        # http://stackoverflow.com/a/19711609/1044366
        sha = hashlib.sha1()
        with open(file_path, 'rb') as f:
            while True:
                block = f.read(2 ** 10)  # one-megabyte blocks.
                if not block:
                    break
                sha.update(block)
        return sha.hexdigest()
