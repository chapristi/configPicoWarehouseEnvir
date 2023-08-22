from File import File
class Configuration:
    def __init__(self):
        self.file = File("data.json")
        file_data = self.file.read_file()
        self.ssid = file_data["SSID"]
        self.password = file_data["PASSWORD"]
        self.url = file_data["URL"]
    def get_ssid(self):
      """
        retourne la valeur du SSID
      """
      return self.ssid
    def get_password(self):
      """
        retourne la valeur du mot de passe
      """
      return self.password
    def get_url (self):
      """
        retourne la valeur de l'url
      """
      return self.url
 
    def set_ssid(self, ssid):
        """
          permet de definir la valeur du SSID
        """
        if ssid != "":
            self.ssid = ssid
            print(f"Le SSID a bien été modifié par ({self.ssid})\n")
        else:
            print(f"Le SSID reste inchangé ({self.ssid})\n")
 
    def set_password(self, password):
        """
          permet de definir la valeur du mot de passe
        """
        if password != "":
            self.password = password
            print("Le mot de passe est bien enregistré\n")
        else:
            print(f"Le mot de passe reste inchangé ({self.password})\n")


    def set_url(self, url):
        """
          permet de definir la valeur du mot de l'url
        """
        if url != "":
            self.url = url
            print(f"L'URL du serveur a été modifiée par ({self.url})\n")
        else:
            print(f"L'URL du serveur n'a pas été modifié ({self.url})\n")

 
    def display_starting_menu(self):
        ascii_art = """
 
                  YAao,
                    Y8888b,
                  ,oA8888888b,
            ,aaad8888888888888888bo,
         ,d888888888888888888888888888b,
       ,888888888888888888888888888888888b,
      d8888888888888888888888888888888888888,
     d888888888888888888888888888888888888888b
    d888888P'                    `Y888888888888,
    88888P'                    Ybaaaa8888888888l
   a8888'                      `Y8888P' `V888888
 d8888888a                                `Y8888
AY/'' `\Y8b                                 ``Y8b
Y'      `YP                                    ~~
         `'            
 
        """
        print(ascii_art)
        print("👋 Bienvenue dans le menu de configuration\n")
    def update_informations(self):
        """
            va mettre à jour les informations dans le fichier
        """
        data = {"SSID":self.ssid, "PASSWORD":self.password, "URL":self.url}
        self.file.write_file(data=data)
    def summary(self):
        print(f"Voici un recapitulatif des informations collectés:\n    SSID: {self.ssid}\n    PASSWORD: {self.password}\n    URL: {self.url}")

config = Configuration()

config.display_starting_menu()
 
ssid = input(f"🌐 Entrez le SSID ({config.get_ssid()}) ")
config.set_ssid(ssid)
 
password = input(f"🔒 Entrez le mot de passe ({config.get_password()}) ")
config.set_password(password)
 
url = input(f"💻 Entrez l'adresse du serveur ({config.get_url()}) ")
config.set_url(url)

config.update_informations()

config.summary()
