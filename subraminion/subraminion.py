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

    def process_files(self, verbose=False):
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

    def get_duplicate_file_list(self):
        """
        """
        return self._duplicate_file_list

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
