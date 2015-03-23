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



#Procédure d'utilisation
##Démarrage
##consultation sur l'écran
##consultation sur web serveur
#Conclusion
> Written with [StackEdit](https://stackedit.io/).