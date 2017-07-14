import sys

true_login = "1"
true_password = "1"

def CheckLogin(login, password):
    #print(login, ' ', password)
    if login == true_login and password == true_password:
        print("Yeay! Go ahead! ")
        return 1
    else:
        Exit()
        print("\nPlease enter correct login and password \n")
def Exit():
    print("\n Exiting the script...")
    sys.exit()
