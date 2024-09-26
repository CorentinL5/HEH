---
created: 2024-09-26
tags:
  - Lessons/School/HEH/Bloc2/Quad2
---

# # 📚  Commandes Linux par Labo
> **Création de la note à *`09:57`* le *`2024-09-26`.***
---

## Labo 01 : Commandes Fondamentales

1. **Connexion root**
   ```bash
   su root
   ```

2. **Afficher le manuel d'une commande**
   ```bash
   man <commande>
   ```

3. **Création et gestion d'utilisateurs**
   - Créer un utilisateur : 
     ```bash
     useradd <nom_utilisateur>
     passwd <nom_utilisateur>
     ```
   - Supprimer un utilisateur :
     ```bash
     userdel <nom_utilisateur>
     ```

4. **Se déplacer dans les répertoires**
   - Monter au répertoire parent :
     ```bash
     cd ..
     ```
   - Aller dans un répertoire spécifique :
     ```bash
     cd /home/userX
     ```

5. **Afficher le chemin actuel**
   ```bash
   pwd
   ```

6. **Afficher l'utilisateur actuel**
   ```bash
   whoami
   ```

7. **Visualiser le contenu d'un répertoire**
   ```bash
   ls /boot
   ```

8. **Créer un répertoire**
   ```bash
   mkdir <nom_dossier>
   ```

9. **Créer un fichier vide**
   ```bash
   touch <nom_fichier>
   ```

10. **Supprimer un fichier ou un répertoire**
    - Supprimer un fichier :
      ```bash
      rm <nom_fichier>
      ```
    - Supprimer un répertoire vide :
      ```bash
      rmdir <nom_dossier>
      ```
    - Supprimer un répertoire avec son contenu :
      ```bash
      rm -r <nom_dossier>
      ```

11. **Copier un fichier**
    ```bash
    cp <source> <destination>
    ```

12. **Afficher le calendrier**
    ```bash
    cal
    ```

13. **Redémarrer ou arrêter la machine**
    - Redémarrer :
      ```bash
      shutdown -r now
      ```
    - Éteindre :
      ```bash
      shutdown -h now
      ```

14. **Localiser un exécutable**
    ```bash
    which <commande>
    ```

15. **Rechercher des fichiers par nom**
    ```bash
    locate <nom_fichier>
    ```

16. **Afficher la date et l'heure actuelles**
    ```bash
    date
    ```

17. **Effacer l'écran du terminal**
    ```bash
    clear
    ```

18. **Afficher les premières ou dernières lignes d’un fichier**
    - Premières lignes :
      ```bash
      head <nom_fichier>
      ```
    - Dernières lignes :
      ```bash
      tail <nom_fichier>
      ```

---

## Labo 02 : Commandes Fondamentales (Suite)

1. **Recherche de fichiers avec locate**
   ```bash
   locate <nom_fichier>
   ```

2. **Mettre à jour la base de données de locate**
   ```bash
   updatedb
   ```

3. **Déterminer le type de données d’un fichier**
   ```bash
   file <nom_fichier>
   ```

4. **Afficher la taille des fichiers**
   ```bash
   du <nom_fichier>
   du -h <nom_fichier>  # Format lisible par l'humain
   ```

5. **Afficher le contenu d'un fichier**
   ```bash
   cat <nom_fichier>
   ```

6. **Déplacer un fichier**
   ```bash
   mv <source> <destination>
   ```

7. **Recherche de fichiers avec find**
   - Trouver un fichier par nom :
     ```bash
     find / -name <nom_fichier> 2>/dev/null
     ```
   - Trouver des fichiers modifiés récemment :
     ```bash
     find / -mtime -10
     ```

8. **Modifier le fichier de bannière de connexion**
   ```bash
   nano /etc/motd
   ```

9. **Localiser un binaire d’une commande**
   ```bash
   which <commande>
   ```

10. **Afficher les chemins des fichiers associés à une commande**
    ```bash
    whereis <commande>
    ```

11. **Afficher le terminal utilisé**
    ```bash
    tty
    ```

12. **Afficher les dernières connexions des utilisateurs**
    ```bash
    last
    ```

