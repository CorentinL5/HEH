---
created: 2025-02-05
tags:
  - Lessons/School/HEH/Bloc2/Quad2
---
# 📚 Plan de Nommage des Équipements

> **Note créée le _`2025-02-05`_ à _`12:17`_.**

---

## 1. Information du document
### 1.1. Objectif
Ce document définit les règles de nommage des équipements informatiques afin d'assurer une identification claire, cohérente et évolutive.

### 1.2. Contact
Corentin LALLEMENT 
> Mail : corentin.lallement@heh.be  

Haute Ecole en Hainaut,  
> Département des Sciences et Technologies  
> 8A, Avenue Maistriau,  
> 7000 Mons
### 1.3. Confidentialité
Les informations contenues dans ce document sont réservée à un usage interne à la HEH.
### 1.4. Termes et conditions
L'auteur et la HEH n'assument aucune responsabilité pour les erreurs ou omissions dans le contenu de ce document ou de tout document de tiers référencé ou associé, y compris, mais sans s'y limiter, les erreurs typographiques, les inexactitudes ou les informations périmées. Ce document et tous les renseignements qui s'y trouvent sont fournis «tels quels» sans aucune garantie, expresse ou implicite.
### 1.5. Informations sur le Document
Nom du document : `Projet-Cyber1-plan-de-nommage.pdf` 
Version : `Version 1.3`
Niveau de confidentialité : `Utilisation interne à la HEH uniquement`
Auteur du document : `LALLEMENT Corentin` - `240314`
Date de création : `5 Février 2025, 12h17`
Contributeur(s) : `/`
Révisé par : `Mr Mandoux`
Date de dernière révision : `17/03/2025`
Approuvé par : `/`

---

## 2. Structure du Nommage

Chaque nom suit la structure suivante :

```
[GRP]-[TYPE]-[AG/SITE]-[RÔLE]-[E]-[###]
```

### Détails des éléments :

| Élément     | Description                                                                           | Exemple                           |
| ----------- | ------------------------------------------------------------------------------------- | --------------------------------- |
| **GRP**     | Groupe de l'entreprise (**G1**, **G2**)                                               | `G1`, `G2`                        |
| **TYPE**    | Type d’équipement (**SRV**, **SWT**, **PCT**, etc.)                                   | `SRV`, `PRT`, `VPN`               |
| **L**       | Lieu de référence (local, ville, à spécifier au <u>point 5</u>)      | `0`, `1`, `2`, ...|
| **AG/SITE/WAN** | Code de l’agence, du site ou du WAN                                                   | `AG001`, `ST002`, `WN003`         |
| **RÔLE**    | Fonction de l’équipement (deux chiffres)                                              | `01` (AD), `03` (Web), `07` (DB)  |
| **E**       | Environnement (**P**, **D**, **T**)                                                   | `P` (Prod), `D` (Dev), `T` (Test) |
| **###**     | - Numéro unique (3 chiffres)<br>- OU Prénom_Nom du détenteur des périphériques finaux | `001`, `002`, `003`               |

---

## 3. Types d'Équipements

| Type d’Équipement | Code |
|---|---|
|Pare-feu|**FRW**|
|Routeur|**RTR**|
|Switch|**SWT**|
|Serveur|**SRV**|
|Poste utilisateur Fixe|**PCF**|
|Poste utilisateur Mobile|**PCM**|
|Caméra|**CAM**|
|Imprimante|**PRT**|

---
<div style="page-break-after: always;"></div>

## 4. Rôles et Codes Définis

| **RÔLE (deux chiffres uniquement)** | **Description**              |
| ----------------------------------- | ---------------------------- |
| **00**                              | Aucun rôle spécifique        |
| **01**                              | Active Directory (AD)        |
| **02**                              | Serveur SFTP                 |
| **03**                              | Serveur Web                  |
| **04**                              | Serveur FTP                  |
| **05**                              | Serveur Web + FTP            |
| **06**                              | Serveur de fichiers          |
| **07**                              | Serveur base de données (DB) |
| **08**                              | Serveur applicatif           |
| **09**                              | Serveur de sauvegarde        |
| **10**                              | Poste utilisateur            |
| **11**                              | ...            |

---

## 5. Lieu définis par agence/ site /wan

| **AG/ST/WN** | **#** |  **##** | **Description**|
| --- | --- | --- | --- |
| AG | 0 | 01 | Agence 1, HEH local 2/13 |
| ST | 1 | 01 | Agence 1, HEH local 2/13 |
| AG | 0 | 01 | Agence 1, HEH local 2/13 |
| AG | 0 | 01 | Agence 1, HEH local 2/13 |

\# -> 1


## 6. Exemples de Noms

| **Équipement**                   | **Nom**                         | **Description**                                   |
| -------------------------------- | ------------------------------- | ------------------------------------------------------------ |
| Pare-feu principal (AG001)       | `G1-FRW-AG001-00-P-001`         | Pare-feu principal de l'Agence 001 local 2/13                |
| Serveur Active Directory (AG002) | `G1-SRV-WN002-01-P-001`         | Serveur AD de la WAN 002 (Prod) local 2/13                   |
| Serveur Web (ST002)              | `G2-SRV-ST002-03-P-002`         | Serveur Web du Site 002 (Prod) local 2/13                    |
| Serveur FTP (AG003)              | `G1-SRV-AG003-04-P-003`         | Serveur FTP de l'Agence 003 (Prod) local 2/13                |
| Serveur base de données (AG003)  | `G2-SRV-AG003-07-P-002`         | Serveur de base de données de l'Agence 003 (Prod) local 2/13 |
| PC fixe de Jean Dupont (AG001)   | `G1-PCF-AG101-10-P-Jean_Dupont` | Poste utilisateur Fixe de Jean Dupont (Prod) local 2/16      |
| Imprimante principale (AG002)    | `G1-PRT-AG102-00-P-001`         | Imprimante principale de l'Agence 002 (Prod) local 2/16      |

---
<div style="page-break-after: always;"></div>

## 7. Guide pour Ajouter un Nouveau Nom

1. **Déterminer le Groupe** (G1 ou G2 selon l'organisation)
2. **Choisir le Type d’Équipement** (SRV, PRT, VPN…)
3. **Utiliser le Code Agence/Site** (AG001, ST002…)
4. **Sélectionner le Rôle** (Ex : 03 pour un serveur Web)
5. **Spécifier l'Environnement** (P = Prod, D = Dev, T = Test)
6. **Numéroter l'Équipement** (001, 002… selon l'ordre)

**Exemple de création :**

- **Nouveau serveur Web sur le Site 003 (Production)** → `G1-SRV-ST003-03-P-001`
- **Nouvelle imprimante dans l’Agence 005** → `G2-PRT-AG005-00-P-001`

Ce plan de nommage garantit une gestion claire et évolutive des équipements informatiques. 🚀