from random import random
import datetime
# Welcame to Login System Version 4.0 .
with open("serectxpathlogqual.tid") as IDpath:
    log_ID = str(IDpath.readline())

with open("serectxpathlogpassqual.tid") as PASSpath:
    log_PASS = str(PASSpath.readline())

# creating a login log which represent the log of l time and date.
with open("login_log.txt") as log:
    login_log1 = str(log.readline())

# we are create login system in python by simple Logic.
print("Welcame to Login System Version 4.0\n")
print("© Copyright 2020 Ti Corporation.\n")
# we put User Inputs in Varibles.
print("If you want to exit this program plase press Q\n")

ID_system = input("Please Enter Your ID.\n")
print("\n")
while ID_system != log_ID:
    if ID_system == "q":
        break
    print("Acess Not Allowed\n")
    ID_system = input("Please Enter Your ID.\n")
    print("\n")
# here serect work in script
if (log_ID == ID_system):
    PASS_system = input("Please Enter Your PASSWORD.\n")
    print("\n")
    while PASS_system != log_PASS:
        if PASS_system == "q":
            break
        print("Acess Not Allowed\n")
        PASS_system = input("Please Enter Your PASSWORD.\n")
        print("\n")
    if (log_PASS == PASS_system):
        print("Acess Allowed\n")
        print(login_log1)
        with open("login_log.txt", "w") as op:
            op.write(str(datetime.datetime.now()))
        print("*******************************************\n")
        print("If you want to change the ID and Password. Please press C \n")
        print("*******************************************\n")
        change = input()
        # we take input form user to change the ID or Password
        if change == "c":
            value = input("Enter New ID -> ")
            with open("serectxpathlogqual.tid", "w") as op:
                op.write(value)
            print("Your ID is changed Successfully !")
            # AGP is a Varible that store the user input Yes or No
            AGP = input("You Want to Genrate Password Automatic (y/n)")
            while AGP != "y" or "n":
                if AGP == "y":
                    value = random()
                    print(f"This Your Password -> {value}")
                    with open("serectxpathlogpassqual.tid", "w") as op:
                        op.write(str(value))
                    print("Your Password is changed Successfully !")
                    break
                elif AGP == "n":
                    value = input("Enter New Password -> ")
                    with open("serectxpathlogpassqual.tid", "w") as op:
                        op.write(str(value))
                    print("Your Password is changed Successfully !")
                    break
                else:
                    if AGP != "y" or "n":
                        print("You enter invaild input please try again.\n")
                        AGP = input(
                            "You Want to Genrate Password Automatic (y/n)")
