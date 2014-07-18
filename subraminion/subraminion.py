# -*- coding: utf-8 -*-
# Copyright (c) 2014 Sandeep Raju. See LICENSE.txt for details.
import os
import re
import hashlib
from collections import defaultdict


class Subraminion(object):

    """
    """

    def __init__(self, base_path, pattern=None):
        """
        """
        self._sha1_file_map = defaultdict(list)
        self._duplicate_file_list = []
        self._base_path = base_path
        self._pattern = pattern

    def process_files(self, verbose=False):
        """
        """
        # http://stackoverflow.com/a/16974952/1044366
        for root, dirs, files in os.walk(self._base_path):
            for f in files:
                file_path = os.path.join(root, f)
                if verbose:
                    print '[processing] %s' % file_path
                file_sha1 = self._calculate_sha1(file_path)
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
