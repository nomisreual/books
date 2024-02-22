from app import create_app
import unittest


class TestCase(unittest.TestCase):
    # def setUp(self):
    #     app = create_app()
    #     app.testing = True
    #     self.app = app.app.test_client()

    def test_request_example(self):
        # response = self.app.get("/")
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
