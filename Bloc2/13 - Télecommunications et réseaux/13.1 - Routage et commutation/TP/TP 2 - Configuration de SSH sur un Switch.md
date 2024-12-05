# TP 2 - Configuration de SSH sur un Switch

## Objectifs
1. Sécuriser les mots de passe.
2. Activer le chiffrement des communications avec SSH.
3. Vérifier l'implémentation de SSH.

---

## Table d’adressage

| Appareil | Interface | Adresse IP  | Masque de sous-réseau |
|----------|-----------|-------------|-----------------------|
| S1       | VLAN 1    | 10.10.10.2  | 255.255.255.0         |
| PC1      | Carte réseau | 10.10.10.10 | 255.255.255.0        |

---

## Étapes

### **Partie 1 : Mots de passe sécurisés**

#### Étape 1 : Telnet à partir de PC1
1. Sur **PC1**, ouvrez l'invite de commandes et tapez :
   ```bash
   telnet 10.10.10.2
```

2. Entrez le mot de passe `cisco` pour accéder au mode EXEC utilisateur.

#### Étape 2 : Sauvegarder la configuration actuelle

1. Passez en mode privilégié :
    
    ```bash
    enable
    ```
    
    - Mot de passe EXEC privilégié : `cisco`.
2. Sauvegardez la configuration :
    
    ```bash
    copy running-config startup-config
    ```
    

#### Étape 3 : Crypter les mots de passe

1. Accédez au mode configuration globale :
    
    ```bash
    configure terminal
    ```
    
2. Cryptez les mots de passe :
    
    ```bash
    service password-encryption
    ```
    
3. Vérifiez que les mots de passe sont cryptés :
    
    ```bash
    show running-config
    ```
    

---

### **Partie 2 : Chiffrement des communications**

#### Étape 1 : Configurer le nom de domaine et générer des clés sécurisées

1. Définir le nom de domaine :
    
    ```bash
    ip domain-name netacad.pka
    ```
    
2. Générer des clés RSA :
    
    ```bash
    crypto key generate rsa
    ```
    
    - Lorsque demandé, entrez `1024` comme longueur de clé.

#### Étape 2 : Créer un utilisateur SSH et configurer les lignes VTY

1. Créez un utilisateur administrateur avec mot de passe secret :
    
    ```bash
    username admin secret cisco
    ```
    
2. Configurez les lignes VTY pour n’autoriser que SSH :
    
    ```bash
    line vty 0 4
    login local
    transport input ssh
    no password
    ```
    

---

### **Partie 3 : Vérification de l’implémentation de SSH**

#### Étape 1 : Tester la connexion Telnet

1. Déconnectez vous de la session Telnet :
    
    ```bash
    exit
    ```
    
2. Essayez de vous reconnecter via Telnet :
    
    ```bash
    telnet 10.10.10.2
    ```
    
    - Résultat attendu : **La connexion doit échouer.**

#### Étape 2 : Tester la connexion SSH

1. Sur **PC1**, connectez-vous en utilisant SSH :
    
    ```bash
    ssh -l admin 10.10.10.2
    ```
    
2. Entrez le mot de passe de l’utilisateur `admin` : `cisco`.

#### Étape 3 : Sauvegarder la configuration

1. Passez en mode EXEC privilégié après la connexion :
    
    ```bash
    enable
    ```
    
    - Mot de passe EXEC privilégié : `cisco`.
2. Sauvegardez la configuration finale :
    
    ```bash
    copy running-config startup-config
    ```
    

---

## Résultats attendus

1. **Telnet** : Échec de connexion.
2. **SSH** : Connexion réussie avec l'utilisateur `admin`.
3. **Configuration** : Les modifications sont sauvegardées et permanentes.

---