db = {}
def addUserToDB(name,passw):
    db[name] = {"PSWD":passw,"BLNC": 0}
    return

def optionMenu(userName):
    print("\033[H\033[J", end="")  
    option = input("Enter option : \n (w)ithdraw\n (d)eposit\n (s)how balance\n (e)xit\n enter option : ")
    match option:
        case "s" : 
            print(db[userName]["BLNC"])
            input("enter any key to continue ... ")
            optionMenu(userName)
        case "w" : 
            flag = True
            while flag:
                withdrawAmount = int(input("Enter amount to withdraw : "))
                if withdrawAmount <=  db[userName]["BLNC"] :
                    db[userName]["BLNC"] = db[userName]["BLNC"] - withdrawAmount
                    print("withdraw successfull, amount withdrawed : ",withdrawAmount)
                    print("available balance is : ", db[userName]["BLNC"] )
                    flag = False
                    #time 3s
                    input("enter any key to continue ...")
                    optionMenu(userName)
                else:
                    print("insufficient balance ...") 
                    optionMenu(userName)

        case "d" :
            depositAmount = int(input("Enter amount to deposit : "))
            db[userName]["BLNC"] = db[userName]["BLNC"] + depositAmount 
            print("Deposit successful ...")
            print("available balance is : ", db[userName]["BLNC"] )
            input("Enter any key to continue ....")
            optionMenu(userName)
        case "e" : main()
        case _ : 
            print("invalid input")
            optionMenu(userName)


def passchecker(userName, password) :
    if userName in db:
        if db[userName]["PSWD"] == password :
            return True
        else:
            return False
    else:
        print("not registered...")
        main()
def main():

    print("\033[H\033[J", end="")
    registerState = input("Are you a registered user (y)es , (n)o : ").lower()
    if registerState == "n" :
        Newusername = input("Enter new user name : ").lower()
        Newpass = input("Enter new password : ")
        if Newusername in db:
            print("username already exist, press any key to continue ...")
            input()
            main()
        addUserToDB(Newusername,Newpass)
        print("user registerd successfully, press any key to continue ...")
        input()
        main()    

    elif registerState == "y" :
        pscheckFlag = False
        while pscheckFlag == False:
            userName = input("Enter username : ")        
            password = input("Enter password : ")
            pscheckFlag = passchecker(userName,password)
            if pscheckFlag == True:
                break
        optionMenu(userName)
    else:
        print("invalid input, press any key to continue...")
        input()
        main()

main()

