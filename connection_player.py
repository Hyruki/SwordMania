import csv
import time
import os

def register():
    user = input("Enter votre nom d'utilisateur : ")
    if user == "":
        print("Vous n'avez rien rentrer comme nom réessayer")
        register()
    else:
        with open('Joueur.csv', 'a',newline='') as files:
            write = csv.writer(files)
            write.writerow([user])


def chargement():
    for i in range(3):
        print("""   ____   _                                                                _   
  / ___| | |__     __ _   _ __    __ _    ___   _ __ ___     ___   _ __   | |_ 
 | |     | '_ \   / _` | | '__|  / _` |  / _ \ | '_ ` _ \   / _ \ | '_ \  | __|
 | |___  | | | | | (_| | | |    | (_| | |  __/ | | | | | | |  __/ | | | | | |_ 
  \____| |_| |_|  \__,_| |_|     \__, |  \___| |_| |_| |_|  \___| |_| |_|  \__|
                                 |___/                                         """)
        time.sleep(1)
        os.system('cls')
        print("""   ____   _                                                                _       
  / ___| | |__     __ _   _ __    __ _    ___   _ __ ___     ___   _ __   | |_     
 | |     | '_ \   / _` | | '__|  / _` |  / _ \ | '_ ` _ \   / _ \ | '_ \  | __|    
 | |___  | | | | | (_| | | |    | (_| | |  __/ | | | | | | |  __/ | | | | | |_   _ 
  \____| |_| |_|  \__,_| |_|     \__, |  \___| |_| |_| |_|  \___| |_| |_|  \__| (_)
                                 |___/                                             """)
        time.sleep(1)
        os.system('cls')
        print("""   ____   _                                                                _           
  / ___| | |__     __ _   _ __    __ _    ___   _ __ ___     ___   _ __   | |_         
 | |     | '_ \   / _` | | '__|  / _` |  / _ \ | '_ ` _ \   / _ \ | '_ \  | __|        
 | |___  | | | | | (_| | | |    | (_| | |  __/ | | | | | | |  __/ | | | | | |_   _   _ 
  \____| |_| |_|  \__,_| |_|     \__, |  \___| |_| |_| |_|  \___| |_| |_|  \__| (_) (_)
                                 |___/                                                 """)
        time.sleep(1)
        os.system('cls')
        print("""   ____   _                                                                _               
  / ___| | |__     __ _   _ __    __ _    ___   _ __ ___     ___   _ __   | |_             
 | |     | '_ \   / _` | | '__|  / _` |  / _ \ | '_ ` _ \   / _ \ | '_ \  | __|            
 | |___  | | | | | (_| | | |    | (_| | |  __/ | | | | | | |  __/ | | | | | |_   _   _   _ 
  \____| |_| |_|  \__,_| |_|     \__, |  \___| |_| |_| |_|  \___| |_| |_|  \__| (_) (_) (_)
                                 |___/                                                     """)
        time.sleep(1)
        os.system('cls')

def main_connection():
    with open('Joueur.csv', 'r') as files:
        read = csv.DictReader(files, delimiter=',')
        for lines in read:
            if lines["Joueurs"] != " ":
                a = input("identifient : ")
                if a == lines["Joueurs"]:
                    print("fe")
                    b = input("Mot de passe : ")
                    if b == lines["Mdp"]: 
                        chargement()
            else:
                register()
