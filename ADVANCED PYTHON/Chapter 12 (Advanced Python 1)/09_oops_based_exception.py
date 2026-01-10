"""
=================================================
OOP-BASED REAL-WORLD EXCEPTION HANDLING EXAMPLE
=================================================

Scenario:
A simple Bank Account system where:
- Balance cannot go negative
- Withdrawal beyond balance is forbidden
- Invalid input must be handled cleanly
"""

# -------------------------------
# Custom Exceptions (Business Rules)
# -------------------------------

class InsufficientBalanceError(Exception):
    """Raised when withdrawal amount exceeds balance"""
    pass


class InvalidAmountError(Exception):
    """Raised when amount is zero or negative"""
    pass


# -------------------------------
# BankAccount Class (OOP Design)
# -------------------------------

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount: float):
        # Validate amount
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")

        # Business rule check
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance.")

        self.balance -= amount
        return self.balance


# -------------------------------
# Application Layer (Exception Handling)
# -------------------------------

try:
    account = BankAccount("Shivu", 5000)

    amount = float(input("Enter amount to withdraw: "))
    remaining_balance = account.withdraw(amount)

    print(f"Withdrawal successful. Remaining balance: {remaining_balance}")

except ValueError:
    # Raised by float() conversion
    print("ValueError: Please enter a numeric amount.")

except InvalidAmountError as e:
    print("InvalidAmountError:", e)

except InsufficientBalanceError as e:
    print("InsufficientBalanceError:", e)

finally:
    print("Transaction attempt completed.")
