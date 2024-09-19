# Configuration du réseau

## Tâche 1: Configuration des adresses et des noms d'hôtes

### Configuration des noms d'hôtes des routeurs

1. **Accéder au mode privilégié :**
    ```plaintext
    enable
    ```

2. **Accéder au mode de configuration globale :**
    ```plaintext
    configure terminal
    ```

3. **Configurer les noms d'hôtes :**
    ```plaintext
    hostname R1
    ```

    ```plaintext
    hostname R2
    ```

    ```plaintext
    hostname R3
    ```

### Configuration des adresses IP des interfaces des routeurs

Pour R1 :
```plaintext
interface FastEthernet0/0
 ip address 172.20.3.254 255.255.252.0
 no shutdown
 exit

interface FastEthernet1/0
 ip address 172.20.6.2 255.255.255.252
 no shutdown
 exit

interface FastEthernet2/0
 ip address 172.20.4.254 255.255.255.0
 no shutdown
 exit

```

Pour R2 :
```plaintext
en
conf t
hostname R2

interface FastEthernet2/0
 ip address 172.20.5.126 255.255.255.128
 no shutdown
 exit

interface FastEthernet0/0
 ip address 172.20.6.6 255.255.255.252
 no shutdown
 exit

interface FastEthernet1/0
 ip address 172.20.6.1 255.255.255.252
 no shutdown
 exit

```

Pour R3 :
```plaintext
en
conf t
hostname R3

interface GigabitEthernet8/0
 ip address 172.20.6.5 255.255.255.252
 no shutdown
 exit

interface GigabitEthernet9/0
 ip address 172.20.5.254 255.255.255.128
 no shutdown
 exit

```

## Tâche 2: Configuration du routeur R1

1. **Accéder au mode privilégié :**
    ```plaintext
    enable
    ```

2. **Accéder au mode de configuration globale :**
    ```plaintext
    configure terminal
    ```

3. **Configurer le mot de passe secret chiffré :**
    ```plaintext
    enable secret cisco
    ```

4. **Activer le chiffrement des mots de passe :**
    ```plaintext
    service password-encryption
    ```

5. **Configurer le mot de passe pour la ligne de console :**
    ```plaintext
    line console 0
     password cisco
     login
     exit
    ```

6. **Configurer le mot de passe pour les lignes VTY :**
    ```plaintext
    line vty 0 4
     password cisco
     login
     exit
    ```

7. **Configurer la bannière :**
    ```plaintext
    banner motd #RESTRICTED#
    ```

8. **Blocage des tentatives de connexion infructueuses :**
    ```plaintext
    login block-for 300 attempts 3 within 120
    ```

- **Code Final :**
en
conf t
enable secret cisco
service password-encryption
line console 0
 password cisco
 login
 exit
line vty 0 4
 password cisco
 login
 exit
banner motd `#RESTRICTED#`
login block-for 300 attempts 3 within 120 * not working


## Tâche 3: Configuration des commutateurs

### Configuration de SW4 pour administration SSH depuis PC1

1. **Accéder au mode privilégié :**
    ```plaintext
    enable
    ```

2. **Accéder au mode de configuration globale :**
    ```plaintext
    configure terminal
    ```

3. **Configurer le nom d'hôte :**
    ```plaintext
    hostname SW4
    ```

4. **Configurer le nom de domaine :**
    ```plaintext
    ip domain-name examen.juin
    ```

5. **Générer les clés RSA :**
    ```plaintext
    crypto key generate rsa
     1024
    ```

6. **Configurer le nom d'utilisateur et le mot de passe :**
    ```plaintext
    username admin secret cisco
    ```

7. **Configurer les lignes VTY pour SSH :**
    ```plaintext
    line vty 0 4
     login local
     transport input ssh
     exit
    ```

8. **Configurer l'interface VLAN pour la gestion :**
    ```plaintext
    interface vlan 1
     ip address [SW4_IP_Address] [Subnet_Mask]
     no shutdown
     exit
    ```


### Mappage statique pour SRV01 sur SW2

1. **Accéder au mode privilégié :**
    ```plaintext
    enable
    ```

2. **Accéder au mode de configuration globale :**
    ```plaintext
    configure terminal
    ```

3. **Configurer le mappage statique :**
    ```plaintext
    mac address-table static [SRV01_MAC_Address] vlan [VLAN_ID] interface [Interface_ID]
    ```

## Tâche 4: Configuration des routes statiques IPv4

### Routes statiques sur R1

1. **Accéder au mode privilégié :**
    ```plaintext
    enable
    ```

2. **Accéder au mode de configuration globale :**
    ```plaintext
    configure terminal
    ```

3. **Configurer les routes statiques :**
    ```plaintext
    ip route 192.168.5.0 255.255.255.128 172.20.6.1
    ip route 192.168.5.128 255.255.255.128 172.20.6.1
    ```
en
conf t
ip route 172.20.5.0 255.255.255.128 172.20.5.126
ip route 172.20.5.128 255.255.255.128 172.20.6.6


### Routes statiques sur R2

1. **Accéder au mode privilégié :**
    ```plaintext
    enable
    ```

2. **Accéder au mode de configuration globale :**
    ```plaintext
    configure terminal
    ```

3. **Configurer les routes statiques :**
    ```plaintext
    ip route 192.168.1.0 255.255.255.0 192.168.2.1
    ip route 192.168.4.0 255.255.255.0 192.168.3.2
    ```

### Route statique par défaut sur R3

1. **Accéder au mode privilégié :**
    ```plaintext
    enable
    ```

2. **Accéder au mode de configuration globale :**
    ```plaintext
    configure terminal
    ```

3. **Configurer la route statique par défaut :**
    ```plaintext
    ip route 0.0.0.0 0.0.0.0 192.168.3.1
    ```

## Tâche 5: Configuration du routage IPv6

### Configuration des interfaces sur R1 et R2 avec IPv6

Pour R1 :
```plaintext
interface FastEthernet0/0
 ipv6 address 2001::1:172:0:0:1/64
 no shutdown
 exit

interface FastEthernet1/0
 ipv6 address 2001::2:172:0:0:2/64
 no shutdown
 exit
```

Pour PC1 :
```plaintext
ipv6 address 2001::1:172:0:0:2/64
```

Pour R2 :
```plaintext
interface FastEthernet1/0
 ipv6 address 2001::2:172:0:0:229/64
 no shutdown
 exit
```

### Route statique par défaut pour IPv6 sur R1

1. **Accéder au mode privilégié :**
    ```plaintext
    enable
    ```

2. **Accéder au mode de configuration globale :**
    ```plaintext
    configure terminal
    ```

3. **Configurer la route statique par défaut :**
    ```plaintext
    ipv6 route ::/0 2001::2:172:0:0:229
    ```