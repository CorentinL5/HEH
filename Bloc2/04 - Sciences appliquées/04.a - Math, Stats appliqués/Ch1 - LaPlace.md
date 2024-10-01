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
![[Laplace.pdf]]

# Calcul des Transformées de Laplace Inverses

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

#### Première partie :
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

#### Deuxième partie :
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

#### Solution complète (a) :
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
A = 1 \quad \text{et} \quad B = -1
$$
Donc :
$$
\frac{p+2}{(p+3)(p+4)} = \frac{1}{p+3} - \frac{1}{p+4}
$$

Les transformées inverses de $\frac{1}{p+a}$ sont $e^{-at}$, donc la solution est :
$$
\mathcal{L}^{-1} \left( \frac{p+2}{(p+3)(p+4)} \right) = e^{-3t} - e^{-4t}
$$

---

### (c) $\frac{a}{p^2 - a^2}$ 

Cette expression peut être simplifiée en utilisant la formule :
$$
\frac{1}{p^2 - a^2} = \frac{1}{2a} \left( \frac{1}{p - a} - \frac{1}{p + a} \right)
$$
La transformée inverse est donc :
$$
\mathcal{L}^{-1} \left( \frac{1}{p^2 - a^2} \right) = \frac{\sinh(at)}{a}
$$
En multipliant par $a$, on obtient :
$$
\mathcal{L}^{-1} \left( \frac{a}{p^2 - a^2} \right) = \sinh(at)
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
p^2 + 4p - 21 = (p-3)(p+7)
$$
Ensuite, on décompose en fractions partielles :
$$
\frac{10}{(p-3)(p+7)} = \frac{A}{p-3} + \frac{B}{p+7}
$$
En résolvant, on trouve $A = \frac{5}{2}$ et $B = \frac{5}{2}$, donc :
$$
\frac{10}{(p-3)(p+7)} = \frac{5}{2} \left( \frac{1}{p-3} - \frac{1}{p+7} \right)
$$
Les transformées inverses de $\frac{1}{p-a}$ sont $e^{at}$, donc la solution est :
$$
\mathcal{L}^{-1} \left( \frac{10}{p^2 + 4p - 21} \right) = \frac{5}{2} e^{3t} - \frac{5}{2} e^{-7t}
$$

---

### (f) $\frac{p}{(p-5)^3}$ 

C'est une fonction dérivée. On reconnaît que la transformée inverse de $\frac{1}{(p-a)^n}$ est :
$$
\mathcal{L}^{-1} \left( \frac{1}{(p-a)^n} \right) = \frac{t^{n-1}}{(n-1)!} e^{at}
$$
Dans ce cas, nous avons besoin de la dérivée par rapport à $t$. La solution est donc :
$$
\mathcal{L}^{-1} \left( \frac{p}{(p-5)^3} \right) = (t + 2) e^{5t}
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

Cette expression est une transformée décalée dans le temps. On reconnaît que la transformée inverse de $\frac{1}{p^3}$$ est  $\frac{t^2}{2}$ . Le terme $e^{-p}$ représente un décalage d'une unité vers la droite. 
Donc la solution est :
$$
\mathcal{L}^{-1} \left( \frac{e^{-p}}{p^3} \right) = u(t-1) \frac{(t-1)^2}{2}
$$
où $u(t-1)$ est la fonction échelon de Heaviside.

---

## Exercice 3
> Résoudre les équations différentielles suivantes
> ![[Pasted image 20241001140728.png]] 

### (a) $s'(t) + 3s(t) = 0$ avec $s(0) = 1$

Cette équation est une équation différentielle linéaire du premier ordre avec coefficients constants. La solution générale d'une équation de la forme $s'(t) + as(t) = 0$ est :
$$
s(t) = Ce^{-at}
$$
Ici, $a = 3$, donc la solution générale est :
$$
s(t) = Ce^{-3t}
$$
Utilisons la condition initiale $s(0) = 1$ pour déterminer $C$ :
$$
1 = Ce^{0} \implies C = 1
$$
La solution est donc :
$$
s(t) = e^{-3t}
$$

---

### (b) $s'(t) - 2s(t) = t$ avec $s(0) = 0$

Cette équation est une équation différentielle linéaire non homogène. La solution générale est de la forme :
$$
s(t) = s_h(t) + s_p(t)
$$
- **Solution de l'équation homogène** :
L'équation homogène associée est $s'(t) - 2s(t) = 0$. La solution est :
$$
s_h(t) = Ce^{2t}
$$

