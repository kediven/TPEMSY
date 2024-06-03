# TPEMSY
TP sur la BBG - mesure de la température / humidité / VCO & MSI

## Projet EMSY

Ce projet consiste à mesurer la température et l'humidité à l'aide d'un capteur SHT40, à calculer le point de rosée à partir de ces mesures, à enregistrer ces données dans un fichier CSV et à envoyer un email d'alerte lorsque la température dépasse 28 degrés Celsius.

## Fonctions du script

### read_sensor_data()

Cette fonction lit les données du capteur SHT40 et renvoie la température et l'humidité. Si une erreur se produit lors de la lecture, elle est capturée et un message d'erreur est affiché.

### calculate_dew_point(temp, hum)

Cette fonction calcule le point de rosée à partir de la température et de l'humidité. Elle utilise les coefficients de Magnus pour effectuer le calcul. Voir image aprés listing pour en savoir plus sur la formule utilisée.

### write_row_to_csv(file_path, row_data)

Cette fonction écrit une ligne de données dans un fichier CSV. Si une erreur se produit lors de l'écriture, elle est capturée et un message d'erreur est affiché.

### send_email(receiver, subject, message)

Cette fonction envoie un email à une liste de destinataires. Elle utilise le protocole SMTP pour envoyer l'email.

## Comment exécuter le script

1. Connectez-vous au terminal PUTTY et connectez-vous à l'adresse de notre BBG avec l'adresse IP.
![image](https://github.com/kediven/TPEMSY/assets/144989993/b1204ff9-1883-44de-a194-edfe32fcce0b)

2. Connectez-vous en tant qu'utilisateur avec l'utilisateur : `debian` et le mot de passe :`temppwd`.
![image](https://github.com/kediven/TPEMSY/assets/144989993/a4e415fa-d93d-43f3-b960-6412a7bb0a43)

3. Exécutez le script `tp_emsy2.py` dans un terminal avec la commande `python3 tp_emsy2.py`.
![image](https://github.com/kediven/TPEMSY/assets/144989993/06dd8258-955b-40ed-938d-fef907d92de6)

## Voici les librairies utilisées
Nous utilisons lors de l'initialisation du capteur ces librairies dans le reportoire dev qui ont été implémentées par l'utilisateur "root"
![image](https://github.com/kediven/TPEMSY/assets/144989993/e2adff2d-7635-4ca8-b3ec-535e9ba58a07)

Nos différentes librairies locales téléchargées depuis github
![image](https://github.com/kediven/TPEMSY/assets/144989993/05657fe2-0f19-4b8d-b772-c8d1a2762734)

## Données sur le fichier .csv dans le chemin d'accès désiré 
![image](https://github.com/kediven/TPEMSY/assets/144989993/971a0358-423a-457c-99b3-f3b7e2d3394f)
![image](https://github.com/kediven/TPEMSY/assets/144989993/c6d68ed4-affa-433d-8b97-3f646512c902)

## CRON sous le système Unix :
Afin de rentrer dans le planificateur de tâches nous devons éxécuter la commande `crontab -e`.
Par la suite nous demandons donc à exécuter le script python réalisé toutes les 15 minutes, à chaque heure, chaque jour, chaque mois et chaque jour de la semaine. 
Format de demande : minutes/heure/jour/mois et jour de la semaine
![image](https://github.com/kediven/TPEMSY/assets/144989993/1ae87116-d647-4caf-b199-17e58b495515)


## ERREUR NETWORK
Nous avons obtenu des erreurs lors de l'envoi du mail alors que nous n'avions pas auparavant.
Notre code pour l'envoi du mail semble fonctionnel mais nous n'avions jamais réussi à obtenir un e-mail d'avertissement.
Nous avons obtenu ceci lorsque nous dépassons de 28°C:
![image](https://github.com/kediven/TPEMSY/assets/144989993/7f626183-5b4f-4072-8f90-69f888ab3c15)

Dans notre script nous faisons appel au serveur SMTP pour l'envoi automatique du mail, mais il se trouve que nous n'arrivons
pas à établir une connexion. Nous nous sommes connectés à la BBG et nous avons essayé de joindre "google.ch" ou alors "github.com" et voici le résultat :

![image](https://github.com/kediven/TPEMSY/assets/144989993/b6e2207a-ea4e-48da-9932-bfddae1e51df)





















