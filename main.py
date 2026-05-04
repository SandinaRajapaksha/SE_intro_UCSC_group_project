#user class
class UserClass:
    name : "default" # type: ignore
    passwordUsr : 1234
    balance : 0

listOfusers = []


def alreadyRegisteredMenu():
    option = input("Are you a registes user : (y)yes , (n)o , (e)exit")
    match option:
        case "y" : passcheck()
        case "n" : registerUser()
        case _ : alreadyRegisteredMenu()

def passcheck():
    userName = input("enter user name : ")
    password = input("enter password : ")
    for i in listOfusers:
        if userName == i:
            break
        else :
            passcheck()
    
    if password == userName.passwordUsr:
        optionselect()
    else:
        print("incorrect password, enter any key to contiue")
        input()
        alreadyRegisteredMenu()

def registerUser():
    newUsername = input("enter new username")
    newPassword = input("enter new password")
    userobject = UserClass(newUsername,newPassword)
    license.append(userobject)
    print("successfully registered, enter any key to continue")
    input()
    alreadyRegisteredMenu()

def optionselect():
    print("select option : ")
    print("(d)eposit money\n(w)ithdraw money\n(c)heck balance\n(e)xit")
    option = input()
    match option:
        case "d" : deposit()
        case "w" : withdraw()
        case "c" : checkBalance()
        case _ : alreadyRegisteredMenu() 
    
