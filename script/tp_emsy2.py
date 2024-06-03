# Informations sur l'auteur et la version du script
__author__ = "VCO & MSI"
__version__ = "69.0"
__maintainer__ = "MSI & VCO"
__email__ = "matteo.stefanelli@eduvaud.ch"
__status__ = "Prototype"
__date__ = "juin2024"

# Importation des bibliothèques nécessaires
import datetime
import math
import csv
import smtplib
from sensirion_i2c_driver import I2cConnection
from sensirion_i2c_sht.sht4x import Sht4xI2cDevice
from sensirion_i2c_driver.linux_i2c_transceiver import LinuxI2cTransceiver
from datetime import time

# Initialisation du capteur
sensor = Sht4xI2cDevice(I2cConnection(LinuxI2cTransceiver('/dev/i2c-2')))

# Fonction pour lire les données du capteur
def read_sensor_data():
    try:
        # Essaye de lire les données du capteur SHT40
        # temp est la température et hum est l'humidité relative
        temp, hum = sensor.single_shot_measurement()
    except Exception as error:
        # Si une erreur se produit lors de la lecture des données du capteur, 
        # elle est capturée et un message d'erreur est affiché
        print("Erreur lors de la récupération des valeurs du capteur:", error)
    else:
        # Si aucune erreur ne se produit, la température et l'humidité sont renvoyées
        return temp, hum
    # Si une erreur se produit, la fonction renvoie 0
    return 0

# Fonction pour calculer le point de rosée
def calculate_dew_point(temp, hum):
    # Coefficient de Magnus pour la température
    beta = 17.62
    # Coefficient de Magnus pour l'humidité
    lamb = 243.12
    # Calcul de la première partie de la formule du point de rosée
    part1 = lamb * (math.log(hum/100) + ((beta * temp)/(lamb + temp)))
    # Calcul de la deuxième partie de la formule du point de rosée
    part2 = beta - (math.log(hum/100) + ((beta * temp)/(lamb + temp)))
    # Calcul du point de rosée en divisant part1 par part2
    dew_point = part1 / part2
    # Renvoie le point de rosée
    return dew_point

# Fonction pour écrire une ligne dans un fichier CSV
def write_row_to_csv(file_path, row_data):
    try:
        # Ouvre le fichier en mode 'append' (ajout à la fin du fichier)
        with open(file_path, 'a') as file:
            # Crée un écrivain CSV qui écrira dans le fichier
            csv_writer = csv.writer(file)
            # Écrit la ligne de données dans le fichier CSV
            csv_writer.writerow(row_data)
    except Exception as error:
        # Si une erreur se produit lors de l'écriture dans le fichier, 
        # la fonction renvoie 0 et l'exception
        return 0, error
    else:
        # Si aucune erreur ne se produit, la fonction renvoie 1
        return 1

# Fonction pour envoyer un email
#Fonction reprise depuis le dernier TP-- Send an email en python (Semestre 1 - EMSY)
def send_email(receiver, subject, message):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login('ETML.ES.EMSY@gmail.com',"cely neve caly akjz")
        sender = "ETML.ES.EMSY@gmail.com"
        headers = {
            'Content-Type': 'text/html; charset=utf-8',
            'Content-Disposition': 'inline',
            'Content-Transfer-Encoding': '8bit',
            'From': sender,
            'To':receiver,
            'Date': datetime.datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
            'X-Mailer': 'python',
            'Subject': subject
        }
        email_msg = ''
        for key, value in headers.items():
            email_msg += "%s: %s\n" % (key, value)
        email_msg += "\n%s\n" % message
        try:
            server.sendmail(headers['From'], headers['To'], email_msg.encode("utf8"))
            print("Email envoyé avec succès!")
        except Exception as error:
            print("Une erreur s'est produite:", error)

# Script principal
if __name__ == "__main__":
    # Affichage d'un message de bienvenue
    print("Bonjour et bienvenue à EMSY")

    # Étape 1: Mesure de la température et de l'humidité
    # La fonction get_sensor_data() est appelée pour lire les données du capteur
    temp, hum = read_sensor_data()

    # Affichage de la température et de l'humidité sur la console
    print("La température est de :",temp)
    print("L'humidité est de :",hum)

    # Étape 2: Calcul du point de rosée
    # La fonction compute_dew_point() est appelée avec la température et l'humidité comme arguments
    dew_point = calculate_dew_point(temp.degrees_celsius, hum.percent_rh)

    # Affichage du point de rosée sur la console
    print("Le point de rosée est :",dew_point)

    # Étape 3: Enregistrement des données dans un fichier CSV
    # Obtention de la date et de l'heure actuelles
    current_datetime = datetime.datetime.now()
    date = current_datetime.strftime("%d.%m.%Y")
    time = current_datetime.strftime("%H:%M")

    # Préparation de la ligne de données à écrire dans le fichier CSV
    row_data = [date, time, round(temp.degrees_celsius,1), round(hum.percent_rh,1), round(dew_point,1)]

    # Chemin du fichier CSV
    csv_file_path = '/home/debian/TempLog.csv'

    # Appel de la fonction write_row_to_csv() pour écrire la ligne de données dans le fichier CSV
    write_row_to_csv(csv_file_path,row_data)

    # Étape 4: Envoi d'un email si la température dépasse 28 degrés Celsius
    if temp.degrees_celsius >= 28:
        # Préparation du sujet et du message de l'email
        email_subject = "Attention temperature en hausse"
        email_message = "La temperature vient de depasser les 28 degrees" + str (round(temp.degrees_celsius,1))

        # Appel de la fonction send_email() pour envoyer l'email
        send_email(["matteo.stefanelli@eduvaud.ch"], email_subject, email_message)

        # Affichage du message de l'email sur la console
        print("Le point de rosée est :",email_message)