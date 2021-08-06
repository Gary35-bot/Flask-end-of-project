import unittest
from app import app

# testing my api to see if it work


class TestingMyApi(unittest.TestCase):

    # email testing and it works

    def email_sender(self):
        test = app.test_client(self)
        response = test.get('/send-email')
        status = response.status_code
        self.assertEqual(status, 404)


if __name__ == "__main__":
    unittest.main()
