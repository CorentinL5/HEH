---
created: 2024-09-20
tags:
  - Lessons/School/HEH/Bloc2/Quad2
---

# # 📚  Ch1 - Routage
> **Création de la note à *`11:32`* le *`2024-09-20`.***
---

# 📝 Prise de Notes - Cours

---
- Les réseaux :
	- Nous utilisons les réseaux de diverses manières
	- BCP de réseaux différents
- Caractéristique des réseaux
	- La topologie
		- physique
		- logique
	- La vitesse (débit)
	- Le coût
	- La sécurité
	- La disponibilité
		- les 5 "9" (99,999%) = 5 minutes par an
	- L'évolutivité
	- La fiabilité
- Les routeurs
	- Équipement spécialisé dans la transmission de paquets entre réseaux
	- Autres fonctions
		- QoS
		- ACL
		- Fonctions de sécurité (Pare feu, IPS, ..)
	- Plans fonctionnels d'un routeur
		1. Management plane
			- Plan de gestion
			- protocols
				- Telnet, SSH
				- Protocoles de transferts de fichiers (TFTP, SCP)
				- SNMP, Netflow, syslog
				- NTP
				- TACACS+
		2. Control plane
			- Plan de contrôle (gère les paquets et le trafic)
		3. Data plane
			- Plan de données (données des utilisateurs)
	- Trois mécanisme de transfert de données
		1. Commutation de processus
			![[Pasted image 20240920115053.png]]
		2. Commutation rapide (Fast switching)
			![[Pasted image 20240920115131.png]]
		3. Cisco Express Forwarding
			![[Pasted image 20240920115149.png]]
			Routage rapide sans compréhension de ce qui se passe
	- Fonctions principales du routeur
		- Couche 2
			- changent à chaque saut
			- Protocols peuvent être différents en entrée et sortie du routeur
			- Pour Ethernet (Adresse MAC, table ARP, table de commutation)
		- Couche 3
			- Adresses de couche 3 
				- Peuvent être conservées de la source à la destination
				- Peuvent varier en présence de NAT
			- Table de routage
	- Réception d'un paquet IP par le routeur
		![[Pasted image 20240920120414.png]]
- Tables de routage
	- Une table
		  ![[Pasted image 20240920121318.png]]
		  ![[Pasted image 20240920121526.png]]
	- Détermination du chemin
		![[Pasted image 20240920121609.png]]
	- Sélection du meilleur chemin
		- Métrique et meilleure route
		- Meilleure correspondance de la table de routage
	- Résolution de l'interface de sortie
		![[Pasted image 20240920121723.png]]
	- Distance administrative
		![[Pasted image 20240920122606.png]]





1)
	# ip access-list standard EXE1
	# Remote exe 1
	# permit 192.168.0.0 0.0.255.255
2)
	# ip access-list standard EXE2
	# Remote exe 2
	# deny 192.168.0.0 0.0.255.255
3)
	# ip access-list standard EXE3
	# Remote exe 3
	# permit 192.168.0.0 0.0.254.255