Python
import unittest

class DecisionTest(unittest.TestCase):

    def test_decision(self):

        decision = "approved"

        self.assertEqual(
            decision,
            "approved"
        )

if __name__ == "__main__":

    unittest.main()
