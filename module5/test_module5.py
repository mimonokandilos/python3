import unittest
from web_development import create_static_website
import os

class TestWebDevelopment(unittest.TestCase):
    def test_create_static_website(self):
        result = create_static_website()
        self.assertEqual(result, "Static website created successfully.")

        # Verify that the file was created
        self.assertTrue(os.path.exists("index.html"))

        # Verify the content of the file
        with open("index.html", "r") as file:
            content = file.read()
            self.assertIn("<title>My Static Website</title>", content)
            self.assertIn("<h1>Hello, World!</h1>", content)
            self.assertIn("<p>This is a simple static website.</p>", content)

if __name__ == "__main__":
    unittest.main()