13. **Compter lignes, mots et caractères d’un fichier**
    ```bash
    wc <nom_fichier>
    wc -l <nom_fichier>  # Compter les lignes
    wc -w <nom_fichier>  # Compter les mots
    wc -c <nom_fichier>  # Compter les caractères
    ```

---

## Labo 03 : Gestion des fichiers

1. **Afficher les informations détaillées des fichiers :**
   ```bash
   ls -l
   ```
   - Affiche les permissions, nombre de liens, propriétaire, groupe, taille, date de modification, et nom des fichiers.

2. **Vérifier le type et les permissions d’un fichier :**
   ```bash
   ls -l <nom_fichier>
   ```

3. **Changer les permissions d'un fichier :**
   - Méthode symbolique :
     ```bash
     chmod u=rx,g=w,o= <fichier>
     ```
   - Méthode numérique :
     ```bash
     chmod 521 <fichier>
     ```

4. **Vérifier les permissions d’un fichier :**
   ```bash
   ls -l <fichier>
   ```

5. **Changer le propriétaire et le groupe d’un fichier :**
   - Modifier le propriétaire :
     ```bash
     chown <nouveau_propriétaire> <fichier>
     ```
   - Modifier le groupe :
     ```bash
     chgrp <nouveau_groupe> <fichier>
     ```

6. **Monter et démonter un système de fichiers :**
   - Démonter une partition :
     ```bash
     umount /chemin_du_point_de_montage
     ```
   - Monter une partition :
     ```bash
     mount /chemin_du_point_de_montage
     ```

7. **Rechercher des fichiers modifiés :**
   - Modifiés dans les 9 derniers jours :
     ```bash
     find / -mtime -9
     ```
   - Modifiés il y a exactement 9 jours :
     ```bash
     find / -mtime 9
     ```

8. **Copier un répertoire :**
   ```bash
   cp -r /source /destination
   ```

9. **Rechercher du texte dans les fichiers :**
   - Rechercher une chaîne spécifique dans un fichier :
     ```bash
     grep <mot> <fichier>
     ```
   - Rechercher récursivement dans un répertoire :
     ```bash
     grep -r <mot> /chemin_du_répertoire
     ```

10. **Visualiser le contenu d'un fichier :**
    ```bash
    cat <fichier>
    ```

11. **Afficher les permissions actuelles en numéraire avec `chmod` :**
    - Exemples de permissions avec `chmod` :
      - `chmod 777 <fichier>` : `rwxrwxrwx` (tous les accès pour tous).
      - `chmod 141 <fichier>` : `--xr----x`.
      - `chmod 471 <fichier>` : `r--rwx--x`.
      - `chmod 754 <fichier>` : `rwxr-xr--`.
      - `chmod 664 <fichier>` : `rw-rw-r--`.
      - `chmod 627 <fichier>` : `rw--w-rwx`.
      - `chmod 765 <fichier>` : `rwxrw-r-x`.
      - `chmod 462 <fichier>` : `r--rw--w-`.

---

## Labo 04 : Gestion des utilisateurs
1. **Vérifier les informations des utilisateurs (UID, GID, répertoire personnel) :**
   ```bash
   cat /etc/passwd
   ```

2. **Créer un utilisateur :**
   ```bash
   useradd <nom_utilisateur>
   ```

3. **Vérifier l’UID et les groupes d’un utilisateur :**
   ```bash
   id <nom_utilisateur>
   ```

4. **Vérifier les fichiers créés par un utilisateur :**
   ```bash
   touch <chemin/fichier>
   ls -l <chemin/fichier>
   ```

5. **Modifier un utilisateur :**
   - Modifier l’UID :
     ```bash
     usermod -u <nouvel_UID> <nom_utilisateur>
     ```
   - Supprimer un utilisateur :
     ```bash
     userdel <nom_utilisateur>
     ```
   - Supprimer l’utilisateur et son répertoire personnel :
     ```bash
     userdel -r <nom_utilisateur>
     ```

6. **Créer un utilisateur avec une date d’expiration :**
   ```bash
   useradd -e <YYYY-MM-DD> <nom_utilisateur>
   ```

