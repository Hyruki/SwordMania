import re


def register():
    user = input("Enter votre nom d'utilisateur : ")
    if user == "":
        print("Vous n'avez rien rentrer comme nom réessayer")
        register()
    else:
        with open('DataUser.txt', 'w+') as files:
            files.write(user + "\n")


def connection():
    print("eds")


with open('DataUser.txt', 'r+') as files:
    r = files.readlines(1)
    for read in r:
        if read != None:
            connection()
        else:
            print("dzq")