! Entrée en mode privilégié
enable

! Configuration du nom du switch en utilisant le plan de nommage des équipements
hostname G1-SWT-AG003-00-P-001  ! Nom du switch selon le plan de nommage des équipements

! Configuration du message d'accueil MOTD
banner motd ! Attention ! Accès restreint. Toute tentative d'accès non autorisée sera poursuivie. !

! Création de tous les VLANs selon le plan d'adressage
vlan 10
    name Informatique
    exit

vlan 15
    name Commerciaux
    exit

vlan 20
    name Technique
    exit

vlan 25
    name Finances
    exit

vlan 30
    name Marketing
    exit

vlan 35
    name RD
    exit

vlan 40
    name RH
    exit

vlan 45
    name Direction
    exit

vlan 50
    name Gestion
    exit

vlan 55
    name Transit
    exit

vlan 60
    name Servers
    exit

vlan 65
    name Voix
    exit

vlan 70
    name Wi-Fi
    exit

vlan 100
    name Natif
    exit

vlan 199
    name Poubelle
    exit

! Configuration des interfaces pour chaque VLAN
interface range fa0/1 - 24
    switchport mode access
    switchport access vlan 30  ! Assigne par défaut le VLAN 30 à ces interfaces
    exit

! Configuration de l'interface trunk pour les connexions inter-switches ou avec un routeur
interface gig0/1
    switchport mode trunk
    switchport trunk allowed vlan 10,15,20,25,30,35,40,45,50,55,60,65,70,100,199  ! Inclut tous les VLANs
    exit

! Configuration de l'interface VLAN de gestion
interface vlan 100
    ip address 172.20.100.1 255.255.255.0
    no shutdown
    exit

! Activation de l'interface de gestion
interface gig0/0
    no shutdown
    exit

! Configuration du mot de passe pour l'accès privilégié
enable secret G1_Agence3_Password

! Configuration du mot de passe pour la console
line con 0
    password G1_Console_Password
    login
    exit

! Configuration du mot de passe pour l'accès SSH
line vty 0 4
    password G1_SSH_Password
    login
    transport input ssh
    exit

! Configuration pour l'accès SSH
ip domain-name heh.local
crypto key generate rsa modulus 2048
ip ssh version 2

! Sauvegarde de la configuration
write memory
