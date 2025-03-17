---
created: 202503-17
tags:
  - Lessons/School/HEH/Bloc2/Quad2
Auteur: LALLEMENT Corentin - 240314
---

# # 📚  EXO 2 - Exercices
> 	**Création de la note à *`10:37`* le *`2025-03-17`.***
> Par `LALLEMENT Corentin`, **`240314`**.

---

## **Question 1 : Opérations sur les ensembles**

### **Q1a**

Soient $A = {1, 2, 4, 7} $ et $ B = {2, 3, 7, 8}$.

1. **Calcul des opérations sur les ensembles :**
    
    $A \cup B = \{1, 2, 3, 4, 7, 8\}$
    $A \cap B = \{2, 7\}$
    $A \setminus B = \{1, 4\}$
    $B \setminus A = \{3, 8\}$
2. **Vérification de la cardinalité de $ A \cup B $ :**
    
    $|A \cup B| = |A| + |B| - |A \cap B|$$
    $|A \cup B| = 4 + 4 - 2 = 6$
3. **Liste des couples de $ A \times B $ et sa taille :**
    
    $A \times B = \{(1,2), (1,3), (1,7), (1,8), (2,2), (2,3), (2,7), (2,8),$
		    $(4,2), (4,3), (4,7), (4,8), (7,2), (7,3), (7,7), (7,8)\}$
    $|A \times B| = 4 \times 4 = 16$

---

### **Q1b**

On se place dans l’univers $U = {0, 1, 2, 3, 4, 5, 6, 7, 8}$.  
On définit :

A={0,1,2,3},B={2,4,5},C={1,2,4,7}A = \{0, 1, 2, 3\}, \quad B = \{2, 4, 5\}, \quad C = \{1, 2, 4, 7\}

1. **Calculs :**
    
    $(A \cup B) \cap C = \{0,1,2,3,4,5\} \cap \{1,2,4,7\} = \{1,2,4\}$
    $(A \cap B) \setminus C = (\{2\} \setminus \{1,2,4,7\}) = \emptyset$
    $(B \cup C)^c = U \setminus (B \cup C) = \{0,3,6,8\}$
2. **Vérification de l’identité**
    
    $(A \cup B) \cap C = (A \cap C) \cup (B \cap C)$
    - L'égalité est bien vérifiée.
3. **Test de $ (A \cap B) \subseteq C $**
    
	$A \cap B = \{2\} \quad \text{et} \quad C = \{1,2,4,7\}$
	$(A∩B)⊆C(Vrai)(A \cap B) \subseteq C \quad \text{(Vrai)}$

---

### **Q1c**

On a :

X = \{a, b, c\}, \quad Y = \{1, 2, 3, 4\}$

1. **Calcul explicite de $X \times Y$ :**
    
    $X \times Y = \{(a,1), (a,2), (a,3), (a,4), (b,1), (b,2), (b,3), (b,4), (c,1), (c,2), (c,3), (c,4)\}$
2. **Exemple d’un sous-ensemble $ R \subseteq X \times Y $ qui n’est pas une fonction de $ X $ vers $ Y $**
    
    $R={(a,1),(a,2),(b,3)}$R = \{(a,1), (a,2), (b,3)\}$
    - Ici, $ a $ est associé à deux valeurs différentes, donc $ R $ n’est **pas une fonction**.
3. **Exemple d’un sous-ensemble $F \subseteq X \times Y$ injectif mais pas surjectif (ou l’inverse)**
    
    - **Injectif mais pas surjectif** :
        
        $F={(a,1),(b,2),(c,3)}$F = \{(a,1), (b,2), (c,3)\}$
        - Chaque élément de $X$ a une image distincte dans $Y$, donc **injectif**.
        - Mais $4$ n’est jamais atteint, donc **pas surjectif**.
    - **Surjectif mais pas injectif** :
        
        $F = \{(a,1), (b,2), (b,3), (c,4)\}$
        - Tous les éléments de $Y$ sont atteints, donc **surjectif**.
        - Mais $b$ a deux images (2 et 3), donc **pas injectif**.


---

## **Question 2 : Lois ensemblistes / preuves**

### **Q2a - Preuve de l'égalité**

Prouvons :

$(A \setminus B) \cup (A \cap B) = A$

1. **Preuve par double inclusion :**
    
    - Montrons que $(A \setminus B) \cup (A \cap B) \subseteq A$ :
        - Si $x \in (A \setminus B)$, alors $x \in A$ et $x \notin B$.
        - Si $x \in (A \cap B)$, alors $x \in A$ et $x \in B$.
        - Dans tous les cas, $x \in A$, donc l'inclusion est vérifiée.
    - Montrons que $A \subseteq (A \setminus B) \cup (A \cap B)$ :
        - Si $x \in A$, alors deux possibilités :
            - Soit $x \in B$ donc $x \in A \cap B$.
            - Soit $x \notin B$ donc $x \in A \setminus B$.
        - Dans tous les cas, $x \in (A \setminus B) \cup (A \cap B)$, donc l'inclusion est vérifiée.
2. **Interprétation** :
    
    - Un élément de $A$ est soit dans $B$, soit en dehors de $B$, ce qui couvre toutes les possibilités.

---

