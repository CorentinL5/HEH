# TP 3 : Configuration des Interfaces de Routeur

## Partie 1 : Configuration de l’adressage IPv4

### **Étape 1 : Configurer les adresses IPv4**

#### Configuration de R1
```ps1
enable
configure terminal
interface g0/0
ip address 172.16.20.1 255.255.255.128
no shutdown
exit
interface g0/1
ip address 172.16.20.129 255.255.255.128
no shutdown
exit
````

#### Configuration de PC1

1. Ouvrir la configuration IP de PC1.
2. Saisir :
    - Adresse IP : `172.16.20.10`
    - Masque de sous-réseau : `255.255.255.128`
    - Passerelle par défaut : `172.16.20.1`

#### Configuration de PC2

1. Ouvrir la configuration IP de PC2.
2. Saisir :
    - Adresse IP : `172.16.20.138`
    - Masque de sous-réseau : `255.255.255.128`
    - Passerelle par défaut : `172.16.20.129`

### **Étape 2 : Vérifier la connectivité**

1. Tester la connectivité avec la commande `ping` depuis :
    - **PC1** vers **PC2**.
    - **PC2** vers le serveur Dual Stack.

---

## Partie 2 : Configuration de l’adressage IPv6

### **Étape 1 : Configurer les adresses IPv6**

#### Configuration de R2

```bash
enable
configure terminal
interface g0/0
ipv6 address 2001:db8:c0de:12::1/64
no shutdown
exit
interface g0/1
ipv6 address 2001:db8:c0de:13::1/64
no shutdown
exit
interface s0/0/1
ipv6 address fe80::2 link-local
no shutdown
exit
```

#### Configuration de PC3

1. Ouvrir la configuration IPv6 de PC3.
2. Saisir :
    - Adresse IP : `2001:db8:c0de:12::a/64`
    - Passerelle par défaut : `fe80::2`

#### Configuration de PC4

1. Ouvrir la configuration IPv6 de PC4.
2. Saisir :
    - Adresse IP : `2001:db8:c0de:13::a/64`
    - Passerelle par défaut : `fe80::2`

### **Étape 2 : Vérifier la connectivité**

1. Tester la connectivité avec la commande `ping` depuis :
    - **PC3** vers **PC4**.
    - **PC4** vers le serveur Dual Stack.

---