- **Solution particulière** :
Cherchons une solution particulière de la forme $s_p(t) = At + B$. En dérivant :
$$
s_p'(t) = A
$$
Substituons dans l'équation :
$$
A - 2(At + B) = t
$$
Ce qui donne le système suivant :
$$
A - 2A = 0 \implies A = 1
$$
$$
-2B = 0 \implies B = 0
$$
Donc, la solution particulière est $s_p(t) = t$.

- **Solution générale** :
$$
s(t) = Ce^{2t} + t
$$
Utilisons la condition initiale $s(0) = 0$ pour déterminer $C$ :
$$
0 = Ce^{0} + 0 \implies C = 0
$$
La solution est donc :
$$
s(t) = t
$$

---

### (c) $s'(t) = s(t) + te^t$ avec $s(0) = -1$

Cette équation est également une équation différentielle non homogène. Nous allons utiliser la méthode du facteur intégrant pour la résoudre.

- **Réécriture de l'équation** :
$$
s'(t) - s(t) = te^t
$$

Le facteur intégrant est donné par $e^{-\int -1 dt} = e^t$.

- **Multiplication de l'équation par le facteur intégrant** :
$$
e^t s'(t) - e^t s(t) = te^{2t}
$$
$$
\frac{d}{dt}(e^t s(t)) = te^{2t}
$$

Intégrons les deux côtés par rapport à $t$ :
$$
e^t s(t) = \int te^{2t} dt
$$
Utilisons l'intégration par parties pour résoudre $\int te^{2t} dt$. Soit :
- $u = t \implies du = dt$
- $dv = e^{2t} dt \implies v = \frac{e^{2t}}{2}$

L'intégrale devient :
$$
\int te^{2t} dt = \frac{te^{2t}}{2} - \int \frac{e^{2t}}{2} dt = \frac{te^{2t}}{2} - \frac{e^{2t}}{4}
$$

Ainsi, nous avons :
$$
e^t s(t) = \frac{te^{2t}}{2} - \frac{e^{2t}}{4} + C
$$
Divisons par $e^t$ :
$$
s(t) = \frac{te^{t}}{2} - \frac{e^{t}}{4} + Ce^{-t}
$$

Utilisons la condition initiale $s(0) = -1$ :
$$
-1 = \frac{0}{2} - \frac{1}{4} + C \implies C = -\frac{3}{4}
$$

La solution finale est donc :
$$
s(t) = \frac{te^{t}}{2} - \frac{e^{t}}{4} - \frac{3}{4}e^{-t}
$$

---

### (d) $\frac{1}{2}s'(t) + s(t) = \sin(2t) + \cos(2t)$ avec $s(0) = 0$

Commençons par réécrire l'équation :
$$
s'(t) + 2s(t) = 2\sin(2t) + 2\cos(2t)
$$

C'est une équation différentielle linéaire non homogène. La solution générale est de la forme :
$$
s(t) = s_h(t) + s_p(t)
$$

- **Solution de l'équation homogène** :
L'équation homogène associée est $s'(t) + 2s(t) = 0$. La solution est :
$$
s_h(t) = Ce^{-2t}
$$

- **Solution particulière** :
Cherchons une solution particulière de la forme :
$$
s_p(t) = A\sin(2t) + B\cos(2t)
$$
En dérivant :
$$
s_p'(t) = 2A\cos(2t) - 2B\sin(2t)
$$
Substituons dans l'équation :
$$
(2A\cos(2t) - 2B\sin(2t)) + 2(A\sin(2t) + B\cos(2t)) = 2\sin(2t) + 2\cos(2t)
$$

En regroupant les termes en $\sin(2t)$ et $\cos(2t)$ :
$$
(2A + 2B)\cos(2t) + (-2B + 2A)\sin(2t) = 2\cos(2t) + 2\sin(2t)
$$
Cela nous donne le système :
$$
2A + 2B = 2 \quad \text{(1)}
$$
$$
-2B + 2A = 2 \quad \text{(2)}
$$

Résolvons ce système :
- En additionnant (1) et (2), on obtient $4A = 4 \implies A = 1$
- En substituant dans (1), on trouve $2 + 2B = 2 \implies B = 0$

La solution particulière est donc :
$$
s_p(t) = \sin(2t)
$$

- **Solution générale** :
$$
s(t) = Ce^{-2t} + \sin(2t)
$$

Utilisons la condition initiale $s(0) = 0$ :
$$
0 = C + \sin(0) \implies C = 0
$$

La solution finale est donc :
$$
s(t) = \sin(2t)
$$

---
