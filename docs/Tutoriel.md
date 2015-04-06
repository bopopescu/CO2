TUTORIEL
===================


[TOC]
#Introduction
Le but de ce tutoriel est d'expliquer comment utiliser un Rasberry Pi pour lire une sonde CO2, et ensuite d'afficher sur un écran et sur un webservice la valeur obtenue.
L'ensemble est disponible à l'adresse suivante : http://github.com/IUT1-CO2/CO2
#Matériel
##Raspberry Pi
Raspberry Pi : http://www.raspberrypi.org/

> **Nb :** Nous avons testé le code avec un Raspberry Pi version 1 modèle B et B+ sous Raspbian.

##Carte d'affichage
PiFace Control and display :
 http://www.piface.org.uk/products/piface_control_and_display/
##Sonde CO2

SenseAir  :  http://senseair.se/products/oem-modules/k30/


#Etapes d'instalation
##Branchement
Inserez la carte SD munie d'un Raspbian fraichement installé.
Connectez le Raspberry Pi et la carte d'affiche grâce au bornier latéral du Raspberry Pi.
Connectez le Raspberry Pi par sa sortie RJ45 avec un cable PT100 ou PT1000 à votre ordinateur ou routeur.
Alimentez le.
Connectez la Sonde CO2 au Raspberry Pi.
> **Nb :** Pour le modèle B+, connectez la carte d'affichage au plus proche de la carte SD du Raspberry Pi.

##Bibliothèque
Les bibliothèques utilisées ont été modifier pour répondre au critère d'utilisation. Elles sont disponible sur GitHub : 
http://github.com/IUT1-CO2/CO2

télécharger la bibliothèque permettant l'utilisation de la carte PiFace Control and display :
```
$ sudo aptitude install python-pifacecad
do you want to continue ? [Y/n/?] 
$ y // pour confimer
``` 

##GitHub
Pour récuperer l'ensemble du code, des bibliothèques et des datasheets allez sur GitHub à l'adresse suivante:
http://github.com/IUT1-CO2/CO2
Pour récupérer les sources : 
Se placer dans le dossier home: 
```
$ cd
$ mkdir CO2
$ cd CO2
$ wget https://github.com/IUT1-CO2/CO2/archive/master.zip
$ tar -xf master.zip
$ cd CO2-master
$ ls // bien verifier que le dossier n'est pas vide

```

##Configuration

Toutes procedures pour la première utilisation du Raspberry Pi ne seront pas détaillé dans ce tutoriel. De nombreux tutoriels sont disponibles sur internet. 
Les quelques lignes a rajouter sont :
```
$ nano pvServerMain.py ( chercher la ligne " plix.http.address":"...." et remplacer les "...." par l'adresse du Raspberry'
$ ctrlx

$ sudo raspi-config
selctionner advanced options puis spi et cocher Yes

Puis valider le reste des fenêtres.
```


#Procédure d'utilisation
##Démarrage
Une fois le programme installé. Il n'y a pas de procédure spécifique au démarage. Le programme se lancera automatiquement au démarrage du Raspberry Pi.
Sinon taper la commande suivante:
```
	$ python pvServerMain.py

```

> **Nb :** Si il y a l'erreur " serial.serialutil.SerialException:could not open...." c'est que le capteur est non ou mal branché.
##consultation sur l'écran
La consultation de la valeur CO2 sur l'écran se fait par l'appuis sur le bouton poussoir S5 ( pendant 5 secondes ) de la carte d'affichage.
##consultation sur web serveur
Pour lire la valeur depuis le web serveur il suffit de ce connecter au serveur à l'adresse configurée lors de l'installation du programme.
#Conclusion

Une fois le programme installé dans votre Raspberry Pi, l'utilisation est très intuitive et ne demande aucune intervention. La valeur relevée est alors disponible soit sur le web serveur soit directement sur l'écran de la carte d'affichage. 

Récapitulatif des commandes utilisé:
```
$ cd
$ mkdir CO2
$ cd CO2
$ wget https://github.com/IUT1-CO2/CO2/archive/master.zip
$ tar -xf master.zip
$ cd CO2-master
$ ls // bien verifier que le dossier n'est pas vide

```
> Written with [StackEdit](https://stackedit.io/).
