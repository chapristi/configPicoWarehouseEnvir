from machine import Pin
from time import sleep
import dht
import network
import urequests
import json
from File import File

# Création d'une instance du capteur de température et d'humidité DHT22 connecté à la broche GPIO 18
capteur = dht.DHT22(Pin(18))

# Création d'une instance d'un objet WLAN pour se connecter à un réseau Wi-Fi en tant que client
wlan = network.WLAN(network.STA_IF)
wlan.active(True)  # Activation de l'interface Wi-Fi

# Création d'une instance de la classe File pour la gestion du fichier
file = File("data.json")
data = file.read_file()  # Lecture des informations de connexion au Wi-Fi depuis le fichier

# Connexion au réseau Wi-Fi
wlan.connect(data["SSID"], data["PASSWORD"])
print(wlan.isconnected())

# Attente de la connexion au réseau Wi-Fi
while not wlan.isconnected():
    print('.', end="")
    sleep(0.5)
    
print("\nOK")
mac_address = wlan.config('mac')
mac_address_str = ':'.join('%02x' % b for b in mac_address)
print("MAC address:", mac_address_str.upper())

def jsonDump(informations):
    """
    Cette fonction convertit les données d'entrée en format JSON.
    """
    return json.dumps(informations)

def sendPostReq(humidity, temperature, url):
    """
    Cette fonction envoie les informations à l'API via une requête POST.
    """
    informations = {
        "temperature": temperature,
        "humidity": humidity,
        "macAddress": mac_address_str
    }
    payload = jsonDump(informations)
    headers = {"Content-Type": "application/json"}
    resp = urequests.post(url + "/api/sensorDatas", data=payload, headers=headers)
    return resp.json()

while True:
    try:
        capteur.measure()  # Mesure de la température et de l'humidité
        print(capteur.humidity(), capteur.temperature())
        response = sendPostReq(capteur.humidity(), capteur.temperature(), data["URL"])
        print(response)
        sleep(30)  # Attente de 30 secondes avant la prochaine mesure
    except OSError as e:
        print("Échec de la réception")

