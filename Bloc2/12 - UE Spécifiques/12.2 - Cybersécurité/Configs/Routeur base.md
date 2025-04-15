```bash
############################################
# 📡 ROUTEUR AGENCE 3 (Partagé avec AG4)   #
# 🔧 Config bloc 2 : Essentiel et Sécurisé #
############################################

hostname G1-RTR-AG003-00-001

!
! 🔧 Interfaces WAN (vers firewall/VDOM Root)
!
interface GigabitEthernet0/0
 description Liaison vers Firewall AG3 (VDOM AG3)
 ip address 172.20.55.1 255.255.255.252
 no shutdown

interface GigabitEthernet0/1
 description Liaison vers Firewall AG4 (VDOM AG4)
 ip address 172.21.55.1 255.255.255.252
 no shutdown

!
! 🔀 Interface LAN (Trunk vers Switch L2)
!
interface GigabitEthernet0/2
 description Trunk vers Switch L2
 no ip address
 switchport mode trunk
 switchport trunk encapsulation dot1q
 no shutdown

!
! 🔄 Routage statique (bloc 2)
!
ip routing
ip route 0.0.0.0 0.0.0.0 172.20.55.2   ! Default vers VDOM AG3
ip route 172.21.0.0 255.255.0.0 172.21.55.2   ! Accès AG4 via son VDOM

!
! 🔐 Sécurité minimale (bloc 2)
!
! Comptes locaux avec mots de passe chiffrés
username admin privilege 15 secret 9 $9$hopla$9415c0bc862924cb2f3ee9714107e6b41a8f82715cb1e185fc9e3eeaf15bb46b4322b3345114952593d94dc7dc032e39b8ae2097cfb692aa98319e79dbce62aa
username oper privilege 1 secret 9 $9$grenouille$9012f861cc2598f54d4e67cce94b5752daf38a8e3b1d398ee9d7cb3dcff69ba011b04c2e88d0d50fca5775ed4cff90f6b51e962d1c410a56f4f5ebe60e6671927

! Activez SSH uniquement depuis VLAN de gestion
line vty 0 4
 transport input ssh
 login local
 access-class 50 in

ip access-list standard 50
 permit 172.20.50.0 0.0.0.255
 deny any
exit

ip ssh version 2
ip ssh authentication-retries 3
ip ssh time-out 60
ip domain-name heh.local
crypto key generate rsa modulus 3072

!
! Désactivation des interfaces web
!
no ip http server
no ip http secure-server

!
! 🔒 Banner de sécurité
!
banner login ^C
🚨 Accès réservé aux administrateurs autorisés. Toute tentative non autorisée sera enregistrée et signalée. 🚨
^C

!
end


```