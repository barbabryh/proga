class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance
    
import unittest

class TestBankAccount(unittest.TestCase):

    def test_create_account_with_valid_balance(self):
        account = BankAccount("12345", 100.0)
        self.assertEqual(account.get_balance(), 100.0)
        print("test_create_account_with_valid_balance OK")

    def test_create_account_with_invalid_balance(self):
        with self.assertRaises(ValueError) as e:
            BankAccount("12345", -50.0)
        self.assertEqual(str(e.exception), "Initial balance cannot be negative")


    def test_successful_deposit(self):
        account = BankAccount("12345", 50.0)
        account.deposit(30.0)
        self.assertEqual(account.get_balance(), 80.0)


    def test_invalid_deposit(self):
        account = BankAccount("12345", 50.0)
        with self.assertRaises(ValueError) as e:
            account.deposit(0)
        self.assertEqual(str(e.exception), "Deposit amount must be greater than 0")


    def test_invalid_deposit_negative(self):
        account = BankAccount("12345", 50.0)
        with self.assertRaises(ValueError) as e:
            account.deposit(-20)
        self.assertEqual(str(e.exception), "Deposit amount must be greater than 0")


    def test_successful_withdrawal(self):
        account = BankAccount("12345", 100.0)
        account.withdraw(40.0)
        self.assertEqual(account.get_balance(), 60.0)


    def test_withdrawal_exceeds_balance(self):
        account = BankAccount("12345", 50.0)
        with self.assertRaises(ValueError) as e:
            account.withdraw(60.0)
        self.assertEqual(str(e.exception), "Insufficient funds")


    def test_invalid_withdrawal(self):
        account = BankAccount("12345", 50.0)
        with self.assertRaises(ValueError) as e:
            account.withdraw(0)
        self.assertEqual(str(e.exception), "Withdrawal amount must be greater than 0")


    def test_invalid_withdrawal_negative(self):
        account = BankAccount("12345", 50.0)
        with self.assertRaises(ValueError) as e:
            account.withdraw(-10)
        self.assertEqual(str(e.exception), "Withdrawal amount must be greater than 0")

    def test_balance_after_operations(self):
        account = BankAccount("12345", 100.0)
        account.deposit(50.0)
        account.withdraw(30.0)
        self.assertEqual(account.get_balance(), 120.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)