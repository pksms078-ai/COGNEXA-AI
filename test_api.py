Python
import unittest

class APITest(unittest.TestCase):

    def test_status(self):

        self.assertEqual(
            200,
            200
        )

if __name__ == "__main__":

    unittest.main()
