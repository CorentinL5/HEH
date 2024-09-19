---
created: 2024-09-17
tags:
  - Lessons/School/HEH/Bloc1/Quad2
---

# # 📚  Base de données
> **Création de la note à *`10:38`* le *`2024-09-17`.***
---

# 📝 Prise de Notes - Cours

---

## 👋 Infos du Cours
- **Professeur :** Malaise

---

## 📅 Dates de cours

https://hehplanning2024.umons.ac.be/invite


---

## 📚 Références

- [Fiche ECTS](https://www.heh.be/upload/ects/2024-2025/2024-2025-UE-bases-de-donnees-et-developpement-back-end-12334.pdf) 
---

## 📑 Notes

### Note du [[2024-09-17]]

- SGBD: Système de Gestion de Base de Données
- SQL 
- ![DB-Engines Ranking](https://db-engines.com/en/ranking)


#### Principe du MCD
> *Comme les classes en UML (sans méthodes)*
- Attributs
	Identifiants (clé) 
- Associations
- Degré
- Cardinalités
	1,1 / 0,N
##### Clé primaire
> *Être Certain d'être unique*
- propriété naturelle
	Personne > Email
- propriété artificielle 👍
	Client > ID
- propriété composée
	Entreprise > Enseigne + localité
##### Associations
- One to many
	Le one contient l'ID du many
- Many to many
	Il faut créer une table "de jointure" pour "lier les deux"

---

### Note du [[2024-09-19]]

#### Exercices de MCD
1) Marque 
   Voiture
   client
   - ![[Pasted image 20240919091227.png]]
2) Dresseur,
   Pokemon,
   race,
   type,
   attaque,
   equipe
   - ![[Pasted image 20240919091239.png]]
#### MCD > MLD
> Cardinalités retirés et noms d'associations retirés
##### one to many
- ajouter une clé et faire une flèche de la clé 
##### many to many
- table avec le verbe
- et ajouter dans cette table les 2 ID et des infos, souligner une nouvelle ID 
  (flèche de la nouvelle table vers les deux existantes)
##### one to one
- UNE SEULE TABLE

/back