### **Q2b - Preuve d’une loi de De Morgan**

Prouvons l’une des identités suivantes :

$(A∪B)^c= A^c \cap B^c \quad \text{ou} \quad (A \cap B)^c = A^c \cup B^c$

1. **Preuve par double inclusion :**
    
    - Montrons que $(A \cup B)^c \subseteq A^c \cap B^c$ :
        - Si $x \in (A \cup B)^c$, alors $x \notin A$ et $x \notin B$.
        - Donc, $x \in A^c$ et $x \in B^c$.
        - Donc, $x \in A^c \cap B^c$, inclusion vérifiée.
    - Montrons que $A^c \cap B^c \subseteq (A \cup B)^c$ :
        - Si $x \in A^c \cap B^c$, alors $x \notin A$ et $x \notin B$.
        - Donc, $x \notin A \cup B$, donc $x \in (A \cup B)^c$.
2. **Exemple d’ensembles concrets :**
    
    - Soit $A = {1,2,3}$ et $B = {3,4,5}$ dans un univers $U = {1,2,3,4,5,6}$.
    - On a $(A \cup B)^c = {6}$ et $A^c \cap B^c = {6}$, ce qui confirme l'égalité.

---

### **Q2c - Preuve de la distributivité**

Prouvons :

$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$

1. **Preuve par double inclusion :**
    
    - Montrons que $A \cap (B \cup C) \subseteq (A \cap B) \cup (A \cap C)$ :
        - Si $x \in A \cap (B \cup C)$, alors $x \in A $ et $ x \in B \cup C$.
        - Donc, $x$ est soit dans $B$, soit dans $C$, donc $x$ est dans $(A \cap B) \cup (A \cap C)$.
    - Montrons que $(A \cap B) \cup (A \cap C) \subseteq A \cap (B \cup C)$ :
        - Si $x \in (A \cap B)$, alors $x \in A$ et $x \in B$.
        - Si $x \in (A \cap C)$, alors $x \in A$ et $x \in C$.
        - Dans les deux cas, $x \in A \cap (B \cup C)$, inclusion vérifiée.
2. **Explication intuitive :**
    
    - Un élément est dans $A$ et dans $(B \text{ ou } C)$.
    - Cela signifie qu’il est soit dans $A \cap B$, soit dans $A \cap C$, donc il appartient bien à $(A \cap B) \cup (A \cap C)$.

---

## **Question 3 : Relations / équivalences / ordres**

### **Q3a - Relation d'ordre entre les rôles**

On a une relation définie par :  
$r_1 \leq r_2 \iff Perm(r_1) \subseteq Perm(r_2)$

1. **Déterminer si $\text{"}\leq\text{"}$ est un ordre partiel, une équivalence ou aucun des deux :**
    
    - **Réflexivité** : Pour tout rôle $r$, $Perm(r) \subseteq Perm(r)$, donc $r \leq r$, la relation est **réflexive**.
    - **Antisymétrie** : Si $Perm(r_1) \subseteq Perm(r_2)$ et $Perm(r_2) \subseteq Perm(r_1)$, alors $Perm(r_1) = Perm(r_2)$, donc $r_1 = r_2$. La relation est **antisymétrique**.
    - **Transitivité** : Si $Perm(r_1) \subseteq Perm(r_2)$ et $Perm(r_2) \subseteq Perm(r_3)$, alors $Perm(r_1) \subseteq Perm(r_3)$, donc $r_1 \leq r_3$. La relation est **transitive**.
    - La relation est donc un **ordre partiel**.
2. **Exemple de deux rôles incomparables :**
    
    - Soient $r_1$ avec $Perm(r_1) = {A, B}$ et $r_2$ avec $Perm(r_2) = {B, C}$.
    - $Perm(r_1) \not\subseteq Perm(r_2)$ et $Perm(r_2) \not\subseteq Perm(r_1)$, donc $r_1$ et $r_2$ sont **incomparables**.
3. **Critère pour supprimer un rôle "redondant" :**
    
    - Un rôle $r$ est **redondant** si un autre rôle $r'$ existe tel que $Perm(r) \subseteq Perm(r')$ et que $r$ n’ajoute aucune permission unique.
    - On peut alors **fusionner** les rôles ou **supprimer** $r$.

---

### **Q3b - Relation d’anagrammes**

On définit la relation :  
$u \sim v \iff u \text{ est un anagramme de } v$

1. **Type de relation** :
    
    - **Réflexivité** : Un mot est toujours l'anagramme de lui-même, donc $u \sim u$.
    - **Symétrie** : Si $u \sim v$, alors $v \sim u$ car l'ordre des lettres ne compte pas.
    - **Transitivité** : Si $u \sim v$ et $v \sim w$, alors $u \sim w$ car ils contiennent les mêmes lettres.
    - La relation est donc une **relation d'équivalence**.
2. **Exemple concret :**  
    $\text{"chien"} \sim \text{"niche"} \sim \text{"chine"}$  
    Ces mots sont des **anagrammes** car ils contiennent les mêmes lettres.
    

---

### **Q3c - Relation sur les mots binaires**

On définit :  
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
    - Ainsi, chaque **classe d'équivalence** de la relation $\sim$ correspond à un ensemble de positions de $1$.

---
