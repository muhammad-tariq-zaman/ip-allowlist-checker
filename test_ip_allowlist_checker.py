import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import load_allowlist, allowed


class TestAllowlist(unittest.TestCase):
    def test_inside_range_allowed(self):
        nets = load_allowlist("10.0.0.0/8\n# comment\n")
        self.assertTrue(allowed(nets, "10.1.2.3"))

    def test_outside_range_denied(self):
        nets = load_allowlist("10.0.0.0/8\n")
        self.assertFalse(allowed(nets, "192.168.1.1"))

    def test_v4_not_matched_by_v6_range(self):
        nets = load_allowlist("2001:db8::/32\n")
        self.assertFalse(allowed(nets, "10.0.0.1"))
