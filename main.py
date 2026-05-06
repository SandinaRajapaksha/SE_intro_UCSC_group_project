db = {}
def addUserToDB(name,passw):
    db[name] = {"PSWD":passw,"BLNC": 0}
    print(db)

def optionMenu(userName):
    option = input("enter option :")
    match option:
        case "s" : 
            print(db[userName]["BLNC"])
            input("enter any key : ")
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
        
        case "d" :
            depositAmount = int(input("Enter amount to deposit : "))
            db[userName]["BLNC"] = db[userName]["BLNC"] + depositAmount 
            print("Deposit successful ...")
            print("available balance is : ", db[userName]["BLNC"] )
            input("Enter any key to continue ....")
            optionMenu(userName)
        case _ : main()

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
    registerState = input("Are you a registered user (y)es , (n)o : ")
    if registerState == "n" :
        Newusername = input("Enter new user name : ")
        Newpass = input("Enter new password : ")
        addUserToDB(Newusername,Newpass)
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

main()

