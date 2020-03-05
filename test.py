#!/usr/bin/env python
# coding: utf-8

import task2
from unittest import TestCase


class TestPrime(TestCase):
    def test_polindrome(self):
        """ Test that function returns proper values """
        self.assertFalse(task2.is_polindrome('assbv', 0))
        self.assertTrue(task2.is_polindrome('asddsa', 0))
        """Test that reaction to negative input is valid"""
        self.assertRaises(TypeError, task2.is_polindrome, 'assbv', -1)
