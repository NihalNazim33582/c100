class ATM:
    def __init__(self,atmCard,pinNumber):
        self.atmCard    =   atmCard
        self.pinNumber  =   pinNumber  
        
    def balance(self):     
        print("Your balance is $9,999,999,999,999")
        
    def bankEnquiry(self,amount):
        new_amount = 9999999999999 - amount
        print("You have withdrawn "+str(amount) +". Your remaining balance is "+ str(new_amount))

def main():
        
    card_no =   input("Insert your card number here :  ")
    pin_no  =   input("Insert your pin number here(Dont't worry its perfectly safe):  ")

    new_user =  ATM(card_no,pin_no)

    print("Which activity do you want to do?  : ")
    print("1.Balance   2.Withdrawl")
    activity = int(input("Enter the number of your activity (Enter the Number): "))
        
    if (activity == 1):
        new_user.balance()
        
    elif (activity == 2):
        amount = int(input("Enter the amount you would like to withdraw (Only Numbers): -"))
        new_user.bankEnquiry(amount)
        
    else:
        print("Please enter a valid number.(A number with in your balance.)")
        
if __name__ == "__main__":
    main()