7. **Configurer la validité du mot de passe :**
   ```bash
   chage -M <jours> <nom_utilisateur>
   ```

8. **Autres commandes utiles :**
   - Verrouiller un compte utilisateur :
     ```bash
     passwd -l <nom_utilisateur>
     ```
   - Afficher le nom de l’utilisateur connecté :
     ```bash
     logname
     ```
   - Lister les groupes d’un utilisateur :
     ```bash
     groups <nom_utilisateur>
     ```
   - Modifier les informations du compte utilisateur :
     ```bash
     chfn <nom_utilisateur>
     ```
   - Afficher les paramètres par défaut des nouveaux utilisateurs :
     ```bash
     useradd -D
     ```

9. **Gérer les groupes :**
   - Ajouter un groupe :
     ```bash
     groupadd <nom_groupe>
     ```
   - Ajouter un utilisateur à des groupes :
     ```bash
     usermod -aG <groupe1,groupe2> <nom_utilisateur>
     ```

10. **Vérification des permissions de fichiers et liens :**
    - Vérifier si un nom fait référence à un fichier ou à un répertoire :
      ```bash
      ls -ld <nom>
      ```

11. **Gérer les liens symboliques et durs :**
    - Créer un lien symbolique :
      ```bash
      ln -s <cible> <lien>
      ```
    - Créer un lien dur :
      ```bash
      ln <cible> <lien>
      ```

12. **Rechercher et afficher des fichiers modifiés :**
    - Rechercher des fichiers modifiés récemment :
      ```bash
      find / -mtime -<jours>
      ```

---

## Labo 05 : Les sauvegardes
1. **Commandes `tar` pour l'archivage :**
   - **Créer une archive :**
     ```bash
     tar -cvf <archive.tar> <chemin_dossier>
     ```
     - `-c` : Crée une archive.
     - `-v` : Affiche les fichiers archivés.
     - `-f` : Spécifie le nom du fichier d'archive.

   - **Lister le contenu d’une archive :**
     ```bash
     tar -tvf <archive.tar>
     ```
     - `-t` : Liste le contenu de l’archive.

   - **Restaurer des fichiers depuis une archive :**
     ```bash
     tar -xvf <archive.tar> -C <destination>
     ```
     - `-x` : Extrait les fichiers.
     - `-C` : Spécifie le répertoire de destination.

   - **Ajouter des fichiers modifiés ou nouveaux à une archive :**
     ```bash
     tar -uvf <archive.tar> <chemin_dossier>
     ```
     - `-u` : Met à jour l’archive avec les fichiers modifiés ou ajoutés.

   - **Créer une archive compressée (gzip) :**
     ```bash
     tar -czvf <archive.tar.gz> <chemin_dossier>
     ```
     - `-z` : Compresse avec `gzip`.

   - **Lister le contenu d’une archive compressée :**
     ```bash
     tar -tzvf <archive.tar.gz>
     ```

2. **Commandes de compression et décompression :**
   - **Compresser un fichier avec `gzip` :**
     ```bash
     gzip <fichier>
     ```

   - **Vérifier l’état de compression avec `gzip` :**
     ```bash
     gzip -l <fichier.gz>
     ```

   - **Décompresser un fichier avec `gunzip` :**
     ```bash
     gunzip <fichier.gz>
     ```

   - **Compresser avec `bzip2` :**
     ```bash
     bzip2 <fichier>
     ```

   - **Décompresser avec `bunzip2` :**
     ```bash
     bunzip2 <fichier.bz2>
     ```

3. **Utilisation de `rsync` pour la synchronisation :**
   - **Synchroniser des répertoires :**
     ```bash
     rsync -av <source> <destination>
     ```
     - `-a` : Mode archive (conserve les attributs).
     - `-v` : Mode verbeux (affiche les fichiers).

   - **Synchroniser et supprimer les fichiers absents dans la source :**
     ```bash
     rsync -av --delete <source> <destination>
     ```
     - `--delete` : Supprime les fichiers dans la destination qui ne sont pas dans la source.

---

## labo 06 : 