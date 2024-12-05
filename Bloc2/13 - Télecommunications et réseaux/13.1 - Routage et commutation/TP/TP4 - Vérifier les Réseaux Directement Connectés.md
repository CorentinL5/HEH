# TP4 - Vérifier les Réseaux Directement Connectés

## Partie 1 : Vérifier les réseaux IPv4 directement connectés

### **Étape 1 : Vérifier les adresses IPv4 et l’état du port sur R1**

#### a. Vérifiez l’état des interfaces configurées :
```bash
R1# show ip interface brief | exclude unassigned
````

#### b. Corrigez les problèmes d’état du port si nécessaire :

- Si des interfaces sont administrativement désactivées, utilisez :
    
    ```bash
    R1(config)# interface [interface_id]
    R1(config-if)# no shutdown
    ```
    

#### c. Vérifiez les adresses IP configurées sur R1 :

- Comparez avec la table d’adressage et corrigez si nécessaire :
    
    ```bash
    R1(config)# interface [interface_id]
    R1(config-if)# ip address [correct_ip] [subnet_mask]
    ```
    

#### d. Affichez la table de routage par filtrage :

```bash
R1# show ip route | begin Gateway
```

**Question :** Quelle est l’adresse de la passerelle de dernier recours ?

#### e. Affichez les informations d’interface pour Description ou Connexion :

```bash
R1# show interface | include Desc|conn
```

**Question :** Quel est l’ID de circuit affiché ?

#### f. Vérifiez le paramètre duplex, la vitesse et le type de support pour l’interface G0/0/0 :

```bash
R1# show interface g0/0/0 | include duplex
```

**Question :** Quels sont le paramètre duplex, la vitesse et le type de support ?

---

### **Étape 2 : Vérifiez la connectivité**

1. Depuis **PC1**, exécutez un ping vers :
    
    - **PC2** : `ping 172.16.20.138`
    - **Serveur Dual Stack** : `ping [IP_du_Serveur]`
2. Si le ping échoue :
    
    - Vérifiez l’état des interfaces sur R1 :
        
        ```bash
        R1# show ip interface brief
        ```
        
    - Confirmez les adresses IP des périphériques.

---

## Partie 2 : Vérifier les réseaux IPv6 directement connectés

### **Étape 1 : Vérifier les adresses IPv6 et l’état du port sur R2**

#### a. Vérifiez l’état des interfaces configurées :

```bash
R2# show ipv6 interface brief
```

**Question :** Quel est l’état des interfaces configurées ?

#### b. Corrigez les adresses IPv6 incorrectes :

- Supprimez l’adresse IPv6 incorrecte sur une interface :
    
    ```bash
    R2(config)# interface g0/0/1
    R2(config-if)# no ipv6 address 2001:db8:c0de:14::1/64
    ```
    
- Configurez l’adresse correcte :
    
    ```bash
    R2(config-if)# ipv6 address 2001:db8:c0de:13::1/64
    ```
    

#### c. Affichez la table de routage IPv6 :

```bash
R2# show ipv6 route
```

#### d. Affichez tous les adressages IPv6 configurés :

```bash
R2# show running-config | include ipv6|interface
```

**Question :** Combien d’adresses sont configurées sur chaque interface Gigabit ?

---

### **Étape 2 : Vérifiez la connectivité**

1. Depuis **PC3**, exécutez un ping vers :
    
    - **PC4** : `ping 2001:db8:c0de:13::a`
    - **Serveur Dual Stack** : `ping [IP_du_Serveur]`
2. Si le ping échoue :
    
    - Vérifiez l’état des interfaces sur R2 :
        
        ```bash
        R2# show ipv6 interface brief
        ```
        
    - Confirmez les adresses IPv6 des périphériques.

---