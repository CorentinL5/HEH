---
created: 2025-02-16
tags:
  - Lessons/School/HEH/Bloc2/Quad2
Auteur: LALLEMENT Corentin - 240314
---

# # 📚  Synthese - Calcul de complexité
> **Création de la note à *`15:38`* le *`2025-02-16`.***
> Par `LALLEMENT Corentin`, **`240314`**.
---

# **Synthèse - Complexité des algorithmes de tri**

## **1️⃣ Notions de base**

- **n** : nombre d'éléments dans le tableau
- **n - 1** : opérations faites une seule fois par boucle principale
- **n² - n** : opérations faites plusieurs fois dans la boucle interne (`j`)
- **n log n** : complexité plus efficace utilisée par les **tris avancés**
- **Complexité O()** : notation qui montre la vitesse de l’algorithme

---

## **2️⃣ Tri à bulles**

- Compare chaque paire d’éléments et les échange si nécessaire
- Deux boucles imbriquées :
    - **Boucle `i` (externe) : n - 1 fois**
    - **Boucle `j` (interne) : jusqu’à n² - n au total**

**Opérations comptées :**

- Comparaisons : **n² - n**
- Échanges (si tableau inversé) : **3(n² - n)**

|Cas|Comparaisons|Échanges|Total|O()|
|---|---|---|---|---|
|**Meilleur cas** (déjà trié)|**n² - n**|**0**|**2n² - 1**|**O(n²)**|
|**Moyen cas** (moitié des échanges)|**n² - n**|**1.5(n² - n)**|**3.5n² - 1.5n - 1**|**O(n²)**|
|**Pire cas** (ordre inverse)|**n² - n**|**3(n² - n)**|**5n² - 3n - 1**|**O(n²)**|

⚠ **Toujours lent pour les grands tableaux, même dans le meilleur cas.**

---

## **3️⃣ Tri par insertion**

- Prend un élément et le place à la bonne position en décalant les autres
- Deux boucles imbriquées :
    - **Boucle `i` (externe) : n - 1 fois**
    - **Boucle `j` (interne) : varie selon l’ordre du tableau**

**Opérations comptées :**

- Comparaisons : **n² - n** (pire cas)
- Décalages : **n² - n** (pire cas)

|Cas|Comparaisons|Décalages|Total|O()|
|---|---|---|---|---|
|**Meilleur cas** (déjà trié)|**n - 1**|**0**|**7n - 1**|**O(n)**|
|**Moyen cas** (moitié des décalages)|**n²/2 - n/2**|**n²/2 - n/2**|**1.5n² - 3n - 1**|**O(n²)**|
|**Pire cas** (ordre inverse)|**n² - n**|**n² - n**|**3n² - 3n - 1**|**O(n²)**|

⚠ **Bon choix si le tableau est déjà presque trié, mais lent si tout est en désordre.**

---

## **4️⃣ Comparaison avec les tris en `O(n log n)`**

Les **tris avancés** comme **quicksort** et **mergesort** sont bien meilleurs car ils tournent en **O(n log n)**, ce qui est **beaucoup plus rapide que O(n²)**.

| Algo                       | Meilleur cas   | Moyen cas      | Pire cas       |
| -------------------------- | -------------- | -------------- | -------------- |
| **Tri à bulles**           | **O(n)**       | **O(n²)**      | **O(n²)**      |
| **Tri par insertion**      | **O(n)**       | **O(n²)**      | **O(n²)**      |
| **Tri rapide (quicksort)** | **O(n log n)** | **O(n log n)** | **O(n²)**      |
| **Tri fusion (mergesort)** | **O(n log n)** | **O(n log n)** | **O(n log n)** |

✅ **O(n log n) est bien plus efficace que O(n²), surtout quand n devient grand**.  
⚡ **Si beaucoup d’éléments à trier, toujours préférer quicksort ou mergesort !**