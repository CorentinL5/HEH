---
created: 2025-04-01
tags:
  - Lessons/School/HEH/BlocX/QuadX
Auteur: LALLEMENT Corentin - 240314
---

# # 📚  Projet-Cyber1-plan-de-nommage-VDOM
> Par `LALLEMENT Corentin`, **`240314`**.
---


## 📐 **Plan de Nommage du VDOM (avec code d'admin égal au code d'agence le plus bas)**

### **Structure** 

```
VDM-[RÔLE][CODE]
```

### ✅ **Explication des éléments** :

- **RÔLE** : Définit le rôle, soit un **admin** (ADM), soit une **agence** (AG).
    
- **CODE** : Le code **de l'agence la plus basse** devient également le code de l'admin associé.
    
    - **ADM001** aura le même code que **AG001**.
        
    - **ADM002** aura le même code que **AG002**, et ainsi de suite.
        

---

### ✨ **Exemples de Noms**

#### **1. Admins**

| **Nom**      | **Description**                                    |
| ------------ | -------------------------------------------------- |
| `VDM-ADM001` | Admin avec le code **ADM001**, associé à **AG001** |
| `VDM-ADM002` | Admin avec le code **ADM002**, associé à **AG002** |
| `VDM-ADM003` | Admin avec le code **ADM003**, associé à **AG003** |

#### **2. Agences**

| **Nom**     | **Description**               |
| ----------- | ----------------------------- |
| `VDM-AG001` | Agence avec le code **AG001** |
| `VDM-AG002` | Agence avec le code **AG002** |
| `VDM-AG003` | Agence avec le code **AG003** |
