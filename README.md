# TPEMSY
TP sur la BBG - mesure température / humidité / VCO & MSI
# Projet EMSY

Ce projet consiste à mesurer la température et l'humidité à l'aide d'un capteur SHT40, à calculer le point de rosée à partir de ces mesures, à enregistrer ces données dans un fichier CSV et à envoyer un email d'alerte lorsque la température dépasse 28 degrés Celsius.

## Fonctions du script

### read_sensor()

Cette fonction lit les données du capteur SHT40 et renvoie la température et l'humidité.

### calculate_dew_point(temperature, humidity)

Cette fonction calcule le point de rosée à partir de la température et de l'humidité. Elle prend en entrée la température en degrés Celsius et l'humidité en pourcentage, et renvoie le point de rosée en degrés Celsius.

### csv_write_row(file_path, data_row)

Cette fonction écrit une ligne de données dans un fichier CSV. Elle prend en entrée le chemin du fichier CSV et la ligne de données à écrire, et ne renvoie rien.

### send_email(recipients, subject, message)

Cette fonction envoie un email à une liste de destinataires. Elle prend en entrée la liste des destinataires, le sujet de l'email et le message de l'email, et ne renvoie rien.

## Comment exécuter le script

1. Exécutez le script `tp_emsy2.py` dans un terminal avec la commande `python3 tp_emsy2.py`.

## Modification des paramètres

Pour modifier l'adresse email du destinataire des alertes, modifiez la ligne suivante dans le script `tp_emsy2.py` :

```python
send_email(["matteo.stefanelli@eduvaud.ch"], subject, message)

