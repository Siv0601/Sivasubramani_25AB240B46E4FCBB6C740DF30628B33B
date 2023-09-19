class BankAccount:
  def initial(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self,amount):
    if amount>0:
      self.__account_balance += amount
      print("Deposited Rs.{}. Now balance: Rs.{} ".format(amount,self.__account_balance))
    else:  
      print("Invalid deposit")

  def withdraw(self,amount):
    if amount>0 and amount<=self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw Rs.{}. Now balance: Rs.{} ".format(amount,self.__account_balance))
    else: 
       print("Invalid withdraw or amoint insufficient")

  def display(self):
    print("Account Holder:{}. Account Number:{}. Account Balance:{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))


account = BankAccount()

account.initial(account_number="6379697038",account_holder_name="Murugesh",initial_balance=6000.0)
account.display()
account.deposit(2000)
account.withdraw(1000)
account.display()