
import os
import csv
import psutil

def createuser(file):
    fichier = open(file,"r")
    users = open("/etc/passwd","r")
    group = open("/etc/group","r")

    reader = csv.DictReader(fichier, delimiter=":")
    cheikUser = False #le user n'existe pas
    cheikGroup = False #le group n'existe pas


    #j'ai ajouter des fonction de teste, on poura les remplacer par les foction de aicha
    #lire le contenu du fichier
    for texte in reader:
        for groups in group:
            #tester si le group existe dans la liste des
            if texte["nom_group"] in groups:
                cheikGroup = True
                break

         #si le group n'existe pas, on le cree       
        if not cheikGroup:
                os.system("sudo groupadd "+ texte["nom_group"])
        
        for user in users:
            #tester si le user existe
            if texte["nom_user"] in user:
                cheikUser = True
                break

        #si le user n'existe pas, on le cree
        if not cheikUser:   
                os.system("sudo useradd -N "+ texte["nom_user"])

        #on deplace le user dans son group
        os.system("sudo usermod -g "+ texte["nom_group"]+" "+ texte["nom_user"])

    fichier.close()
    users.close()
    group.close()






