#!/usr/bin/env python3
"""testing module for GithubOrgClient in client.py"""

from unittest import TestCase
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """class for testing GithubOrgClient class"""

    @parameterized.expand([
        ("googel", {"name": "google"}),
        ("abc", {"name": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org, res, mock_get_json):
        """test org method"""
        mock_get_json.return_value = Mock(return_value=res)
        github_client = GithubOrgClient(org)
        self.assertEqual(github_client.org(), res)
