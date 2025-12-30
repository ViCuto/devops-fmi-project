"""
Module for testing the Flask application.
This module uses unittest to verify that the web server works correctly.
"""

import unittest
from app import app, GREETINGS


class TestApp(unittest.TestCase):
    """Test suite for the Flask app routes and logic."""

    def setUp(self):
        """Set up the test client before each test."""
        self.client = app.test_client()

    def test_connection(self):
        """Test if the home page returns status code 200 (OK)."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_valid_greeting(self):
        """Test if the response contains a valid greeting from the list."""
        response = self.client.get("/")
        data = response.data.decode()
        self.assertIn(data, GREETINGS)


if __name__ == "__main__":
    unittest.main()
