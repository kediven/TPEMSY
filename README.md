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
   
3. Connectez-vous en tant qu'utilisateur avec l'utilisateur : `debian` et le mot de passe :`temppwd`.
4. Exécutez le script `tp_emsy2.py` dans un terminal avec la commande `python3 tp_emsy2.py`.







