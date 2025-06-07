## ⚙️ Étapes globales du projet React + API sécurisée

### 🧱 Étape 1 – Initialisation du projet

* [ ] Création du projet React avec Vite (vite + react)
* [ ] Arborescence claire (`components/`, `pages/`, `context/`, `api/`, etc.)
* [ ] Configuration d’Axios avec interceptor (`axiosConfig.js`)
* [ ] Setup `React Router` + `Context` global (`AuthContext`, `CartContext`)

---

### 🔐 Étape 2 – Authentification sécurisée

* [ ] Pages **Login** et **Register** connectées à l’API
* [ ] AuthContext avec `accessToken` et `refreshToken`
* [ ] Auto-refresh du token si expiré
* [ ] Protection des routes privées (`PrivateRoute`)

---

### 🛍️ Étape 3 – Produits & Catégories

* [ ] Page **Tous les produits**
* [ ] Page **par catégorie**
* [ ] Page **détails produit** (avec images, stock, reviews, etc.)
* [ ] Bouton favoris
* [ ] Ajout au panier (choix couleur, taille, quantité)

---

### 🛒 Étape 4 – Panier & commande

* [ ] Vue du panier (avec prix, total, édition quantité)
* [ ] Application d’un code **promo / réduction**
* [ ] Validation du panier → Création de la commande
* [ ] Page historique des commandes

---

### ⭐ Étape 5 – Système de reviews

* [ ] Ajouter un avis (note + commentaire)
* [ ] Affichage des avis sur chaque produit
* [ ] Moyenne des étoiles visibles

---

### 🧠 Étape 6 – Page utilisateur

* [ ] Infos personnelles
* [ ] Gestion du mot de passe
* [ ] Historique commandes + favoris

---
