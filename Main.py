import csv
def register():
    user = input("Enter votre nom d'utilisateur : ")
    if user == "":
        print("Vous n'avez rien rentrer comme nom réessayer")
        register()
    else:
        with open('Joueur.csv', 'a',newline='') as files:
            write = csv.writer(files)
            write.writerow([user])


def connection():
    print("eds")

with open('Joueur.csv', 'r') as files:
    read = csv.DictReader(files, delimiter=',')
    for lines in read:
        if lines["Joueurs"] != " ":
            connection()
        else:
            register()
