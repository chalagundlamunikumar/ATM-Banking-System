from report import export_to_pdf

class Bankaccount:
   def __init__(self,holdername,account_number,balance,pin):
      self.holdername=holdername
      self.account_number = account_number
      self.balance=balance
      self.pin=pin
      self.transactions=[]
      self.min_balance=10000
      
   def deposit(self,amount):
      self.balance+=amount
      print("Amount deposited:",amount)
      self.transactions.append(f"Deposited: {amount}")
      
   def withdraw(self,amount):
      if self.balance-amount>=self.min_balance:
         self.balance-=amount
         print("Amount withdrawn:",amount)
         self.transactions.append(f"withdraw: {amount}")
      else:
         print("Insufficient balance")
         self.transactions.append(f"Failed withdraw attempt: {amount}")
      
   def transfer(self,amount,other_account):
      if self.balance-amount>=self.min_balance:
         self.balance-=amount
         other_account.balance+=amount
         print("Amount transferred:",amount)
         self.transactions.append(f"Transferred: {amount} to {other_account.holdername}")
      else:
         print("Insufficient balance")
         self.transactions.append(f"Failed transfer attempt: {amount} to {other_account.holdername}")
         
   def display(self):
      print("Account holder:",self.holdername)
      print("Account balance:",self.balance)
   def show_history(self):
      print(f"\nTransaction history for{self.holdername}:")
      if not self.transactions:
         print("No transactions yet.")     
      else:
         for t in self.transactions:
            print("-",t)
         print("welcome to create your bank account")
         
Holdername = input("Enter account holder name:")
account_number = input("Enter account number:")
balance = int(input("Enter initial balance:")) 
pin = int(input("Set your account pin:"))    
acc1=Bankaccount(Holdername,account_number,balance,pin)
print("\nCreate another account to transfer money")
holdername =input("Enter account holder name:")
account_number =input("Enter account number:")
balance =int(input("Enter initial balance:")) 
pin =int(input("Set your account pin:"))    
acc2=Bankaccount(holdername,account_number,balance,pin)

attempts=5
while attempts>0:
   entered_pin=int(input(f"\nEnter pin for {acc1.holdername}"))
   if acc1.pin == entered_pin:
      print("Pin verified successfully")
      break
   else:
      attempts-=1
      print(f"Incorrect pin.Try again!{attempts} attempts left")
else:
   print("Too many incorrect attempts.Exiting...")
   exit()
while True:
   print("\n...Menu...")
   print("1.deposit")
   print("2.withdraw")
   print("3.transfer")
   print("4.checkbalance")
   print("5.show history")
   print("6. Export transaction history to PDF")
   print("7.exit")
   
   try:
      choice = int(input("Enter your choice: "))
   except ValueError:
      print("❌ Please enter a valid number only!")
      continue

   if choice==1:
      amount=int(input("Enter amount to deposit:"))
      acc1.deposit(amount)
      
   elif choice==2:
      amount=int(input("Enter amount to withdraw:"))
      acc1.withdraw(amount)
      
   elif choice==3:
      amount=int(input("Enter amount to transfer:"))
      acc1.transfer(amount,acc2)
      
   elif choice==4:
      acc1.display()
   elif choice==5:
      acc1.show_history()
   elif choice == 6:
   
    export_to_pdf(
      acc1.holdername,
      acc1.account_number,
      acc1.balance,
      acc1.transactions
)


   elif choice==7:
      print("ATM !session ended")
      break
   else:
      print("Invalid choice")
   