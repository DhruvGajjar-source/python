import random
user_data={}
transactions = []
balance = 0
class Atm:

    def change_pin(self):
        try:
            contact = int(input("Enter your valid 10 digit contact number : "))
            pin = int(input("Enter your 4 digit pin : "))
            if contact==user_data['contact'] and pin==user_data['pin']:
                otp = random.randint(1000,9999)
                print("******Your OTP is :",otp,"********")
                uotp = int(input("Enter a OTP sent to your contact number : "))
                if uotp==otp:
                    print("Otp verification succesfully completed!!")
                    npin=int(input("Enter your new 4-digit pin : "))
                    user_data['pin'] = npin 
                    print("Pin changed succesfully!!")
                else:
                    print("Invalid OTP!!")
            else:
                print("Enter valid contact number and pin.")
        except ValueError as e:
            print("Enter a number only")

    def deposit(self):
        try:
            global balance
            contact = int(input("Enter your valid 10 digit contact number : "))
            pin = int(input("Enter your 4 digit pin : "))
            if contact==user_data['contact'] and pin==user_data['pin']:
                print("Your current balance is : ",balance)
                amount = int(input("Enter amount to deposit : "))
                balance = balance + amount
                transactions.append(f"deposit of : {amount}")
                print("After deposit current balance is :",balance)
            else:
                print("Enter valid contact and pin!!")
        except ValueError as e:
            print("Enter input in number only.")

    def withdraw(self):
        try:
            global balance
            contact = int(input("Enter your valid 10 digit contact number : "))
            pin = int(input("Enter your 4 digit pin : "))
            if contact==user_data['contact'] and pin==user_data['pin']:
                print("Your current balance is :",balance)
                print("""  
                            withdraw charges:
                            ₹0 for <= ₹1000
                            ₹100 for <= ₹20000
                            ₹1000 for <= ₹100000
                            ₹2000 for > ₹100000
        """)
                amount = int(input("Enter a amount withdraw : "))  
                if amount>0 and amount<=1000:
                    balance = balance - amount
                    transactions.append(f"withdraw of : {amount}")
                    print("Withdraw succesful!!")
                    print("Current balance is : ",balance)
                elif amount>1000 and amount<=20000 and amount + 100 < balance:
                    balance = balance - (amount + 100)
                    transactions.append(f"withdraw of : {amount}")
                    print("Withdraw succesful!!")
                    print("Current balance is : ",balance)
                elif amount>20000 and amount<=100000 and amount + 1000 < balance:
                    balance = balance - (amount + 1000) 
                    transactions.append(f"withdraw of : {amount}")
                    print("Withdraw succesful!!")
                    print("Current balance is : ",balance)
                elif amount>100000 and amount<=1000000 and amount + 2000 < balance:
                    balance = balance - (amount + 2000)
                    transactions.append(f"withdraw of : {amount}")
                    print("Withdraw succesful!!")
                    print("Current balance is : ",balance)
                else:
                    print("Insufficient balance!!")
        except ValueError:
            print("Enter amount in number only!!")

    def balance(self):
        contact = int(input("Enter your valid 10 digit contact number : "))
        pin = int(input("Enter your 4 digit pin : "))
        if contact==user_data['contact'] and pin==user_data['pin']:
            print("Your current balance is : ",balance)
        else:
            print("Enter valid contact and pin!!")

    def transactions(self):
        contact = int(input("Enter your valid 10 digit contact number : "))
        pin = int(input("Enter your 4 digit pin : "))
        if contact==user_data['contact'] and pin==user_data['pin']:
            print("Your previous transactions are listed below. ")
            for i in transactions[-10:]:
                print(i)

obj = Atm()
try:
    print("*****Welcome ATM Sign-up Process*****")
    name = input("Enter your name : ")
    contact = int(input("Enter your valid 10 digit mobile number :"))
    pin = int(input("Enter your 4-digit pin : "))
    rpin = int(input("Re-enter your pin : "))
    deposit = int(input("Enter amount more than 1000 for first diposit : "))

    if len(str(contact))==10 and len(str(pin))==4 and deposit>1000:
        if pin==rpin:
            user_data['name']=name
            user_data['contact']=contact
            user_data['pin']=pin
            balance = balance + deposit
            transactions.append(f"deposit of : {deposit}")
            print("Sign-up succesful!!")
except:
    print("Enter valid input!!")

while True:

    menu = """
                Press 1 for Change pin
                Press 2 for Deposite money
                Press 3 for withdraw money
                Press 4 for Check blance
                Press 5 for Last 10 Transactions
                Press 6 for Exit ATM
    """
    try:
        print(menu)
        choice = int(input("Enter your choice : "))

        if choice==1:
            obj.change_pin()
        elif choice==2:
            obj.deposit()
        elif choice==3:
            obj.withdraw()
        elif choice==4:
            obj.balance()
        elif choice==5:
            obj.transactions()
        elif choice==6:
            print("Thankyou for using ATM")
            break
    except:
        print("Enter valid choice between 1 to 6.")
