---
created: 2025-02-03
tags:
  - Lessons/School/HEH/Bloc2/Quad2
---

# # 📚  Intro - JS
> **Création de la note à *`10:33`* le *`2025-02-03`.***
---

# 📝 Prise de Notes - Cours

---
JS :
attribut
`<script>` passe de HTML vers JS
	chargement JS => Prélecture des fichiers JS pour connaitre 

---

Rôle :
- surveiller actions du visiteur
- manipuler variables, calculer des valeurs

et modifier les éléments HTML (= DOM ) pour:
- modifier les attributs
- modifier les propritétés CSS
- modifier contenus textuels
- supprimer ou ajouter des éléments CSS

---
A propos :
- Langage de prog
- adapté au web
- évènementiel
- interprété
- coté client
- Objet
- Typage dynamique
- Nouveau domaines d'app : coté serv (Node.js), app mobiles, jeux en ligne, etc.

---
Historique:
- 1994 LiveScript
- 1995 Netscape et Sun lancent JavaScript
- 1996 Netscape 2.0 premier à supporter le JavaScript
- 1997 Normaliser JavaScript => standard ECMAScript (Javascript, JScript, ActionScript/flash)
- 1998 IE -> JS

---
Intégrer JS:
- `<script> </script>`
- `<script> src="js/script1.js" ></script>
- `<script> src="js/script2.js" async ></script>
- `<script> src="js/script3.js" defer ></script> (attendre)

---
Erreurs :
- `<script> src="js/script1.js" > Code pas executé </script>
- type="text/javascript" => pas besoin
- language = "javascript" pas besoin


Commentaires :
`//`
`/* */`

---
`<noscript>`
```javascript
<noscript>
	<p> code interpreté que si pas de JS (désactivé ou inexistant)
</noscript>
```

---
Utilisation du `;`
- Séparateur d'instruction et propre

---
Utilisation des accolades  `{` et `}`
- permet de mettre des blocks d'instructions

---
Comment débuger
console.log(...);
F12

---
La console
- console.log
- console.error
- console.warn
- console.dir
- console.table
- console.time
- console.timeend

---
Variables:
- type primitif (nombre, chaîne, booléen, indéfini)
- type objet

---
Noms des variables:
- débute par une lettre
- uniquement de lettres
- pas de caractères accentués
- sensible à la case
- pas être réservé (if, break)

---
Déclarations
- explicite (let ou var), let est plus récent et mieux.
- implicite (déonseillé)
- Constantes (const)

---
Portée des variables
- implicites => globales (surcharge)
- explicites => limitées à la fonction/block d'instruction

---
eviter les variables globales

---
Les types
- primitifs
	- nombres
	- chaînes
	- booléens
	- undefined

---
Language Non typé
console.log(typeof(x))

---
erreurs de types
- NaN
- undefined (z=8; z.length)


---
Tableaux:
- indicés `Tableau(x)`
- associatif `Tableau("x")` (`Tableau(0) = Tableau("x")`)
- Plusieurs dimensions

---
Boucles
- .forEach
	- .forEach(element => console/log(element))
- for
- foreach
- while
- dowhile