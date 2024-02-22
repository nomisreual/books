from app import create_app
import unittest


class TestCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.testing = True
        self.app = app.test_client()

    def test_request_example(self):
        response = self.app.get("/")
        self.assertIn(b"<body class=container>", response.data)
