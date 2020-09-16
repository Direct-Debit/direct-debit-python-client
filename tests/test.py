import unittest
from datetime import timedelta

from direct_debit import DirectDebitClient


class TestSend(unittest.TestCase):
    def test_example(self):
        client = DirectDebitClient(False, "TTTT", "")
        print(client.whoami().email)


if __name__ == "__main__":
    unittest.main()
