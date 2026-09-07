data ={
    123456:{'name':"Sakhi",'pin':1234,'balance':5000,'history':[]},
    246810:{'name':"Tarun",'pin':1234,'balance':6520,'history':[]},
    235791:{'name':"Lucky",'pin':1234,'balance':7070,'history':[]}

}
def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]['pin']==pin:
        print("Login Successfully")
        return True
    else:
        print("Invalid Login") 

def menu():
    print(f"Welcome to the ATM,{data[acc_num]['name']}")
    print('[c]heck Balance')
    print('[D]eposit')
    print('[w]ithdraw')
    print('[V]iew transaction')
    print('[E]xit')

def checkbalance():
    print(f'Hello {data[acc_num]["name"]},')
    print("Current Balance:",data[acc_num]["balance"],end="\n\n")

def deposit():
    amount = int(input("Enter the amount of deposit: "))
    data[acc_num]["balance"]+=amount
    data[acc_num]["history"].append(f"{amount} is depositeed")
    print(f"{amount} is deposited successfully")
    checkbalance()

def withdraw():
    amount = int(input("Enter the amount  to withdraw: "))
    if data[acc_num]["balance"]>=amount:
       data[acc_num]["balance"]-=amount
       data[acc_num]["history"].append(f"{amount}is withdraw")
       print(f"{amount} is withdraw successfully")
       checkbalance()
    else:
        print("Insufficient Funds")

def viewtransaction():
    if data[acc_num]["history"]:
        print(">>>>>>>>>>> Transaction History <<<<<<<<<<")
        for i in data[acc_num]["history"]:
            print(i)
        else:
            print(">>>>>>>>>>> End of the History <<<<<<<<<<")
    else:
        print("No Transaction History")