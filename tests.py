
from server import app
import unittest

class FlaskTests(unittest.TestCase):

    def setUp(self):
        """Set up by creating fake client."""

        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'

    def test_index(self):
        """Test for main search page."""

        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn("<h2>Please Write your Text</h2>", result.data)


if __name__ == '__main__':
    unittest.main()