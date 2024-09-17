---
created: 2024-02-08
tags:
  - Lessons/School/HEH/Bloc1/Quad2
---

# # 📚  Télécommunications et réseaux TH HEHB1Q2
> **Création de la note à *`09:32`* le *`2024-02-08`.***
---
[[../Lessons 🏫/0 - Lessons Menu|🏫 - Lessons Menu]]

# 📝 Prise de Notes - Cours

---

## 👋 Infos du Cours
- **Professeur :** Pétein

---

## 📅 Dates de cours

|     Date      |      Heures      | Local |     |                                              Note                                              |
| :-----------: | :--------------: | :---: | --- | :--------------------------------------------------------------------------------------------: |
| jeu. 08 févr. | de 08h15 à 10h15 | 2/09A |     | [[Télécommunications et réseaux TH - HEHB1Q2#Note du ../Daily 📆/2024-02-08 2024-02-08|Clique]] |
| jeu. 15 févr. | de 08h15 à 10h15 | 2/09A |     |            [[Télécommunications et réseaux TH - HEHB1Q2#Note du 2024-02-15|Clique]]             |
| mar. 20 févr. | de 08h15 à 10h15 | 2/09A |     |            [[Télécommunications et réseaux TH - HEHB1Q2#Note du 2024-02-20|Clique]]             |
| jeu. 22 févr. | de 08h15 à 10h15 | 2/09A |     | [[Télécommunications et réseaux TH - HEHB1Q2#Note du ../Daily 📆/2024-02-22 2024-02-22|Clique]] |
| mar. 27 févr. | de 08h15 à 10h15 | 2/09A |     |                                [[#Note du 2024-02-27\|Clique]]                                 |
| ven. 01 mars  | de 10h30 à 12h30 | 2/09A |     |                                [[#Note du 2024-03-01\|Clique]]                                 |
| mar. 12 mars  | de 08h15 à 10h15 | 2/09A |     |                                [[#Note du 2024-03-12\|Clique]]                                 |
| mar. 19 mars  | de 08h15 à 10h15 | 2/09A |     |                                               ❌                                                |
| ven. 05 avr.  | de 10h30 à 12h30 | 2/09A |     |                                               ❌                                                |
| ven. 12 avr.  | de 10h30 à 12h30 | 2/09A |     |                                               ❌                                                |
| ven. 19 avr.  | de 10h30 à 12h30 | 2/09A |     |                                               ❌                                                |
|  ven. 24 mai  | de 08h30 à 10h30 | 2/09A |     |                                               ❌                                                |

---

## ❓ Questions à Poser

- [Question 1]
- [Question 2]
- [Question 3]

---

## 📚 Références

- [Télécommunications et réseaux](https://ecampus.heh.be/course/view.php?id=2373 "TRBLOC1")

---

## 🤔 Réflexions Rapides 

- [Réflexion 1]
- [Réflexion 2]

---
## 📑 Notes

### Note du [[../Daily 📆/2024-02-08|2024-02-08]]
#### Récap Examen
- Note moyenne 10/20.
- TCP/IP <=> OSI
- MB/s = 8Mbits/s
- conversion `binaire - décimal - hexadécimal - octal`
- Exercice: 196.100.55.113 /19
	  1. `AR ?`  <u>1100 0100.0110 0100.001</u>1 0111.0111 0001 / 2x8 + 3 => 196.32.0.0
	  2. `BC ?` 196.100.63.255.
	  3. `Nombre d'hôtes utilisables ?`  $2^x-2, x=32-19$ => $8192-2=8190$

---

### Note du [[2024-02-15]]
#### Découpage réseau
- intro:
	- pas de soucis si c'est **un** petit réseau 
	- S'il y a des centaines d'hôtes cela deient problématique.
	- Sous diviser un réseau permet d'ajouter un niveau hiérarchique pour obtenir 3 niveaux
		1. Un réseau
		2. Un sous réseau
		3. Un hôte
- Pourquoi découper un réseau ? 
	- EN GROS: permet lors d'un envoie d'info, de ne pas envoyer à TOUT les périphériques le dit "message".
- Comment découper un réseau ?
	- Éviter les doublons d'adresses *(chaque hôte doit être associé à UNE adresse Unique)*
	- Assurer et contrôler l'accès 
	- Surveiller la sécurité et les performances 
- Exemples de règles
	- Imprimantes *(adresses IP statiques)* 
	- Utilisateurs *(adresses IP Dynamiques)* 
	- Routeurs *(adresses IP statiques)* 
- Comment communiquent les sous réseaux entre eux ?
	- ⚠️Routeur
- Comment faire des sous réseaux correctes ?
	- Explication du Projet fictif:
		- config et mettre en place le matériel 
		- Plage d'adresse 192.168.160.0/19
		- trois catégories
			- 550 techniciens
			- 130 commerciaux
			- 10 directeurs
	- Résolution du projet *(feuille)*
- Important ⚠️
	- Plus grande au plus petites plages d'adresses,
	- Faire gaffe à l'adresse de sous réseau quelle soit *(compatible)*
	- Trous possibles entre les plages

---
### Note du [[2024-02-20]]
- Découpage réseau 1 seul exercice...

- Création d'un programme python pour faire les calculs :)

---

### Note du [[../Daily 📆/2024-02-22|2024-02-22]]
 
#### Découpage réseau - exercice 2
##### énoncé (trié)
|Nom|fonction|IP|Masque|
|:---:|:---:|:---:|:---:|
|Mlle Liam|commercial|195.208.192.033|/25|
|M Frick|manufacture|195.208.192.133|/25|
|m simon|marketing|195.208.192.210|/25|
|mme gravic|RH|195.208.193.004|/27|
|M Dupont|directeur|195.208.193.011|/27|
|mlle silva|secrétariat|195.208.193.025|/27|
|m geek|informaticien|195.208.193.029|/27|
|m trouvaille|R&D|195.208.193.077|/27|
|Mme Chiffre|comptable|195.208.193.205|/29|
##### Résolution
| Département | AR | BC | N° hôtes th |  |
| :--: | :--: | :--: | :--: | ---- |
| commercial | 195.208.192.000 | 195.208.192.127 | 128 |  |
| manufacture, marketing | 195.208.192.128 | 195.208.192.255 | 128 |  |
| Direceur, IT, RH, secrétariat | 195.208.193.000 | 195.208.193.031 | 32 |  |
| ***Testing*** | *195.208.193.032* | *195.208.193.063* | *32* | After |
| R&D | 195.208.193.064 | 195.208.193.095 | 32 |  |
| Compta | 195.208.193.200 | 195.208.193.207 | 8 |  |
| ***Client*** | *195.208.194.0* | *195.208.193.128* | *128* | After |

##### Ajouts
- Testing (20) 
- Clients (100)

---
### Note du [[2024-02-27]]
#### Découpage réseau IPV6
Découpage par tranche de 4 bits (/68, /72 mais pas /65).

#### Test réseau
- par le protocole **ICMP** 
- fourni des commentaires/messages d'erreurs
=> récup info
- Codes IPV4
	- 0 réseau inacessible
	- 1 hote inacessible
	- 2 protocole inacessible
	- 3 port inacessible
TTL = Time To Leave
TraceRoute
#todo 

#### Sécurité réseau
#todo 
##### Malwares (3types)
- Virus (fichier)
- Vers (logiciel autonomes)
- Chevaux de Troie (Fausse apparence légitime)
##### Attaques
- de reconnaissance
	- dictionaire
	- force brute
	- interception de trafic
	- ingénierie sociale
- par accès
- déni de service

---
### Note du [[2024-03-01]] 
Ethernet

---

### Note du [2024-03-12]
Exercice Ethernet 

---

### Note du [xxxx-xx-xx]
- [Note 1]
- [Note 2]

---
