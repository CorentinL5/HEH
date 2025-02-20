---
created: 2025-02-16
tags:
  - Lessons/School/HEH/Bloc2/Quad2
Auteur: LALLEMENT Corentin - 240314
---

# 📚  EX - Opérations primitives - Tris
> **Création de la note à *`15:54`* le *`2025-02-16`.***
> Par `LALLEMENT Corentin`, **`240314`**.
---

## 🫧 **Tri à bulles**
![[Pasted image 20250218210014.png]]

```
pour i allant de (taille de T) - 1 à 1
```

- **Initialisation** : 1 opération
- **Comparaison (i >= 1)** : (n-1) fois
- **Décrémentation (i = i - 1)** : (n-1) fois
- **Total** : **2n - 1**

---

```
pour j allant de 0 à i - 1
```

- **Initialisation** : (n-1) fois
- **Comparaison (j < i-1)** : exécutée `i` fois par tour de `i`
- **Incrémentation (j = j + 1)** : exécutée `i` fois par tour de `i`
- **Total** : **n² - n**

---

```
si T[j+1] < T[j]
```

- **Comparaison** : exécutée `i` fois par tour de `i`
- **Total** : **n² - n**

---

```
(T[j+1], T[j]) ← (T[j], T[j+1])
```

- **3 affectations** (échange avec variable temporaire)
- **Exécutée autant de fois que la condition est vraie** (au pire `n² - n` fois)
- **Total** : **3(n² - n)**

---

### **Total des opérations pour le tri à bulles**

#### **Meilleur cas (0 échanges, tableau déjà trié)**
- **2n - 1** (boucle `i`)
- **n² - n** (boucle `j`)
- **n² - n** (comparaisons)
- **0 échanges**
> **Total = `2n² - 2n + 2n - 1`**  
> **Total simplifié = `2n² - 1` → O(n²)**

#### **Cas moyen (moitié des échanges)**
- **2n - 1** (boucle `i`)
- **n² - n** (boucle `j`)
- **n² - n** (comparaisons)
- **1.5(n² - n)** (moitié des échanges)
> **Total = `2n² - 2n + 1.5n² - 1.5n + 2n - 1`**  
> **Total simplifié = `3.5n² - 1.5n - 1` → O(n²)**

#### **Pire cas (tous les échanges, tableau inversé)**
- **2n - 1** (boucle `i`)
- **n² - n** (boucle `j`)
- **n² - n** (comparaisons)
- **3(n² - n)** (tous les échanges)
> **Total = `2n² - 2n + 3n² - 3n + 2n - 1`**  
> **Total simplifié = `5n² - 3n - 1` → O(n²)**

<div style="page-break-after: always;"></div>

## 💘**Tri par insertion**
![[Pasted image 20250218210008.png]]

```
pour i de 1 à taille(T) - 1
```

- **Initialisation** : 1 opération
- **Comparaison (i ≤ n-1)** : (n-1) fois
- **Incrémentation (i = i + 1)** : (n-1) fois
- **Total** : **2n - 1**

---

```
x ← T[i]
```

- **1 affectation**
- **Exécutée (n-1) fois**
- **Total** : **n - 1**

---

```
j ← i
```

- **1 affectation**
- **Exécutée (n-1) fois**
- **Total** : **n - 1**

---

```
tant que j > 0 et T[j - 1] > x
```

- **Comparaison** : exécutée jusqu’à `i` fois dans le pire cas
- **Total** : **n² - n**

---

```
T[j] ← T[j - 1]
```

- **1 affectation**
- **Exécutée autant de fois que la condition est vraie** (jusqu’à `i` fois)
- **Total** : **n² - n**

---

```
j ← j - 1
```

- **1 décrémentation**
- **Exécutée autant de fois que la condition est vraie** (jusqu’à `i` fois)
- **Total** : **n² - n**

---

```
T[j] ← x
```

- **1 affectation**
- **Exécutée (n-1) fois**
- **Total** : **n - 1**

<div style="page-break-after: always;"></div>

### **Total des opérations pour le tri par insertion**

#### **Meilleur cas (déjà trié, aucun décalage)**

- **2n - 1** (boucle `i`)
- **n - 1** (`x ← T[i]`)
- **n - 1** (`j ← i`)
- **n - 1** (comparaisons `tant que`)
- **n - 1** (aucun décalage `T[j] ← T[j-1]`)
- **n - 1** (aucun décrémentation `j ← j - 1`)
- **n - 1** (`T[j] ← x`)
> **Total = `7n - 1` → O(n)**

---

#### **Cas moyen (environ moitié des décalages)**

- **2n - 1** (boucle `i`)
- **n - 1** (`x ← T[i]`)
- **n - 1** (`j ← i`)
- **n²/2 - n/2** (comparaisons `tant que`)
- **n²/2 - n/2** (décalages `T[j] ← T[j-1]`)
- **n²/2 - n/2** (décrémentations `j ← j - 1`)
- **n - 1** (`T[j] ← x`)
> **Total = `1.5n² - 3n - 1` → O(n²)**

---

#### **Pire cas (tout est inversé, décalage maximal)**

- **2n - 1** (boucle `i`)
- **n - 1** (`x ← T[i]`)
- **n - 1** (`j ← i`)
- **n² - n** (comparaisons `tant que`)
- **n² - n** (décalages `T[j] ← T[j-1]`)
- **n² - n** (décrémentations `j ← j - 1`)
- **n - 1** (`T[j] ← x`)
> **Total = `3n² - 3n - 1` → O(n²)**

<div style="page-break-after: always;"></div>

## **Comparaison des complexités**

| **Algo**              | **Meilleur cas (déjà trié)** | **Moyen cas** | **Pire cas (ordre inversé)** |
| --------------------- | ---------------------------- | ------------- | ---------------------------- |
| **Tri à bulles**      | O(n²)                        | O(n²)         | O(n²)                        |
| **Tri par insertion** | O(n)                         | O(n²)         | O(n²)                        |
