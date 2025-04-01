en
config t

! Configuration du nom d'hôte
hostname G1-SWT-AG003-00-P-201

! Configuration des mots de passe
enable secret cisco123
line con 0
password cisco123
login
line vty 0 15
password cisco123
login


! Configuration des VLANs
vlan 10
name VLAN_10
exit
vlan 20
name VLAN_20
exit


