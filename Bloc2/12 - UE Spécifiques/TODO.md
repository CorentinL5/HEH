---
created: 2025-04-01
tags:
  - Lessons/School/HEH/BlocX/QuadX
Auteur: LALLEMENT Corentin - 240314
---

# # 📚  TODO
> Par `LALLEMENT Corentin`, **`240314`**.
---

# 📝 Prise de Notes - Cours

---

# ✅ TODO LIST – Projet Cybersécurité (Bloc 2 uniquement)

| Thème principal           | Spécification technique à réaliser                                              | Échéance | Terminé |
| ------------------------- | ------------------------------------------------------------------------------- | -------- | ------- |
| 📌 Analyse et préparation |                                                                                 |          |         |
|                           | Identifier les ressources disponibles (matériel, salle, IP, etc.)               |          | ✅       |
|                           | Définir la topologie générale (nombre de sites, liens WAN, etc.)                |          | ✅       |
| 🧠 Schémas réseau         |                                                                                 |          |         |
|                           | Réaliser un schéma **logique** avec LAN/WAN, routeurs, VDOM, VPN                |          | ✅       |
|                           | Réaliser un schéma **physique** des salles 2/13 et 2/16                         |          | ☐       |
| 🧮 Plan d’adressage IP    |                                                                                 |          |         |
|                           | Définir les **plages IP**                                                       |          | ✅       |
| 🖧 Déploiement des LAN    |                                                                                 |          |         |
|                           | Configurer les VLANs sur les switchs                                            |          | ☐       |
|                           | Configurer les trunks 802.1Q                                                    |          | ☐       |
|                           | Activer STP/RSTP (sécurité switch)                                              |          | ☐       |
|                           | Affecter les adresses IP aux interfaces LAN                                     |          | ☐       |
| 🌍 Déploiement WAN        |                                                                                 |          |         |
|                           | Simuler 2 liens WAN (via câbles croisés ou switch dédié)                        |          | ☐       |
|                           | Configurer les routeurs avec du **routage statique** (ou dynamique si autorisé) |          | ☐       |
|                           | Vérifier la connectivité inter-site                                             |          | ☐       |
| 🔥 Fortigate et VDOM      |                                                                                 |          |         |
|                           | Activer le mode VDOM sur chaque Fortigate                                       |          | ☐       |
|                           | Créer un VDOM par LAN (par salle ou par "site")                                 |          | ☐       |
|                           | Attribuer les interfaces physiques à chaque VDOM                                |          | ☐       |
|                           | Configurer le NAT, DHCP et DNS dans chaque VDOM                                 |          | ☐       |
|                           | Appliquer les règles de **firewall de base**                                    |          | ☐       |
|                           | Autoriser le trafic interne autorisé (ex : LAN → WAN, ping, AD)                 |          | ☐       |
| 🔒 Sécurisation de base   |                                                                                 |          |         |
|                           | Changer les mots de passe par défaut sur tous les équipements                   |          | ☐       |
|                           | Désactiver Telnet, activer SSH uniquement                                       |          | ☐       |
|                           | Configurer une bannière de sécurité                                             |          | ☐       |
|                           | Créer des utilisateurs avec droits limités                                      |          | ☐       |
| 🌐 Accès Internet via DST |                                                                                 |          |         |
|                           | Intégrer chaque LAN dans le LAN du département DST                              |          | ☐       |
|                           | Vérifier NAT et résolutions DNS vers l'extérieur                                |          | ☐       |
| 🛜 VPN site-à-site        |                                                                                 |          |         |
|                           | Configurer un VPN IPsec site-à-site entre les agences/sites                     |          | ☐       |
|                           | Vérifier la **réplication Active Directory** entre les sites via VPN            |          | ☐       |
|                           | Tester le tunnel (stabilité, performance, ping AD, LDAP)                        |          | ☐       |
| 🧾 Documentation Bloc 2   |                                                                                 |          |         |
|                           | Commencer la doc technique : schémas, IP, configs, roles                        |          | ☐       |
|                           | Versionner les fichiers (Git ou simple historique de modifs)                    |          | ☐       |
|                           | Inclure copies d’écran, logs de test, configurations Fortigate/routeur          |          | ☐       |



---


## 01/04/2025

| Tâche                                 | Fait |
| ------------------------------------- | ---- |
| Plan de nommage equipements           | ✅    |
| Plan de nommage VDOM                  | ✅    |
| VDOM ?                                | ✅    |
| Configuration du switch               | ✅    |
| Plan de nomage nom de domaines        | ❌    |
| Schéma réseau                         | ❌    |
| Plan d’adressage IP pour mon agence 3 | ❌    |
| Configuration du routeur              | ❌    |
|                                       |      |


## 15/04/2025

| Tâche                                 | Fait |
| ------------------------------------- | ---- |
| Plan de nomage nom de domaines        |      |
| Schéma réseau                         |      |
| Plan d’adressage IP pour mon agence 3 |      |
| Configuration du routeur              |      |
|                                       |      |
