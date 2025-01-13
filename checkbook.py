#!/usr/bin/python3
class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit a specified amount into the checkbook."""
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraw a specified amount from the checkbook if funds are sufficient."""
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display the current balance in the checkbook."""
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """
    Prompt the user to enter a valid amount.
    
    Parameters:
    - prompt (str): The message to display when asking for input.
    
    Returns:
    - float: A valid, non-negative amount entered by the user.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount must be a positive number. Please try again.")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """Main function to interact with the checkbook."""
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            print("Goodbye!")
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
