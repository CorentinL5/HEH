---
created: 2025-03-17
tags:
  - Lessons/School/HEH/Bloc2/Quad2
Auteur: LALLEMENT Corentin - 240314
---

# # 📚  Remise - EXO séance 2 - LALLEMENT Corentin - 240314
> **Création de la note à *`10: 40`* le *`2025-03-17`.***
> Par `LALLEMENT Corentin`, **`240314`**.
---

# 📝 Remise des 3 exercices

---
## **Question 1 : Opérations sur les ensembles**

### **Q1a**

$A = {1, 2, 4, 7}$ et $B = {2, 3, 7, 8}$.

1. **Calcul des opérations sur les ensembles :**
    $A \cup B = \{1, 2, 3, 4, 7, 8\}$
    $A \cap B = \{2, 7\}$
    $A \setminus B = \{1, 4\}$
    $B \setminus A = \{3, 8\}$

2. **Cardinalité de $A \cup B$ :**
    $|A \cup B| = |A| + |B| - |A \cap B|$$
    $|A \cup B| = 4 + 4 - 2 = 6$

3. **Liste des couples de $A \times B$ et sa taille :**
    $A \times B = \{(1,2), (1,3), (1,7), (1,8), (2,2), (2,3), (2,7), (2,8),$
		    $(4,2), (4,3), (4,7), (4,8), (7,2), (7,3), (7,7), (7,8)\}$
    $|A \times B| = 4 \times 4 = 16$

<div style="page-break-after: always;"></div>

## **Question 2 : Lois ensemblistes / preuves**

### **Q2b - Preuve d’une loi de De Morgan**

$(A∪B)^c= A^c \cap B^c \quad \text{ou} \quad (A \cap B)^c = A^c \cup B^c$

1. **Preuve par double inclusion :**
    - $(A \cup B)^c \subseteq A^c \cap B^c$ :
        - Si $x \in (A \cup B)^c$, alors $x \notin A$ et $x \notin B$.
        - => $x \in A^c$ et $x \in B^c$.
        - => $x \in A^c \cap B^c$, inclusion vérifiée.
    - $A^c \cap B^c \subseteq (A \cup B)^c$ :
        - Si $x \in A^c \cap B^c$, alors $x \notin A$ et $x \notin B$.
        - => $x \notin A \cup B$, donc $x \in (A \cup B)^c$.

2. **Exemple d’ensembles concrets :**
    -  $A = {1,2,3}$ et $B = {3,4,5}$ dans un univers $U = {1,2,3,4,5,6}$.
    - $(A \cup B)^c = {6}$ et $A^c \cap B^c = {6}$, ce qui confirme l'égalité.

---

## **Question 3 : Relations / équivalences / ordres**

$u \sim v \iff u \text{ et } v \text{ ont le même nombre de } 1.$

1. **Type de relation** :
    
    - **Réflexivité** : Tout mot $u$ a le même nombre de $1$ que lui-même, donc $u \sim u$.
    - **Symétrie** : Si $u \sim v$, alors $v \sim u$ car le critère est le **nombre** de $1$, indépendamment de l'ordre.
    - **Transitivité** : Si $u \sim v$ et $v \sim w$, alors $u \sim w$ car ils ont le même nombre de $1$.
    - La relation est donc une **relation d'équivalence**.
2. **Correspondance avec les sous-ensembles de ${1, \dots, n}$ :**
    
    - Si un mot de longueur $n$ contient des $1$ à certaines positions, on peut l’associer à un sous-ensemble de ${1, 2, \dots, n}$.
    - **Exemple** :
        - Le mot $10110$ (longueur 5) correspond à l’ensemble ${1,3,4}$ car les $1$ apparaissent aux positions 1, 3 et 4.
    - Chaque **classe d'équivalence** de la relation $\sim$ correspond à un ensemble de positions de $1$.

