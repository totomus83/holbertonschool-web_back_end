#!/usr/bin/env python3
"""Unit tests for client.GithubOrgClient"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns expected value"""
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {"login": org_name})


    def test_public_repos_url(self):
        """Test that _public_repos_url returns correct URL from mocked org"""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")

        with patch.object(
            GithubOrgClient, "org", new_callable=unittest.mock.PropertyMock
        ) as mock_org:
            mock_org.return_value = payload
            result = client._public_repos_url

        self.assertEqual(result, "https://api.github.com/orgs/google/repos")
