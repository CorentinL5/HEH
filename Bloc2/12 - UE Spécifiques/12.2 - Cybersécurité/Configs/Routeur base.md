```bash
en 
conf t
!
hostname G1-RTR-AG003-00-001
!
! ==============================
! 🔧 Interfaces WAN vers Firewalls
! ==============================

interface GigabitEthernet0/0
 description Liaison vers Firewall AG3 (VDOM AG3)
 ip address 172.20.55.1 255.255.255.252
 no shutdown

interface GigabitEthernet0/1
 description Liaison vers Firewall AG4 (VDOM AG4)
 ip address 172.21.55.1 255.255.255.252
 no shutdown

!
! =============================
! 🔀 Interface LAN (Trunk vers Switch)
! =============================

interface GigabitEthernet0/2
 description Trunk vers Switch L2
 no ip address
 switchport trunk encapsulation dot1q
 switchport mode trunk
 no shutdown

!
! =============================
! 🔄 Routage statique
! =============================

ip routing
ip route 0.0.0.0 0.0.0.0 172.20.55.2
ip route 172.21.0.0 255.255.0.0 172.21.55.2

!
! =============================
! 🔐 Comptes locaux
! =============================

username admin privilege 15 secret MonSuperMotDePasseAdmin
username oper privilege 1 secret MonMotDePasseOper

!
! =============================
! 🔐 SSH sécurisé
! =============================

ip domain name heh.local
crypto key generate rsa modulus 3072
ip ssh version 2
ip ssh authentication-retries 3
ip ssh time-out 60

!
! =============================
! 🔐 Lignes VTY protégées par ACL
! =============================

line vty 0 4
 login local
 transport input ssh
 access-class 50 in

!
! =============================
! 🔐 ACL : accès SSH depuis VLAN de gestion uniquement
! =============================

ip access-list standard 50
 permit 172.20.50.0 0.0.0.255
 deny any

!
! =============================
! ❌ Désactivation des interfaces web
! =============================

no ip http server
no ip http secure-server

!
! =============================
! 🛡 Bannière MOTD de sécurité (compatibilité ASCII)
! =============================

banner motd ^

ATTENTION : Acces reserve aux administrateurs autorises.
Toute tentative non autorisee sera enregistree et signalee.

^
```
