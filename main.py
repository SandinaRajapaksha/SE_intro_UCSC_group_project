#user class
class UserClass:
    name : "default" # type: ignore
    password : 1234
    balance : 0




def alreadyRegisteredMenu():
    option = input("Are you a registes user : (y)yes , (n)o , (e)exit")
    match option:
        case "y" : passcheck()
        case "n" : registerUser()
        case _ : alreadyRegisteredMenu()

def passcheck():
    userName = input("enter user name : ")
    password = input("enter password : ")

