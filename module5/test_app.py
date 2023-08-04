# test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to My Simple Website', response.data)
        self.assertIn(b'This is a simple static website created using HTML and CSS.', response.data)

if __name__ == '__main__':
    unittest.main()
