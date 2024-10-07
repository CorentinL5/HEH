---
created: 2024-09-23
tags:
  - Lessons/School/HEH/Bloc2/Quad2
---
q
# # 📚  Ch1 - LaPlace
> **Création de la note à *`08:20`* le *`2024-09-23`.***
---

# 📝 Prise de Notes - Cours

---

> ![[Laplace.pdf]]

# Calcul des Transformées de Laplace Inverses
> ![[LaplaceExo24-25.pdf#page=1|noscroll]]

## Exercice 1
> Calculer les transformées de Laplace des signaux causaux suivants
> ![[Pasted image 20241001135909.png]] 

### (a) $2e^{-6t}$

La formule pour la transformée de Laplace de $e^{-at}$ est :
$$
\mathcal{L}(e^{-at}) = \frac{1}{p+a}
$$
Donc :
$$
\mathcal{L}(2e^{-6t}) = \frac{2}{p+6}
$$

---

### (b) $5e^{2t}$

La formule pour $e^{at}$ est :
$$
\mathcal{L}(e^{at}) = \frac{1}{p-a}
$$
Ainsi :
$$
\mathcal{L}(5e^{2t}) = \frac{5}{p-2}
$$

---

### (c) $2t^4$

La formule pour $t^n$ est :
$$
\mathcal{L}(t^n) = \frac{n!}{p^{n+1}}
$$
Donc pour $t^4$, nous avons :
$$
\mathcal{L}(2t^4) = 2 \times \frac{4!}{p^5} = \frac{48}{p^5}
$$

---

### (d) $\alpha \cos(\omega t) + \beta \sin(\omega t)$

Les formules pour $\cos(\omega t)$ et $\sin(\omega t)$ sont :
$$
\mathcal{L}(\cos(\omega t)) = \frac{p}{p^2 + \omega^2}
$$
$$
\mathcal{L}(\sin(\omega t)) = \frac{\omega}{p^2 + \omega^2}
$$
Donc :
$$
\mathcal{L}(\alpha \cos(\omega t) + \beta \sin(\omega t)) = \alpha \frac{p}{p^2 + \omega^2} + \beta \frac{\omega}{p^2 + \omega^2}
$$

---

### (e) $t^2 + t - e^{-3t}$

On utilise la formule pour $t^n$ et pour $e^{-at}$ :
$$
\mathcal{L}(t^2) = \frac{2!}{p^3} = \frac{2}{p^3}
$$
$$
\mathcal{L}(t) = \frac{1}{p^2}
$$
$$
\mathcal{L}(e^{-3t}) = \frac{1}{p+3}
$$
Ainsi, la solution complète est :
$$
\mathcal{L}(t^2 + t - e^{-3t}) = \frac{2}{p^3} + \frac{1}{p^2} - \frac{1}{p+3}
$$

---

### (f) $(t^2 + 1)^2$

Développons d'abord l'expression :
$$
(t^2 + 1)^2 = t^4 + 2t^2 + 1
$$
On utilise les formules pour $t^n$ :
$$
\mathcal{L}(t^4) = \frac{4!}{p^5} = \frac{24}{p^5}
$$
$$
\mathcal{L}(t^2) = \frac{2!}{p^3} = \frac{2}{p^3}
$$
$$
\mathcal{L}(1) = \frac{1}{p}
$$
Donc la solution est :
$$
\mathcal{L}((t^2 + 1)^2) = \frac{24}{p^5} + \frac{4}{p^3} + \frac{1}{p}
$$

---

### (g) $H(t - 1)$

La fonction échelon de Heaviside $H(t - a)$ a pour transformée de Laplace :
$$
\mathcal{L}(H(t - a)) = \frac{e^{-ap}}{p}
$$
Ici, $a = 1$, donc :
$$
\mathcal{L}(H(t - 1)) = \frac{e^{-p}}{p}
$$

---

### (h) $(t - 1)H(t - 1)$

La formule pour $H(t-a)f(t-a)$ est :
$$
\mathcal{L}((t - a)H(t - a)) = \frac{e^{-ap}}{p^2}
$$
Ici, $a = 1$, donc :
$$
\mathcal{L}((t - 1)H(t - 1)) = \frac{e^{-p}}{p^2}
$$

---

### (i) $tH(t - 1)$

Utilisons la même formule pour $t H(t - a)$ :
$$
\mathcal{L}(t H(t - a)) = \frac{e^{-ap}(1 + ap)}{p^2}
$$
Ici, $a = 1$, donc :
$$
\mathcal{L}(tH(t - 1)) = \frac{e^{-p}(1 + p)}{p^2}
$$

---

### (j) $(t - 5)H(t - 4)$

Encore une fois, on utilise la formule :
$$
\mathcal{L}((t - a)H(t - b)) = \frac{e^{-bp}}{p^2}
$$
Ici, $a = 5$ et $b = 4$, donc :
$$
\mathcal{L}((t - 5)H(t - 4)) = \frac{e^{-4p}}{p^2}
$$

---

### (k) $e^{3t}t^3$

Pour $e^{at}t^n$, la formule est :
$$
\mathcal{L}(e^{at}t^n) = \frac{n!}{(p - a)^{n+1}}
$$
Ici, $n = 3$ et $a = 3$, donc :
$$
\mathcal{L}(e^{3t}t^3) = \frac{3!}{(p - 3)^4} = \frac{6}{(p - 3)^4}
$$

---

### (l) $e^t \cos(t)$

Pour $e^{at} \cos(bt)$, la formule est :
$$
\mathcal{L}(e^{at} \cos(bt)) = \frac{p - a}{(p - a)^2 + b^2}
$$
Ici, $a = 1$ et $b = 1$, donc :
$$
\mathcal{L}(e^t \cos(t)) = \frac{p - 1}{(p - 1)^2 + 1}
$$

---

### (m) $e^{-4t} \sin(5t)$

Pour $e^{at} \sin(bt)$, la formule est :
$$
\mathcal{L}(e^{at} \sin(bt)) = \frac{b}{(p - a)^2 + b^2}
$$
Ici, $a = -4$ et $b = 5$, donc :
$$
\mathcal{L}(e^{-4t} \sin(5t)) = \frac{5}{(p + 4)^2 + 25}
$$

---

### (n) $(t^2 + t + 1)e^{-2t}$

Développons cette expression en trois termes :
$$
t^2 e^{-2t}, \quad t e^{-2t}, \quad e^{-2t}
$$
Pour $t^n e^{at}$, la formule est :
$$
\mathcal{L}(t^n e^{at}) = \frac{n!}{(p - a)^{n+1}}
$$
Ainsi, pour chaque terme :
$$
\mathcal{L}(t^2 e^{-2t}) = \frac{2!}{(p + 2)^3} = \frac{2}{(p + 2)^3}
$$
$$
\mathcal{L}(t e^{-2t}) = \frac{1}{(p + 2)^2}
$$
$$
\mathcal{L}(e^{-2t}) = \frac{1}{p + 2}
$$
La solution est donc :
$$
\mathcal{L}((t^2 + t + 1)e^{-2t}) = \frac{2}{(p + 2)^3} + \frac{1}{(p + 2)^2} + \frac{1}{p + 2}
$$

---

### (o) $e^{-2t}(t^2 - 1)^2$

Développons l'expression $(t^2 - 1)^2$ :
$$
(t^2 - 1)^2 = t^4 - 2t^2 + 1
$$
Ainsi, on doit calculer :
$$
e^{-2t}t^4, \quad e^{-2t}t^2, \quad e^{-2t}
$$
Pour chaque terme :
$$
\mathcal{L}(t^4 e^{-2t}) = \frac{4!}{(p + 2)^5} = \frac{24}{(p + 2)^5}
$$
$$
\mathcal{L}(t^2 e^{-2t}) = \frac{2!}{(p + 2)^3} = \frac{2}{(p + 2)^3}
$$
$$
\mathcal{L}(e^{-2t}) = \frac{1}{p + 2}
$$
La solution complète est :
$$
\mathcal{L}(e^{-2t}(t^2 - 1)^2) = \frac{24}{(p + 2)^5} - \frac{4}{(p + 2)^3} + \frac{1}{p + 2}
$$

---

### (p) $2e^{-5t}(\cos(2t) + \sin(2t))$

On utilise les formules pour $e^{at} \cos(bt)$ et $e^{at} \sin(bt)$ :
$$
\mathcal{L}(e^{at} \cos(bt)) = \frac{p - a}{(p - a)^2 + b^2}
$$
$$
\mathcal{L}(e^{at} \sin(bt)) = \frac{b}{(p - a)^2 + b^2}
$$
Ici, $a = -5$ et $b = 2$, donc :
$$
\mathcal{L}(e^{-5t} \cos(2t)) = \frac{p + 5}{(p + 5)^2 + 4}
$$
$$
\mathcal{L}(e^{-5t} \sin(2t)) = \frac{2}{(p + 5)^2 + 4}
$$
La solution complète est :
$$
\mathcal{L}(2e^{-5t}(\cos(2t) + \sin(2t))) = 2 \left( \frac{p + 5}{(p + 5)^2 + 4} + \frac{2}{(p + 5)^2 + 4} \right)
$$


---

## Exercice 2
> Calculer les transformées de Laplace inverse des signaux suivants 
> ![[Pasted image 20241001134625.png]] 

### (a) $\frac{3}{p+2} - \frac{1}{p^3}$

Première partie :
$$
\frac{3}{p+2}
$$
On utilise la formule standard de la transformée inverse :
$$
\mathcal{L}^{-1} \left( \frac{A}{p+a} \right) = A e^{-at}
$$
Ici, $A = 3$ et $a = 2$, donc :
$$
\mathcal{L}^{-1} \left( \frac{3}{p+2} \right) = 3 e^{-2t}
$$

Deuxième partie :
$$
\frac{1}{p^3}
$$
La transformée inverse de $\frac{1}{p^n}$ est :
$$
\mathcal{L}^{-1} \left( \frac{1}{p^n} \right) = \frac{t^{n-1}}{(n-1)!}
$$
Ici, $n = 3$, donc :
$$
\mathcal{L}^{-1} \left( \frac{1}{p^3} \right) = \frac{t^2}{2}
$$

Solution complète (a) :
$$
\mathcal{L}^{-1} \left( \frac{3}{p+2} - \frac{1}{p^3} \right) = 3 e^{-2t} - \frac{t^2}{2}
$$

---

### (b) $\frac{p+2}{(p+3)(p+4)}$  

Cette expression peut être décomposée en fractions partielles :
$$
\frac{p+2}{(p+3)(p+4)} = \frac{A}{p+3} + \frac{B}{p+4}
$$
On résout cette équation :
$$
p+2 = A(p+4) + B(p+3)
$$
En développant et en regroupant les termes, on obtient :
$$
p+2 = (A+B)p + (4A + 3B)
$$
En comparant les coefficients de $p$ et les constantes, on obtient :
$$
A + B = 1 \quad \text{et} \quad 4A + 3B = 2
$$
Résolution de ce système :
$$
A = -1 \quad \text{et} \quad B = 2
$$
Donc :
$$
\frac{p+2}{(p+3)(p+4)} = \frac{-1}{p+3} + \frac{2}{p+4}
$$

Les transformées inverses de $\frac{1}{p+a}$ sont $e^{-at}$, donc la solution est :
$$
\mathcal{L}^{-1} \left( \frac{p+2}{(p+3)(p+4)} \right) = -e^{-3t} + 2e^{-4t}
$$

---

### (c) $\frac{a}{p^2 - a^2}$ 
		
Cette expression peut être simplifiée en utilisant la formule :
$$
\frac{1}{p^2 - a^2} = \frac{1}{2a} \left( \frac{1}{p - a} - \frac{1}{p + a} \right)
$$
Donc :
$$
\mathcal{L}^{-1} \left( \frac{A}{p - a} \right) + \left( \frac{B}{p - a} \right)
$$
$$
\frac{A(P+a) + B(p-a)}{(p-a)(p+a)}
$$
$$
\text{Si p = -a : } a=-2aB \leftrightarrow B = -\frac{1}{2}
$$
$$
\text{Si p = a : } a=2aA \leftrightarrow A = \frac{1}{2}
$$
$$
\mathcal{L1}^{-1} \left( \frac{a}{p^2 - a^2} \right) =  \frac{e^at-e^-at}{2}
$$
---

### (d) $\frac{3}{(p+6)^2}$ 

Pour cette expression, on utilise la formule de la transformée inverse :
$$
\mathcal{L}^{-1} \left( \frac{A}{(p+a)^n} \right) = \frac{A t^{n-1}}{(n-1)!} e^{-at}
$$
Ici, $A = 3$, $a = 6$, et $n = 2$, donc la solution est :
$$
\mathcal{L}^{-1} \left( \frac{3}{(p+6)^2} \right) = 3 t e^{-6t}
$$

---

### (e) $\frac{10}{p^2 + 4p - 21}$ 

On commence par factoriser le dénominateur :
$$
p^2 + 4p - 21 = 0
$$
$$
\Delta = b^2 - 4ac = 4^2 - 4 \times 1 \times (-21) = 16 + 84 = 100
$$
$$
p = \frac{-b \pm \sqrt{\Delta}}{2a} = \frac{-4 \pm \sqrt{100}}{2 \times 1} = \frac{-4 \pm 10}{2}
$$
$$
p_1 = \frac{-4 + 10}{2} = 3 \quad \text{et} \quad p_2 = \frac{-4 - 10}{2} = -7
$$
$$
p^2 + 4p - 21 = (p - 3)(p + 7)
$$
Ensuite, on décompose en fractions partielles :
$$
\frac{10}{(p-3)(p+7)} = \frac{A}{p-3} + \frac{B}{p+7}
$$
En résolvant, on trouve $A = 1$ et $B = -1$, donc :
$$
\frac{10}{(p-3)(p+7)} = \frac{5}{2} \left( \frac{1}{p-3} - \frac{1}{p+7} \right)
$$
Les transformées inverses de $\frac{1}{p-a}$ sont $e^{at}$, donc la solution est :
$$
\mathcal{L}^{-1} \left( \frac{10}{p^2 + 4p - 21} \right) = e^{3t} - e^{-7t}
$$

---

### (f) $\frac{p}{(p - 5)^3}$

$$
\frac{p}{(p - 5)^3} = \frac{A}{(p - 5)} + \frac{B}{(p - 5)^2} + \frac{C}{(p - 5)^3}
$$
Multiplier par $(p - 5)^3$ 
Pour éliminer les dénominateurs, multiplions les deux côtés de l'équation par $(p - 5)^3$ :

$$
p = A(p - 5)^2 + B(p - 5) + C
$$
Développer
Développons chaque terme :

- $A(p - 5)^2 = A(p^2 - 10p + 25) = A p^2 - 10 A p + 25 A$
- $B(p - 5) = B p - 5 B$
- $C$ reste inchangé.

L'équation devient donc :

$$
p = A p^2 - 10 A p + 25 A + B p - 5 B + C
$$
$$
p = A p^2 + (-10A + B) p + (25A - 5B + C)
$$

Comparer les coefficients
Pour que cette équation soit valide, les coefficients de chaque puissance de $p$ doivent être égaux de chaque côté de l'équation.

- Le coefficient de $p^2$ est 0 à gauche, donc $A = 0$.
- Le coefficient de $p$ est 1 à gauche, donc $-10A + B = 1$.
- Le terme constant est 0 à gauche, donc $25A - 5B + C = 0$.

Résolution

- De $A = 0$, on déduit que $B = 1$ (de l'équation $-10A + B = 1$).
- En substituant $A = 0$ et $B = 1$ dans l'équation $25A - 5B + C = 0$, on obtient $-5 + C = 0$, donc $C = 5$.

Résultat final
$$
A = 0, \quad B = 1, \quad C = 5
$$

Ainsi, la décomposition en fractions partielles est :

$$
\frac{p}{(p - 5)^3} = \frac{1}{(p - 5)^2} + \frac{5}{(p - 5)^3}
$$
$$
\mathcal{L}^{-1} \left( \frac{p}{(p - 5)^3} \right) = \mathcal{L}^{-1} \left( \frac{1}{(p - 5)^2} \right) + 5 \times \mathcal{L}^{-1} \left( \frac{5}{(p - 5)^3} \right)
$$
---

### (g) $\frac{p+7}{p^2 + 49}$

On décompose cette expression en deux parties :
$$
\frac{p+7}{p^2 + 49} = \frac{p}{p^2 + 49} + \frac{7}{p^2 + 49}
$$

La première partie est de la forme $\frac{p}{p^2 + a^2}$, dont la transformée inverse est $\cos(at)$, et la deuxième est de la forme $\frac{a}{p^2 + a^2}$, dont la transformée inverse est $\frac{\sin(at)}{a}$. Donc la solution est :
$$
\mathcal{L}^{-1} \left( \frac{p+7}{p^2 + 49} \right) = \cos(7t) + \sin(7t)
$$

---

### (h) $\frac{e^{-p}}{p^3}$

Pour expliquer le raisonnement complet derrière la résolution de l'expression $\frac{e^{-p}}{p^3}$ en utilisant les formules présentes dans l'image, nous allons décomposer le problème en deux parties principales : la transformée inverse de $\frac{1}{p^3}$ et l'effet du terme $e^{-p}$ qui introduit un décalage.

#### Partie 1 : Transformée inverse de $\frac{1}{p^3}$

Dans l'image, nous voyons plusieurs formules pour la transformée de Laplace de fonctions courantes. La formule pertinente ici est celle de la transformée de Laplace d'une fonction de la forme $t^n$, indiquée par :

$$
t^n \quad \longrightarrow \quad \frac{n!}{p^{n+1}}
$$

Nous avons dans notre cas $\frac{1}{p^3}$, qui correspond à $n = 2$, car :

$$
\mathcal{L} \left( \frac{t^2}{2} \right) = \frac{2!}{p^3} = \frac{2}{p^3}
$$

Par conséquent, nous savons que la transformée inverse de $\frac{1}{p^3}$ est donnée par :

$$
\mathcal{L}^{-1} \left( \frac{1}{p^3} \right) = \frac{t^2}{2}
$$

Cela nous donne la partie de la fonction sans décalage temporel.

#### Partie 2 : Effet du terme $e^{-p}$

Le terme $e^{-p}$ dans l'expression $\frac{e^{-p}}{p^3}$ représente un décalage dans le temps. Dans l'image, nous avons la formule correspondante au décalage temporel sous la forme :

$$
e^{-ap} x(t) \quad \longrightarrow \quad x(t - a) u(t - a)
$$

C'est la formule standard qui nous dit que la multiplication par $e^{-ap}$ dans le domaine de Laplace correspond à un décalage de $a$ unités vers la droite dans le domaine temporel, avec la fonction échelon de Heaviside $u(t - a)$ qui active la fonction à partir de $t = a$.

Dans notre cas, $a = 1$, donc la multiplication par $e^{-p}$ indique un décalage de 1 unité vers la droite. Cela transforme la fonction $\frac{t^2}{2}$ en $\frac{(t - 1)^2}{2}$ et introduit la fonction échelon de Heaviside $u(t - 1)$ qui active cette fonction à partir de $t = 1$.
 
#### Conclusion

En combinant ces deux résultats, nous obtenons que :

$$
\mathcal{L}^{-1} \left( \frac{e^{-p}}{p^3} \right) = u(t-1) \frac{(t-1)^2}{2}
$$

##### Raisonnement résumé :
1. La transformée inverse de $\frac{1}{p^3}$ est $\frac{t^2}{2}$.
2. Le terme $e^{-p}$ représente un décalage de 1 unité vers la droite, ce qui nous donne $\frac{(t-1)^2}{2}$.
3. La fonction échelon de Heaviside $u(t-1)$ est utilisée pour activer cette fonction à partir de $t = 1$.

Donc, la solution complète est
$$u(t-1) \frac{(t-1)^2}{2}$$

---

## Exercice 3
> Résoudre les équations différentielles suivantes
> ![[Pasted image 20241001140728.png]] 

J'ai ouvert l'image que vous avez fournie. Maintenant, je vais résoudre les équations différentielles en utilisant les transformées de Laplace. Voici les solutions pour chaque équation :

### (a) $s'(t) + 3s(t) = 0$;$s(0) = 1$

1. **Transformée de Laplace :**  
  $s(s) + 3S(s) = 0$
   
2. **Résoudre pour$S(s)$:**  
  $S(s) = -\frac{s}{3}$

3. **Transformée inverse de Laplace :**  
  $s(t) = e^{-3t}$

---

### (b) $s'(t) - 2s(t) = t$ ; $s(0) = 0$

1. **Transformée de Laplace :**  
  $s(s) - 2S(s) =\frac{1}{s^2}$

2. **Résoudre pour $S(s)$:**  
  $S(s)(1 - 2) =\frac{1}{s^2} \text{ X } S(s) = \frac{1}{s^2(1 - 2)} = -\frac{1}{s^2}$

3. **Transformée inverse de Laplace :** 
  $s(t) = -\frac{t}{2}$

---

### (c) $s'(t) = s(t) + te^t ;s(0) = -1$

1. **Transformée de Laplace :**  
  $s(p) - (-1) = S(p) +\frac{1}{(s-1)^2}$
$s(p) * (p-1) = \frac{1}{(p-1)²}-1$
$L^{-1}\left( \frac{1}{p^3} \right) = \frac{t²}{2}$

---

### (d) ${1}{2}s'(t) + s(t) =\sin(2t) +\cos(2t) ; s(0) = 0$

$$
\frac{1}{2} * S(p) + S(p) = \frac{p+2}{p²+4}
$$
$$
S(p) * \left( \frac{1}{2} * p + 1 \right) = \frac{p+2}{p²+4}
$$
$$
S(p) * \left( p + 2 \right) = \frac{p+2}{p²+4}
$$
$$
\frac{1}{2} * S(p) = \frac{1}{p²+4}
$$
$$
s(t) = L^{-1} \left(  \frac{2}{p²+4} \right) = \sin(2t)
$$
---
