---
created: 2024-09-26
tags:
  - Lessons/School/HEH/Bloc2/Quad2
---

# # 📚  Commandes Linux
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

