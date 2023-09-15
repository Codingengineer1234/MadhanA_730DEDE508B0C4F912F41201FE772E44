class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print(f"Deposited {amount} units. New balance: {self.__account_balance}")
    else:
      print("Deposit amount must be greater than zero.")

  def withdraw(self, amount):
    if 0 < amount <= self.__account_balance:
      self.__account_balance -= amount
      print(f"Withdrew {amount} units. New balance: {self.__account_balance}")
    else:
      print(
          "Withdrawal amount must be greater than zero and less than or equal to the account balance."
      )
  def display_balance(self):
    print(f"Account Holder: {self.__account_holder_name}")
    print(f"Account Number: {self.__account_number}")
    print(f"Account Balance: {self.__account_balance}")
if __name__ == "__main__":
  name=input('Enter the Account holder Name:\t')
  acno=input('Enter the Account Number:\t')
  bal=float(input('Enter the current balance:\t'))
  dep=float(input('Enter the amount to be deposited:\t'))
  account = BankAccount(acno, name, bal)
  account.display_balance()
  account.deposit(dep)
  account.display_balance()
  wid=float(input('Enter the amount to be withdraw=\t'))
  account.withdraw(wid)
  account.display_balance()
