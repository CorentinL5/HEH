---
created: 2025-11-07
tags:
  - Lessons/School/HEH/Bloc2/Quad1
  - Lessons/School/HEH/Bloc2/Quad2
Auteur: LALLEMENT Corentin - 240314
---

# # 📚  Template des commandes TP Cisco
> **Création de la note à *`08:48`* le *`2025-11-07`.***
> Par `LALLEMENT Corentin`, **`240314`**.
---

# Basic
## Mode privilégié
```
enable                                ! Passe en mode privilégié (EXEC privilégié)
```

## Mode de configuration globale
```
configure terminal                   ! Passe en mode de configuration globale
```

## Message du jour (MOTD)
```
banner motd # <message> #            ! Définit un message d'accueil affiché à la connexion
```

## Configuration des mots de passe
```
enable password <mot_de_passe>       ! Définit un mot de passe pour le mode privilégié
enable secret <mot_de_passe>         ! Définit un mot de passe chiffré pour le
										    mode privilégié (préféré à 'password')
line console 0                       ! Accède à la ligne console
 password <mot_de_passe>             ! Définit un mot de passe pour la console
 login                               ! Active la demande de mot de passe
exit
line vty 0 4                         ! Accède aux lignes VTY pour les connexions
										distantes
 password <mot_de_passe>             ! Définit un mot de passe pour les
										 accès Telnet/SSH
 login                               ! Active la demande de mot de passe
```

<div style="page-break-after: always;"></div>

## Sauvegarde et restauration de la configuration
```
copy running-config startup-config      ! Sauvegarde la configuration en mémoire
									        NVRAM
copy startup-config running-config      ! Restaure la configuration depuis la NVRAM
erase startup-config                    ! Supprime la configuration sauvegardée
reload                                  ! Redémarre le périphérique
```

## Affichage des informations
```
show ip interface brief                 ! Affiche un résumé des interfaces et
											adresses IP
show interfaces                         ! Affiche des détails sur les interfaces
show vlan brief                         ! Affiche la liste des VLANs
show mac address-table                  ! Affiche la table des adresses MAC
show running-config                      ! Affiche la configuration en cours
show startup-config                      ! Affiche la configuration sauvegardée
show version                             ! Affiche les informations du système
```

<div style="page-break-after: always;"></div>

# SRWE
## Configuration des interfaces
```
interface <interface>                ! Sélectionne l'interface à configurer
										(ex: G0/0, F0/1)
 ip address <ip_v4> <masque>         ! Définit l'adresse IPv4 et le 
										 masque de sous-réseau
 ipv6 address <ip_v6>                ! Définit une adresse IPv6 sur l'interface
 no shutdown                         ! Active l'interface (la remet en UP)
 description <texte>                 ! Ajoute une description à l'interface
```

## Configuration des VLANs
```
vlan <vlan_id>                        ! Crée un VLAN avec l'identifiant spécifié
 name <nom_vlan>                      ! Attribue un nom au VLAN
```

## Assignation des VLANs aux interfaces
```
interface <interface>                ! Sélectionne l'interface
 switchport mode access              ! Configure le port en mode accès 
										 (pour un seul VLAN)
 switchport access vlan <vlan_id>    ! Associe l'interface au VLAN spécifié
```

## Mode Trunk
```
interface <interface>                       ! Sélectionne l'interface
 switchport mode trunk                      ! Configure l'interface en mode trunk
 switchport trunk allowed vlan <vlan_list>  ! Autorise les VLANs spécifiques
												 (ex: 10,20,30)
```

## Configuration des routes statiques
```
ip route <destination> <masque> <next_hop>  ! Ajoute une route statique IPv4
ipv6 route <destination> <next_hop>         ! Ajoute une route statique IPv6
```

## Activation du routage entre VLANs
```
ip routing                               ! Active le routage IPv4 inter-VLAN
ipv6 unicast-routing                     ! Active le routage IPv6 inter-VLAN
```

<div style="page-break-after: always;"></div>

# ENSA
## Configuration d'un DHCP Server
```
ip dhcp excluded-address <ip_start> <ip_end>  ! Exclut une plage d'adresses du DHCP
ip dhcp pool <nom_pool>                       ! Crée un pool DHCP
 network <ip_reseau> <masque>                 ! Définit le réseau du DHCP
 default-router <ip_routeur>                  ! Spécifie la passerelle par défaut
 dns-server <ip_dns>                          ! Définit le serveur DNS
```

## Configuration de NAT
```
ip nat inside source list <acl_id> interface <interface_externe> overload
# Active NAT dynamique avec surcharge

access-list <acl_id> permit <ip_reseau> <masque>
# Définit l'ACL pour NAT

interface <interface>
# Sélectionne l'interface interne

 ip nat inside
 # Configure l'interface en tant qu'intérieur NAT
 
interface <interface>
# Sélectionne l'interface externe

 ip nat outside
 # Configure l'interface en tant qu'extérieur NAT
```

## Sécurisation des ports switch (Port Security)
```
interface <interface>                         ! Sélectionne l'interface
 switchport port-security                     ! Active la sécurité des ports
 switchport port-security maximum <nombre>    ! Définit le nombre maximal
												 d'adresses MAC
 switchport port-security violation <mode>    ! Définit l'action en cas de
												 violation
												 (protect, restrict, shutdown)
 switchport port-security mac-address sticky  ! Active l'apprentissage des
												 adresses MAC dynamiquement
```

<div style="page-break-after: always;"></div>

## Configuration d'un serveur SSH
```
ip domain-name <nom_domaine>             ! Définit le nom de domaine
crypto key generate rsa                  ! Génère une clé RSA pour SSH
ip ssh version 2                         ! Active SSH version 2
line vty 0 15                            ! Accède aux lignes VTY 
											(connexion à distance)
 transport input ssh                     ! Active SSH uniquement
 login local                             ! Demande une authentification locale
```

## Configuration d'un serveur Syslog
```
logging host <ip_serveur_syslog>        ! Définit l'hôte Syslog
logging trap <niveau>                   ! Définit le niveau des logs envoyés
```

## Configuration d'un serveur NTP
```
ntp server <ip_ntp>                     ! Définit l'adresse du serveur NTP
clock timezone <zone> <décalage>        ! Définit le fuseau horaire
```