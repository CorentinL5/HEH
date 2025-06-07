---
created: 2025-04-01
tags:
  - Lessons/School/HEH/Bloc2/Quad2
Auteur: LALLEMENT Corentin - 240314
---
# 📚 Plan de Nommage des Noms de Domaine

---

## 1. Information du document

### 1.1. Objectif
Ce document définit les règles de nommage des noms de domaines afin d'assurer une identification claire, cohérente et évolutive des services réseau internes et publics de la HEH.

### 1.2. Contact
Corentin LALLEMENT  
> Mail : corentin.lallement@heh.be

Haute École en Hainaut  
> Département des Sciences et Technologies  
> 8A, Avenue Maistriau,  
> 7000 Mons

### 1.3. Confidentialité
Les informations contenues dans ce document sont réservées à un usage interne à la HEH.

### 1.4. Termes et conditions
L'auteur et la HEH n'assument aucune responsabilité pour les erreurs ou omissions dans le contenu de ce document ou de tout document de tiers référencé ou associé, y compris, mais sans s'y limiter, les erreurs typographiques, les inexactitudes ou les informations périmées. Ce document et tous les renseignements qui s'y trouvent sont fournis « tels quels » sans aucune garantie, expresse ou implicite.

### 1.5. Informations sur le Document
- **Nom du document** : `Projet-Cyber1-plan-de-nommage-domaines.md`  
- **Version** : `Version 1.0`  
- **Niveau de confidentialité** : `Utilisation interne à la HEH uniquement`  
- **Auteur** : `LALLEMENT Corentin` - `240314`  
- **Date de création** : `1er Avril 2025`  
- **Révisé par** : `/`  
- **Date de dernière révision** : `/`  
	- **Approuvé par** : `/` 

---

## 2. Structure du nom de domaine

Les noms de domaines suivent la structure suivante :

```yml
[service].[site].heh.local  ← Domaine interne 
[service].[site].heh.be     ← Domaine public
```

---

## 3. Détail des éléments

| Élément     | Description                                          | Exemple            |
| ----------- | ---------------------------------------------------- | ------------------ |
| `service`   | Nom court du service (web, mail, sftp, ad, db, etc.) | `web`, `ftp`, `db` |
| `site`      | Code du site, agence ou WAN                          | `st008`, `ag009`   |
| `heh.local` | Domaine interne (non routable, DNS privé)            | —                  |
| `heh.be`    | Domaine public (routable, DNS externe)               | —                  |

---

## 4. Liste des sites

| **Code** | **Lieu**                   |
| -------- | -------------------------- |
| ST008    | Site 8, HEH local 2/16     |
| AG009    | Agence 9, HEHE local 2/16  |
| AG012    | Agence 12, HEHE local 2/16 |

---

## 5. Exemples généraux

| **Service**           | **Nom interne**        | **Nom public**      |
| --------------------- | ---------------------- | ------------------- |
| Serveur Web site 8    | `web.st008.heh.local`  | `web.st008.heh.be`  |
| Serveur AD interne    | `ad.st008.heh.local`   | —                   |
| FTP Agence 9          | `ftp.ag009.heh.local`  | `ftp.ag009.heh.be`  |
| BDD WAN               | `db.wn001.heh.local`   | —                   |
| SFTP public Agence 12 | `sftp.ag012.heh.local` | `sftp.ag012.heh.be` |

---

## 6. Noms pour Switchs & Accès SSH

### 6.1. Switchs

| **Équipement** | **Nom interne**          | **Remarques**                          |
| -------------- | ------------------------ | -------------------------------------- |
| Switch L2      | `SWT201.st003.heh.local` | Premier switch de niveau 2, site 3     |
| Switch L3      | `SWT303.ag009.heh.local` | Troisième switch de niveau 3, agence 9 |


### 6.2. Accès SSH

| **Accès SSH** | **Nom de domaine**               | **Remarques**           |
| ------------- | -------------------------------- | ----------------------- |
| SSH vers AD   | `ssh.ad.st008.heh.local`         | Accès SSH interne       |
| SSH générique | `ssh.<service>.<site>.heh.local` | Préfixe standardisé SSH |

---

## 7. Règles de nommage

- ✅ Tous les noms en **minuscules**, sans accent ni caractère spécial.
- ✅ Pas d’espace, pas de majuscules, pas d’underscore.
- ✅ `site` **obligatoire**, avec code officiel (`st008`, `ag009`, etc.).
- ✅ `heh.local` réservé à l’**interne uniquement**.
- ✅ `heh.be` réservé aux services **publics uniquement**.
- ❌ Ne jamais exposer des équipements sensibles (switchs, ssh, AD…) en `.heh.be`.

---

## 8. Mauvais exemples à éviter

| **Nom**                  | **Pourquoi c’est mauvais**             |
|--------------------------|----------------------------------------|
| `web2.local`             | Pas de site défini                     |
| `Serveur-AD.st008.local` | Trop verbeux, majuscules, mélange fr/en|
| `mailST008.heh.local`    | Majuscules                             |
| `192.168.1.5.local`      | Utilisation d’une IP = pas maintenable |

---

## 9. Pourquoi deux domaines ?

| **Domaine**     | **Usage**     | **Visible sur Internet ?** | **Exemple**                 |
|-----------------|---------------|-----------------------------|-----------------------------|
| `.heh.local`    | Interne       | ❌ Non                      | `db.wn001.heh.local`        |
| `.heh.be`       | Public        | ✅ Oui                      | `web.st008.heh.be`          |

### Avantages :

- 🔐 **Sécurité** : les services sensibles restent internes.
- 🧭 **Clarté** : les domaines publics et privés sont distincts.
- 🔧 **Administration** : facilite la gestion DNS et les règles firewall.

---

## 10. Guide pour créer un nouveau nom

1. Identifier le **service** → ex : `web`
2. Identifier le **site** → ex : `st008`
3. Choisir le **type de domaine** :
   - Interne → `web.st008.heh.local`
   - Public → `web.st008.heh.be`
4. Respecter les conventions de nommage

---

## ✅ TL;DR

- Deux domaines : `.heh.local` (interne) / `.heh.be` (public)
- Structure : `[service].[site].heh.local/.be`
- Éviter les expos inutiles des services internes
- Exemples corrects :
  - `web.st008.heh.be`
  - `swl2.ag009.heh.local`
  - `ssh.db.wn001.heh.local`

---

