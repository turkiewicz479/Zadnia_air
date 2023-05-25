#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import os

from files import write_to_file

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestFiles(unittest.TestCase):
    def test_write_to_file_when_file_does_not_exist(self):
        path = 'data.txt'
        try:
            os.remove(path)
        except FileNotFoundError:
            pass

        self.assertFalse(write_to_file(path))

    def test_write_to_file_when_file_exists(self):
        path = os.path.join(THIS_DIR, 'data.txt')
        with open(path, 'w'):
            pass

        returned_value = None
        ex = None
        try:
            returned_value = write_to_file(path)
        except Exception as _ex:
            ex = _ex
        os.remove(path)

        if ex:
            raise ex
        else:
            self.assertTrue(returned_value)


if __name__ == '__main__':
    unittest.main()
