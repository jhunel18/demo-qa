import unittest
from atm import ATM
from data import users


class TestATM(unittest.TestCase):
    def setUp(self):
        self.atm = ATM(users.copy())  # fresh copy for each test

    def test_login_success(self):
        self.assertTrue(self.atm.login("123456", "1234"))

    def test_login_fail(self):
        self.assertFalse(self.atm.login("123456", "0000"))

    def test_deposit(self):
        self.atm.login("123456", "1234")
        self.atm.deposit(100)
        self.assertEqual(self.atm.get_balance(), 600)

    def test_withdraw_success(self):
        self.atm.login("123456", "1234")
        result = self.atm.withdraw(200)
        self.assertTrue(result)
        self.assertEqual(self.atm.get_balance(), 400)

    def test_withdraw_fail(self):
        self.atm.login("123456", "1234")
        result = self.atm.withdraw(1000)
        self.assertFalse(result)
        self.assertEqual(self.atm.get_balance(), 600)


if __name__ == "__main__":
    unittest.main()
