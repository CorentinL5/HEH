---
created: 2024-09-26
tags:
  - Lessons/School/HEH/Bloc2/Quad2
---

# # 📚  Linux Manips
> **Création de la note à *`08:34`* le *`2024-09-26`.***
---

# 📝 Prise de Notes - Cours

---
## Manip one 
### PDF
![[01_Labo_Linux_Les_commandes_de_bases-ELEVES-.pdf]]   
### Réponses
1. **Prompt après `su root` :**
   - Lorsque tu passes en super-utilisateur avec `su root`, le prompt change souvent pour indiquer que tu es root, généralement de `user@machine$` à `root@machine#`, avec le symbole `#` montrant que tu es en mode super-utilisateur.

2. **Commande `man` :**
   - La commande `man` (manual) affiche le manuel d’utilisation des commandes. Elle est utilisée pour consulter la documentation et les options disponibles pour chaque commande du système. Par exemple, `man ls` affiche le manuel de la commande `ls`.

3. **Création d’un nouvel utilisateur :**
   - Pour créer un utilisateur, utilise `useradd nom_utilisateur`, puis `passwd nom_utilisateur` pour définir le mot de passe. Par exemple : 
	 ```bash
	 useradd malaise
	 passwd malaise
	 ```
   - Pour supprimer l’utilisateur : `userdel malaise`.

4. **Pourquoi il est dangereux de travailler avec le compte root ?**
   - Travailler avec le compte root est risqué car il a tous les privilèges système, y compris la modification ou la suppression de fichiers critiques. Une simple erreur peut entraîner des dysfonctionnements majeurs du système.

5. **Commande `cd` sans argument :**
   - La commande `cd` sans argument te ramène dans ton répertoire personnel (`/home/userX`). C’est un raccourci pratique pour revenir à ton dossier utilisateur.

6. **Résultat de `cd` sans argument :**
   - La commande `cd` sans argument te ramène à ton répertoire personnel (par défaut `/home/userX`). C’est pratique pour revenir rapidement à ton espace personnel.

7. **Commande `pwd` dans `/usr/local/` :**
   - La commande `pwd` affiche le chemin absolu du répertoire courant, donc `/usr/local/` si tu y es déjà. C’est normal et sert à vérifier ta localisation dans l’arborescence.

8. **Commande `whoami` dans `/usr/local/` :**
   - La commande `whoami` affiche ton nom d’utilisateur actuel. Cela permet de vérifier sous quel compte tu es connecté, surtout utile quand tu as plusieurs sessions actives.

9. **Contenu du répertoire `/boot/` avec `ls` :**
   - a) Pour obtenir le nombre de fichiers : utilise `ls -l /boot | grep -v ^d | wc -l`.
   - b) Pour obtenir le nombre de répertoires : utilise `ls -l /boot | grep ^d | wc -l`.

10. **Création du répertoire `etudiant/` dans `/usr/` :**
   - Créer un répertoire ici sans droits administratifs (`root`) génère une erreur de permission : `Permission denied`. Seul l’utilisateur `root` peut créer/modifier des répertoires dans `/usr/`.
   - Créer un répertoire `etudiant` dans `/home/groupeX/` : cela fonctionne normalement car tu as les droits nécessaires dans ton répertoire personnel.

11. **Création et manipulation du fichier `bac.info.heh` :**
- Utiliser `touch bac.info.heh` pour créer un fichier vide dans ton répertoire `etudiant`.
- Impossible de supprimer le répertoire contenant des fichiers avec `rmdir`. Utilise `rm -r etudiant` pour supprimer récursivement le dossier et son contenu.

12. **Copie et suppression du fichier :**
- Copier et renommer : `cp bac.info.heh /tmp/infobac2`.
- Supprimer le répertoire `etudiant` avec `rmdir etudiant` si le répertoire est vide après les opérations.

13. **Commande `cal` sans argument :**
- Affiche le calendrier du mois en cours. Pour voir un calendrier spécifique : `cal 09 1995` (par exemple, pour septembre 1995).

14. **Équivalents des commandes reboot et halt avec `shutdown` :**
- Pour redémarrer : `shutdown -r now`.
- Pour éteindre : `shutdown -h now`.

15. **Explication des commandes diverses :**
- `which` : Localise l’exécutable d’une commande dans le chemin (PATH).
- `locate` : Recherche des fichiers par leur nom en utilisant une base de données pré-indexée.
- `date` : Affiche la date et l'heure actuelles du système.
- `clear` : Efface l’affichage du terminal.
- `head` : Affiche les premières lignes d’un fichier (par défaut 10 lignes).
- `tail` : Affiche les dernières lignes d’un fichier (par défaut 10 lignes).

16. **Éditeurs de texte en mode console :**
- Apprends les bases de `vim` avec la commande `vimtutor`, qui propose un tutoriel interactif pour se familiariser avec cet éditeur puissant. Alternativement, `nano` est plus simple pour débuter.
