import json
class File:
    def __init__(self,file_link: str):
        self.file_link = file_link
        try:
            self.read_file()
        except:
            #si read_file renvoie une erreur cela nous indique que le fichier est vide donc on ecrit
            #des données de base
            self.write_file({"SSID": "VIDE","PASSWORD": "VIDE", "URL": "VIDE"})
    def write_file(self,data):
        """
        data est un objet
        la fonction ecrit dans le fichier
        """
        with open(self.file_link, "w") as f:
            json.dump(data, f)
        #il est important de fermer le fichier apres l'avoir ouvert pour liberer la memoire
        f.close()
    def read_file(self):
        """
        lis le fichier et renvoie les informations sous forme d'objet
        """
        # ouvrir le fichier JSON
        with open(self.file_link, "r") as f:
            # charger le contenu du fichier JSON dans un objet Python
             data = json.load(f)
        f.close()
        return data
