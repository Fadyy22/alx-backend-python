#!/usr/bin/env python3
"""module for testing access_nested_map function"""

from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """class for testing access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
