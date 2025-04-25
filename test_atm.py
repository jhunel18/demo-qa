import unittest
from atm import ATM
from data import users  # assuming users contains the sample data
import copy


class TestATM(unittest.TestCase):

    def setUp(self):
        # Create a deep copy of the users data to ensure tests don't interfere with each other
        self.atm = ATM(copy.deepcopy(users))  

    def test_login_success(self):
        # Test successful login
        self.assertTrue(self.atm.login("123456", "1234"))

    def test_login_fail(self):
        # Test failed login (wrong pin)
        self.assertFalse(self.atm.login("123456", "0000"))

    def test_deposit(self):
        # Test depositing money into the ATM
        self.atm.login("123456", "1234")
        self.atm.deposit(100)  # Deposit 100 into the account
        self.assertEqual(self.atm.get_balance(), 600)  # Assert the balance is 600

    def test_withdraw_success(self):
        # Test successful withdrawal
        self.atm.login("123456", "1234")
        result = self.atm.withdraw(200)  # Try to withdraw 200
        self.assertTrue(result)  # Assert withdrawal was successful
        self.assertEqual(self.atm.get_balance(), 300)  # Assert the new balance is 300

    def test_withdraw_fail(self):
        # Test failed withdrawal due to insufficient funds
        self.atm.login("123456", "1234")
        result = self.atm.withdraw(1000)  # Try to withdraw 1000, which exceeds the balance
        self.assertFalse(result)  # Assert withdrawal failed
        self.assertEqual(self.atm.get_balance(), 500)  # Assert the balance is still 500


if __name__ == "__main__":
    unittest.main()
