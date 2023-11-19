#!/usr/bin/python3
"""Defines unittests for models/user.py."""
from models.user import User
import unittest

class TestUser(unittest.TestCase):
    """Test user model"""
    def test_val(self):
        """Test User values."""
        inst = User(
            email = "madrid@gmail.com",
            password = "halamadrid",
            first_name = "jay",
            second_name = "cetler",
        )
        self.assertEqual(inst.email, "madrid@gmail.com")
        self.assertEqual(inst.password, "halamadrid")
        self.assertEqual(inst.first_name, "jay")
        self.assertEqual(inst.last_name, "cetler")
    
    def test_type(self):
        """Test types of attr"""
        inst = User()
        self.assertIsInstance(inst.email, str)
        self.assertIsInstance(inst.password, str)
        self.assertIsInstance(inst.first_name, str)
        self.assertIsInstance(inst.last_name, str)

if __name__ == "__main__":
    unittest.main()