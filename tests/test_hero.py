#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the Hero class.

This module provides unit tests for the Hero class.

A package for champion (ghahreman) from master (ostad).
"""

import unittest
from ghahreman import Hero


class TestHero(unittest.TestCase):
    """
    Test class for the Hero class.
    """

    def test_init_default_parameters(self):
        """
        Test initialization with default parameters.
        """
        hero = Hero()
        self.assertEqual(hero.height1, 1.0)
        self.assertEqual(hero.radius1, 0.5)
        self.assertEqual(hero.height2, 1.0 / 3.0)
        self.assertEqual(hero.radius2, 0.5 * 0.8)
        self.assertEqual(hero.resolution, 30)

    def test_init_custom_parameters(self):
        """
        Test initialization with custom parameters.
        """
        hero = Hero(height1=2.0, radius1=1.0, resolution=60)
        self.assertEqual(hero.height1, 2.0)
        self.assertEqual(hero.radius1, 1.0)
        self.assertEqual(hero.height2, 2.0 / 3.0)
        self.assertEqual(hero.radius2, 1.0 * 0.8)
        self.assertEqual(hero.resolution, 60)

    def test_create_cones(self):
        """
        Test creation of cones and other elements.
        """
        hero = Hero()
        self.assertIsNotNone(hero.cone1)
        self.assertIsNotNone(hero.cone2)
        self.assertIsNotNone(hero.disk)
        self.assertIsNotNone(hero.bottom_disk)
        self.assertIsNotNone(hero.cube)
        self.assertIsNotNone(hero.sphere)
        self.assertIsNotNone(hero.upper_sphere)
        self.assertIsNotNone(hero.handle1)
        self.assertIsNotNone(hero.handle2)


if __name__ == '__main__':
    unittest.main()
