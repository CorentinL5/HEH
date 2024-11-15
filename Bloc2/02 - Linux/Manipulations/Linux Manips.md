---
created: 2024-09-26
tags:
  - Lessons/School/HEH/Bloc2/Quad1
---

# # 📚  Linux Manips
> **Création de la note à *`08:34`* le *`2024-09-26`.***
---

# 📝 Prise de Notes

---
## Manip one - Cmd de bases
### PDF
![[01_Labo_Linux_Les_commandes_de_bases-ELEVES-.pdf#page=1|noscroll]]
![[01_Labo_Linux_Les_commandes_de_bases-ELEVES-.pdf#page=2|noscroll]]
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
   - Créer un répertoire ici sans droits administratifs (`root`) génère une erreur de permission : `Permission denied`. Seul l’utilisateur `root` peut créer/modifier des répertoires dans `/usr/`.![[Pasted image 20240926092946.png]]
   - Créer un répertoire `etudiant` dans `/home/groupeX/` : cela fonctionne normalement car tu as les droits nécessaires dans ton répertoire personnel.

11. **Création et manipulation du fichier `bac.info.heh` :**
- Utiliser `touch bac.info.heh` pour créer un fichier vide dans ton répertoire `etudiant`.
- Impossible de supprimer le répertoire contenant des fichiers avec `rmdir`. Utilise `rm -r etudiant` pour supprimer récursivement le dossier et son contenu.

12. **Copie et suppression du fichier :**
- Copier et renommer : `cp bac.info.heh /tmp/infobac2`.
- Supprimer le répertoire `etudiant` avec `rmdir etudiant` si le répertoire est vide après les opérations.
  ![[Pasted image 20240926093345.png]]

13. **Commande `cal` :**
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

---

## Manip two - Cmd de bases suite
### PDF
![[02_Labo_Linux_Les_commandes_de_bases_suite-ELEVES-.pdf#page=1|noscroll]]
![[02_Labo_Linux_Les_commandes_de_bases_suite-ELEVES-.pdf#page=2|noscroll]]
### Réponses
1. **Prompt après connexion en `userX` :**
   - Le prompt affiché dépend du shell et de la configuration de l'utilisateur. En général, il ressemble à : `userX@machine:~$`, indiquant le nom de l’utilisateur, le nom de la machine et le répertoire courant (`~` pour le dossier personnel).

2. **Recherche de fichiers avec `locate` :**
   - a) Pour trouver `crontab`, utilise la commande : 
     ```bash
     locate crontab
     ```
     - Les fichiers `crontab` se trouvent souvent dans `/etc/` et `/usr/bin/`.
   - b) Pour `chown`, utilise :
     ```bash
     locate chown
     ```
     - Le fichier `chown` se trouve généralement dans `/usr/bin/`.
   - c) **Créer un fichier et essayer de le trouver avec `locate` :**
     - Après avoir créé un fichier, `locate` ne le trouvera pas immédiatement car il utilise une base de données qui n'est pas mise à jour en temps réel. Utilise `updatedb` pour mettre à jour cette base de données et ensuite `locate` pour retrouver le fichier.

3. **Détermination du type de données avec `file` :**
   - a) Pour `bikibean.zip` :
     ```bash
     file bikibean.zip
     ```
     - Cette commande indiquera probablement "Zip archive data".
   - b) Pour `Agilent.html` :
     ```bash
     file Agilent.html
     ```
     - Résultat attendu : "HTML document, ASCII text".
   - c) Pour `grub2.cfg` :
     ```bash
     file grub2.cfg
     ```
     - Cela indiquera quelque chose comme "ASCII text".

4. **Taille des fichiers avec `du` :**
   - a) Utiliser `du` pour connaître la taille :
     ```bash
     du Agilent.html
     du bikibean.zip
     ```
   - b) Option pour afficher des tailles lisibles :
     - Utilise `-h` (human-readable) : 
     ```bash
     du -h Agilent.html
     du -h bikibean.zip
     ```

5. **Visualiser le contenu de `/etc/fstab` :**
   - Utilise la commande :
     ```bash
     cat /etc/fstab
     ```
   - Cette commande affiche le contenu du fichier de configuration des systèmes de fichiers.

6. **Déplacer `bikibean.zip` vers `/tmp` avec `mv` :**
   - Utilise la commande :
     ```bash
     mv bikibean.zip /tmp
     ```

7. **Recherche de fichiers avec `find` :**
   - a) Pour trouver le répertoire de `fstab` :
     ```bash
     find / -name fstab 
     ```
     - Ce fichier se trouve généralement dans `/etc/`.
   - b) Fichiers modifiés au cours des 10 derniers jours :
     ```bash
     find / -mtime -10
     ```
   - c) Comportement de `find` sans chemin spécifié :
     - Si aucun chemin n’est indiqué, `find` effectue la recherche dans le répertoire courant (`.`) et ses sous-répertoires.

8. **Écrire un message dans la bannière de connexion (`motd`) :**
   - Édite le fichier `/etc/motd` pour ajouter ton message. Pour vérifier, ouvre une nouvelle session ou utilise :
     ```bash
     nano /etc/motd
     ```

9. **Emplacement du binaire de `passwd` avec `which` :**
   - Utilise :
     ```bash
     which passwd
     ```
     - Il se trouve souvent dans `/usr/bin/passwd`.
10. **Informations de `whereis` :**
    - La commande `whereis` affiche les emplacements du binaire, du code source et de la page de manuel d’une commande. Par exemple :
      ```bash
      whereis ls
      ```

11. **Informations de `tty` :**
    - La commande `tty` indique le fichier de terminal associé à la session en cours, souvent quelque chose comme `/dev/pts/0`.

12. **Fonction de `last` :**
    - La commande `last` affiche les derniers utilisateurs qui se sont connectés au système, avec la date et l'heure de la connexion.

13. **Fonction de `wc` :**
    - La commande `wc` (word count) compte les lignes, mots et caractères d’un fichier. Par exemple :
      ```bash
      wc filename
      ```
      - Options : `-l` pour les lignes, `-w` pour les mots, et `-c` pour les caractères.

---

## Manip three - Gestion de Fichiers
### PDF
![[03_Labo_Linux_Permissions_acces-ELEVES-.pdf#page=1|noscroll]]
![[03_Labo_Linux_Permissions_acces-ELEVES-.pdf#page=2|noscroll]]
### Réponses
1. **Informations données par la commande `ls -l` :**
   - La commande `ls -l` affiche des informations détaillées sur les fichiers et répertoires. Exemple :
     ```
     -rw-r--r-- 1 userX groupX 1234 Sep 26 08:34 example.txt
     ```
     - `-rw-r--r--` : Permissions du fichier (lecture, écriture, exécution).
     - `1` : Nombre de liens (hard links).
     - `userX` : Propriétaire du fichier.
     - `groupX` : Groupe propriétaire du fichier.
     - `1234` : Taille du fichier en octets.
     - `Sep 26 08:34` : Date et heure de la dernière modification.
     - `example.txt` : Nom du fichier.

2. **Permissions d’accès et type de fichier :**
   - a) `systemd` : Binaire ou script d'initialisation. Permissions généralement en lecture et exécution (`r-xr-xr-x`).
   - b) `inittab` : Fichier de configuration (`rw-r--r--`), fichier texte.
   - c) `skel` : Répertoire modèle (`rwxr-xr-x`), utilisé pour les nouveaux comptes utilisateurs.

3. **Permissions par défaut des fichiers créés :**
   - a) **Root :** Généralement `rw-r--r--` (644).
   - b) **Utilisateur quelconque :** Généralement `rw-r--r--` (644).
   - c) Un utilisateur ne peut pas toujours lire les fichiers créés par root, car root peut restreindre les droits d’accès (ex. : `chmod 600` pour `rw-------`).

4. **Permissions par défaut des répertoires créés :**
   - a) **Root :** Généralement `rwxr-xr-x` (755).
   - b) **Utilisateur quelconque :** Généralement `rwxr-xr-x` (755).
   - c) L’exécution sur un répertoire permet de naviguer dans ce répertoire et d’exécuter des commandes sur ses fichiers. C’est essentiel pour pouvoir accéder au contenu.

5. **Modifier les permissions de `droituserX` :**
   - a) **Première méthode (symbolique) :**
     ```bash
     chmod u=rx,g=w,o= droituserX
     ```
   - b) **Deuxième méthode (numérique) :**
     ```bash
     chmod 521 droituserX
     ```
   - c) **Vérifier les droits :**
     ```bash
     ls -l droituserX
     ```
   - d) Sans préciser `u`, `g`, ou `o`, `chmod` change les permissions de toutes les catégories (`ugo`).

6. **Réinitialiser les droits par défaut et questions sur les permissions :**
   - a) Seul le propriétaire ou root peut modifier les permissions d’un fichier.
   - b) Si root change le groupe en `root`, userX perd les permissions de modification, sauf s’il reste propriétaire.
   - c) Si root est propriétaire et le groupe est `userX`, un utilisateur de ce groupe ne peut pas modifier le fichier.
   - d) Seul le propriétaire du fichier ou root peut modifier les permissions.
   - e) En général, le propriétaire ou root peut modifier les permissions d’un fichier.

7. **Montage et démontage de `/home` :**
   - Pour démonter :
     ```bash
     umount /home
     ```
   - Pour remonter :
     ```bash
     mount /home
     ```
   - Pour vérifier le système de fichiers et la capacité :
     ```bash
     mount | grep /home
     df -h /home
     ```

8. **Modification ou suppression de fichiers appartenant à root :**
   - Un utilisateur ne peut pas modifier ou supprimer un fichier appartenant à root, même dans son propre répertoire, à moins d’avoir les permissions appropriées.

9. **Permissions par défaut pour un fichier créé :**
   - Réponse : **c) 644** (`rw-r--r--`).

10. **Fichiers modifiés au cours des 9 derniers jours :**
    ```bash
    find / -mtime -9
    ```

11. **Fichiers modifiés il y a exactement 9 jours :**
    ```bash
    find / -mtime 9
    ```

12. **Copier `/home` dans `/usr/homebackup` :**
    ```bash
    cp -r /home /usr/homebackup
    ```

13. **Recherche dans un fichier avec `grep` :**
    - a) Trouver `userX` dans `/etc/passwd` :
      ```bash
      grep userX /etc/passwd
      ```
    - b) Trouver `userX` dans tous les fichiers de `/etc` :
      ```bash
      grep -r userX /etc
      ```

14. **Permissions des commandes `chmod` :**
   - `chmod 777 fichier` : `rwxrwxrwx`
   - `chmod 141 fichier` : `--xr----x`
   - `chmod 471 fichier` : `r--rwx--x`
   - `chmod 754 fichier` : `rwxr-xr--`
   - `chmod 664 fichier` : `rw-rw-r--`
   - `chmod 627 fichier` : `rw--w-rwx`
   - `chmod 765 fichier` : `rwxrw-r-x`
   - `chmod 462 fichier` : `r--rw--w-`

15. **Structure des fichiers de configuration :**
   - **/etc/fstab** : Contient les informations sur les systèmes de fichiers à monter automatiquement au démarrage.
   - **/etc/passwd** : Contient les informations des utilisateurs (nom, UID, GID, etc.).
   - **/etc/shadow** : Contient les mots de passe cryptés des utilisateurs et des informations supplémentaires sur les comptes.
   - **/etc/group** : Contient les groupes du système et les utilisateurs associés à chaque groupe.

---
## Manip four - gestion des utilisateurs
### PDF 
![[04_Labo_Linux_Gestion_des_utilisateurs_-ELEVES-.pdf#page=1|noscroll]]
![[04_Labo_Linux_Gestion_des_utilisateurs_-ELEVES-.pdf#page=2|noscroll]]
### Réponses
1. **UID, GID et répertoire personnel des utilisateurs :**
   - a) **root** : 
     - UID : 0
     - GID : 0
     - Répertoire personnel : `/root`
   - b) **shutdown** :
     - UID : généralement 6
     - GID : généralement 6
     - Répertoire personnel : `/sbin` ou non spécifié
   - c) **nobody** :
     - UID : généralement 65534
     - GID : généralement 65534
     - Répertoire personnel : `/nonexistent` ou `/`

2. **Création d’un utilisateur `userX` et vérification :**
   - Pour créer l’utilisateur : 
     ```bash
     useradd userX
     ```
   - Pour vérifier la connexion :
     ```bash
     su - userX
     ```
   - Pour vérifier la création du répertoire personnel : 
     ```bash
     ls /home/userX
     ```

3. **UID réservés et utilisateurs réels :**
   - Les UID inférieurs à 1000 sont généralement réservés pour les comptes systèmes et services. Les utilisateurs "réels" commencent à partir de l’UID 1000.

4. **Création d’un compte existant :**
   - Si tu essaies de créer un utilisateur déjà existant :
     ```bash
     useradd userX
     ```
     - Réponse du système : `useradd: user 'userX' already exists`.

5. **Afficher l’UID et les groupes de `userX` :**
   ```bash
   id userX
   ```

6. **Création de fichiers par `userX` et vérification :**
   - Créer les fichiers : 
     ```bash
     touch /home/userX/essai
     touch /tmp/essai2
     ```
   - Vérifier le propriétaire :
     ```bash
     ls -l /home/userX/essai
     ls -l /tmp/essai2
     ```

7. **Modification et suppression du compte `userX` :**
   - a) Modifier l’UID de `userX` :
     ```bash
     usermod -u 1055 userX
     ```
   - b) Vérifier l’association des fichiers :
     ```bash
     ls -l /home/userX/essai
     ls -l /tmp/essai2
     ```
   - c) Supprimer le compte `userX` :
     ```bash
     userdel userX
     ```
     - Par défaut, le répertoire personnel n’est pas supprimé, sauf si tu utilises l’option `-r`.

8. **Création d’un compte utilisateur valide jusqu’à demain 18h :**
   ```bash
   useradd -e $(date -d "tomorrow 18:00" +%F) userX_temp
   ```

9. **Créer un compte avec changement de mot de passe tous les trois mois :**
   ```bash
   useradd userY
   chage -M 90 userY
   ```

10. **Fonctions des commandes :**
   - a) `passwd -l groupeX` : Verrouille le mot de passe du compte `groupeX`, empêchant l’accès.
   - b) `logname` : Affiche le nom de l’utilisateur connecté actuellement.
   - c) `groups` : Liste les groupes auxquels appartient l’utilisateur courant.
   - d) `chfn` : Change les informations du compte utilisateur (nom complet, téléphone, etc.).
   - e) `useradd -D` : Affiche ou modifie les paramètres par défaut des nouveaux comptes utilisateurs.

11. **Créer un groupe `graduatX` :**
    ```bash
    groupadd graduatX
    ```

12. **Modification du groupe d’un utilisateur :**
   - a) Ajouter `userX` aux groupes `bachelier` et `userX` :
     ```bash
     usermod -aG bachelier,userX userX
     ```
   - b) Vérifier l’appartenance :
     ```bash
     id userX
     ```

13. **Définition de `userX` dans `/etc/passwd` :**
   - a) Mot de passe crypté : Se trouve dans `/etc/shadow`, généralement marqué par un `x` dans `/etc/passwd`.
   - b) Numéro d’utilisateur : UID.
   - c) Numéro de groupe : GID.
   - d) Nom complet de l’utilisateur : Peut inclure des détails comme "User X".
   - e) Shell de l’utilisateur : `/bin/bash` ou autre shell par défaut.
   - f) Exemples de comptes non associés à une personne : `nobody`, `daemon`.

14. **`chmod 770 test` modifie-t-il le fichier ou le répertoire ?**
   - Pour différencier, utilise `ls -ld test`. Le `d` initial indique un répertoire.

15. **Création de liens vers des fichiers du répertoire `/root` :**
   - Un utilisateur normal ne peut pas créer de lien direct vers des fichiers dans `/root` sans autorisations spécifiques.

16. **Permissions des liens durs et symboliques :**
   - **Lien dur** : Les permissions du fichier original ne changent pas si celles du lien dur changent.
   - **Lien symbolique** : Les permissions du lien symbolique sont indépendantes des permissions du fichier cible.

17. **Modification du contenu via un lien symbolique :**
   - Même si le lien symbolique a `777`, on ne peut pas modifier le fichier si le fichier lui-même n’a pas les permissions d’écriture.

18. **Lien symbolique créé par root :**
   - a) L’utilisateur peut l’utiliser s’il a les droits nécessaires sur le fichier cible.
   - b) Le lien apparaît de la même manière dans le répertoire, peu importe qui liste.

19. **Création d’un utilisateur par un membre du groupe root :**
   - Seul root (ou un utilisateur avec privilèges administratifs spécifiques) peut créer de nouveaux utilisateurs, même si l’utilisateur appartient au groupe root.

---

## Manip five - Les Sauvegardes
### PDF
![[05_Labo_Linux_sauvegarde-ELEVES-.pdf]]
### Réponses
1. **Différence entre une sauvegarde incrémentale et différentielle :**
   - **Sauvegarde incrémentale** : Sauvegarde uniquement les fichiers modifiés depuis la dernière sauvegarde (qu'elle soit complète ou incrémentale). Elle est rapide et utilise moins d'espace, mais la restauration est plus complexe car il faut appliquer chaque sauvegarde incrémentale dans l'ordre.
   - **Sauvegarde différentielle** : Sauvegarde tous les fichiers modifiés depuis la dernière sauvegarde complète. Elle est plus lente et utilise plus d'espace qu'une sauvegarde incrémentale, mais la restauration est plus simple car il suffit d'utiliser la dernière sauvegarde complète et la dernière sauvegarde différentielle.

2. **Création d'une arborescence de fichiers :**
   - Connectez vous en tant que `userX` :
     ```bash
     su - userX
     ```
   - Créez des répertoires et fichiers dans `/home/userX` :
     ```bash
     mkdir /home/userX/docs /home/userX/images
     touch /home/userX/docs/file1.txt /home/userX/images/image1.png
     ```

3. **Archivage avec `tar` :**
   - a) **Archiver l’arborescence** :
     ```bash
     tar -cvf /tmp/userX.tar /home/userX/
     ```
   - b) **Lister le contenu de l’archive** :
     ```bash
     tar -tvf /tmp/userX.tar
     ```
   - c) **Détruire un fichier et le restaurer depuis l’archive** :
     - Supprimer un fichier :
       ```bash
       rm /home/userX/docs/file1.txt
       ```
     - Restaurer le fichier depuis l’archive :
       ```bash
       tar -xvf /tmp/userX.tar -C /
       ```

   - d) **Sauvegarde incrémentale des modifications** :
     - 1) Mettre à jour l’archive avec les nouveaux fichiers ou ceux modifiés :
       ```bash
       tar -uvf /tmp/userX.tar /home/userX/
       ```
     - 2) **Vérifier le bon fonctionnement** :
       - Listez de nouveau le contenu de l'archive pour vérifier l'ajout des fichiers modifiés :
         ```bash
         tar -tvf /tmp/userX.tar
         ```
  
   - e) **Détruire tous les fichiers et les restaurer** :
     - Supprimer tous les fichiers dans `/home/userX` :
       ```bash
       rm -rf /home/userX/*
       ```
     - Restaurer tout depuis l’archive :
       ```bash
       tar -xvf /tmp/userX.tar -C /
       ```

   - f) **Archivage compressé dans `/var/sauve/`** :
     - Créer un archive compressée de `/home/` :
       ```bash
       tar -czvf /var/sauve/homeX.tar.gz /home/
       ```
     - Lister le contenu de l’archive compressée :
       ```bash
       tar -tzvf /var/sauve/homeX.tar.gz
       ```

   - g) **À partir de quelle étape dispose-t-on d’une sauvegarde ?**
     - Dès que l'archive initiale est créée (étape 3.a), on dispose d'une sauvegarde.

4. **Compression de données :**
   - a) **Compresser un fichier avec `gzip` :**
     ```bash
     gzip <nom_du_fichier>
     ```
   - b) **Vérifier l’état de compression :**
     - Affiche les détails de compression avec `gzip -l` :
       ```bash
       gzip -l <nom_du_fichier.gz>
       ```
   - c) **Décompresser le fichier avec `gunzip` :**
     ```bash
     gunzip <nom_du_fichier.gz>
     ```
   - d) **Compresser et décompresser avec `bzip2` :**
     - Compresser avec `bzip2` :
       ```bash
       bzip2 <nom_du_fichier>
       ```
     - Décompresser avec `bunzip2` :
       ```bash
       bunzip2 <nom_du_fichier.bz2>
       ```

5. **Utilisation de `rsync` :**
   - a) **Copier le contenu de `/home/userX/` vers `/tmp/backup/` :**
     ```bash
     rsync -av /home/userX/ /tmp/backup/
     ```
   - b) **Ajouter deux fichiers et synchroniser :**
     - Ajouter des fichiers et supprimer un fichier :
       ```bash
       touch /home/userX/newfile1.txt /home/userX/newfile2.txt
       rm /home/userX/oldfile.txt
       ```
     - Synchroniser les répertoires :
       ```bash
       rsync -av --delete /home/userX/ /tmp/backup/
       ```
   - c) **Vérification des fichiers supprimés :**
     - Le fichier supprimé dans `/home/userX` n’apparaîtra plus dans `/tmp/backup/` si l’option `--delete` a été utilisée lors de la synchronisation avec `rsync`.

---

## Manip six - Gestion des processus
### PDF
![[06_Labo_Linux_processus-ELEVES-.pdf]]
### Réponses
1. **Affichez l’ensemble des processus en cours de fonctionnement sur votre ordinateur (ps).**

   Utilisez la commande suivante pour afficher tous les processus en cours d’exécution :

   ```bash
   ps aux
   ```

   Cela affichera une liste complète des processus avec des informations telles que l'utilisateur, le PID, l'utilisation du CPU et de la mémoire, etc.

2. **Affichez de manière dynamique les processus en cours de fonctionnement sur votre ordinateur (top).**

   Exécutez la commande `top` pour afficher une vue dynamique des processus :

   ```bash
   top
   ```

   Cela mettra à jour en temps réel l’utilisation des ressources du système par les processus.

3. **Essayez la commande yes, elle ne fait rien d'autre qu’afficher des Y à l'écran.**

   a) **Testez-la.**

   Exécutez la commande `yes` :

   ```bash
   yes
   ```

   Cela affichera une série infinie de "Y" à l'écran.

   b) **Comment interrompre son exécution sans utiliser la commande kill ?**

   Vous pouvez interrompre l'exécution en utilisant la combinaison de touches `[Ctrl]` + `[C]`.

   c) **Comment rediriger l’affichage d’une commande vers le néant (vers /dev/null).**

   Vous pouvez rediriger la sortie de la commande `yes` vers `/dev/null` pour éviter qu'elle n'affiche quoi que ce soit :

   ```bash
   yes > /dev/null
   ```

   d) **Lancez le processus du point c) en tâche de fond. Que se passe-t-il ? Justifiez. Pouvez-vous stopper ce processus avec la combinaison de touche [Ctrl] + [ C ].**

   Lancez la commande en tâche de fond avec le caractère `&` :

   ```bash
   yes > /dev/null &
   ```

   Le processus est exécuté en arrière-plan et vous récupérez immédiatement le contrôle de la ligne de commande. Cependant, vous ne pouvez **pas** arrêter ce processus avec `[Ctrl]` + `[C]` car cela ne fonctionne que pour les processus au premier plan.

   e) **Vérifiez que la commande du point d) s'exécute bien en tâche de fond (ps ou job).**

   Utilisez l'une des deux commandes suivantes pour vérifier l'existence du processus en arrière-plan :

   - Avec `ps` :

     ```bash
     ps aux | grep yes
     ```

   - Avec `jobs` (affiche les processus lancés en tâche de fond dans cette session) :

     ```bash
     jobs
     ```

4. **Exécutez la commande suivante : yes > /dev/null**

   a) **Suspendez (et non pas arrêter) son exécution. [Ctrl] + [Z].**

   Exécutez la commande et suspendez-la avec `[Ctrl]` + `[Z]` :

   ```bash
   yes > /dev/null
   ```

   Ensuite, appuyez sur `[Ctrl]` + `[Z]` pour suspendre le processus.

   b) **Ensuite, continuez son exécution (fg).**

   Pour reprendre l'exécution de la commande au premier plan, utilisez la commande `fg` :

   ```bash
   fg
   ```

   c) **Suspendez-la à nouveau puis relancez-la mais cette fois en tâche de fond (bg).**

   Après avoir suspendu à nouveau le processus avec `[Ctrl]` + `[Z]`, relancez-le en arrière-plan avec la commande `bg` :

   ```bash
   bg
   ```

   d) **Vérifiez que cette commande s'exécute bien en tâche de fond puis arrêtez-la.**

   Utilisez `jobs` ou `ps` pour vérifier que le processus fonctionne en arrière-plan, puis arrêtez-le avec `kill` :

   ```bash
   ps aux | grep yes  # Pour obtenir le PID
   kill [PID]
   ```

5. **On exécute la commande suivante : `sleep 200 &`**

   a) **Quel est son processus parent ?**

   Pour déterminer le processus parent de `sleep`, utilisez la commande suivante (en remplaçant `[PID]` par le PID du processus `sleep`) :

   ```bash
   ps -o ppid= -p [PID]
   ```

   Cela vous indiquera le PID du processus parent (souvent, c'est le shell dans lequel vous avez lancé la commande).

   b) **"Tuez" cette application.**

   Vous pouvez arrêter le processus `sleep` avec la commande `kill` :

   ```bash
   kill [PID]
   ```

6. **Utilisez une console texte afin de connecter un utilisateur quelconque. Tuez son shell de connexion. Que se passe-t-il ?**

   Si vous tuez le processus du shell de l'utilisateur, sa session sera immédiatement déconnectée. Cela équivaut à fermer brutalement la session utilisateur.

   Exemple pour tuer un shell :

   ```bash
   ps aux | grep bash  # Identifiez le processus du shell
   kill [PID]
   ```

7. **En analysant le résultat de la commande `ps aux`, indiquez, selon votre avis, quelles sont les applications susceptibles d'être des démons.**

   Les démons (services systèmes) peuvent être identifiés par les critères suivants :
   - Ils sont souvent exécutés par l’utilisateur `root`.
   - Ils n’ont pas de terminal de contrôle associé (`?` dans la colonne `TTY`).
   - Ils ont des noms de processus typiques comme `crond`, `sshd`, `systemd`, `atd`, etc.

   Exemple de démon :

   ```bash
   root      1  0.0  0.3 165780  8260 ?        Ss   10:00   0:02 /usr/lib/systemd/systemd
   ```

8. **Lancez la commande suivante : `sleep 1500 &`**

   a) **Modifiez la priorité de la commande `sleep` (top).**

   Ouvrez `top`, trouvez le processus `sleep`, puis modifiez sa priorité avec la commande `r` dans `top`, ce qui permet de modifier la **niceness** du processus.

   Une autre option serait d’utiliser `renice` directement :

   ```bash
   renice 10 [PID]
   ```

   Cela diminue la priorité du processus `sleep`.

9. **Lancez la commande `top` et répondez aux questions suivantes :**

   a) **Combien de processus sont en cours sur la machine ?**

   En haut de l’interface `top`, vous verrez une ligne qui indique quelque chose comme : `Tasks: 150 total`, ce qui vous donne le nombre de processus en cours.

   b) **Quelle est la quantité de mémoire libre ?**

   La mémoire libre est indiquée sur la ligne `Mem`. Par exemple :

   ```
   Mem :  16000 total, 8000 free, ...
   ```

   c) **Quelle est la quantité de mémoire swap disponible ?**

   La mémoire swap disponible est indiquée sur la ligne `Swap` :

   ```
   Swap:  4096 total, 2048 free, ...
   ```

   d) **Quelle est la mémoire physique utilisée par la tâche `sleep` ?**

   Dans `top`, recherchez la colonne `RES` (mémoire résidente) pour le processus `sleep`, cela correspond à la mémoire physique utilisée.

   e) **Quel est l'état de la tâche ?**

   L'état du processus est indiqué dans la colonne `S`. Pour `sleep`, l'état sera probablement `S` (sleeping).

---

## Manip seven - Systèmes de fichiers
### PDF
![[07_LaboLinux_fichiers_et_systeme_de_fichiers-ELEVES-.pdf]]
### Réponses
1. Créer un fichier quelconque avec l’utilisateur root. Modifier l’utilisateur et le groupe propriétaire de ce fichier de manière à ce qu’il soit associé à l’utilisateur userX et au groupe newgroup.

```bash
# Créer un fichier avec l'utilisateur root
 touch /tmp/monfichier

# Modifier l'utilisateur et le groupe propriétaire du fichier
 chown userX:newgroup /tmp/monfichier
```

Explication :  
`touch` crée un fichier vide. Ensuite, `chown` change le propriétaire (`userX`) et le groupe (`newgroup`) du fichier.

2. Quelles sont les permissions d’accès associées au répertoire /tmp ?

Le répertoire `/tmp` a généralement les permissions suivantes :

```bash
drwxrwxrwt
```

- Le `t` à la fin représente le **sticky bit**, ce qui signifie que seul le propriétaire du fichier ou l'utilisateur root peut le supprimer, même si d'autres utilisateurs ont les permissions d'écriture dans `/tmp`.
- Les permissions complètes sont : **lecture, écriture, et exécution** pour tous les utilisateurs, mais avec cette restriction de suppression due au sticky bit.

3. Quelle est la valeur du umask ? Modifier le umask de manière à ce que les fichiers nouvellement créés aient les permissions par défaut suivantes : rw- -w- r--.

Vous pouvez vérifier la valeur actuelle du `umask` en exécutant :

```bash
umask
```

Pour modifier le umask afin que les fichiers nouvellement créés aient les permissions `rw- -w- r--` (qui correspond à 642), vous devez définir le umask à 0135 :

```bash
umask 0135
```

Explication :  
Le `umask` définit quelles permissions doivent être **retirées** lors de la création de fichiers. Ici, on soustrait de 666 (permissions par défaut pour les fichiers).

4. Modifier le umask de manière à ce que, par défaut, seul le propriétaire d’un fichier dispose des droits en lecture et écriture sur ce fichier. Les autres utilisateurs du système ne doivent avoir aucun droit sur le fichier.

Pour atteindre cet objectif, vous devez définir le `umask` à 0077 :

```bash
umask 0077
```

Explication :  
Cela garantit que les fichiers sont créés avec des permissions `rw-------` (seul le propriétaire a les droits).


5. Quels sont les différents systèmes de fichiers montés, à quels fichiers spéciaux sont-ils associés, quels sont leurs répertoires de montage (mount) ?

Utilisez la commande suivante pour afficher les systèmes de fichiers montés :

```bash
mount
```

Ou bien :

```bash
df -hT
```

Cela vous montrera une liste des systèmes de fichiers, avec les informations suivantes :
- **Type de système de fichiers** (par exemple, `ext4`, `tmpfs`, `xfs`, etc.)
- **Fichiers spéciaux** (par exemple, `/dev/sda1`, `/dev/sda2`)
- **Points de montage** (par exemple, `/`, `/home`, `/tmp`)

6. Affichez l’espace occupé par les différentes partitions de votre système (df). Quels résultats obtenez-vous ?

Exécutez la commande :

```bash
df -h
```

Cela affiche l'espace disque utilisé et disponible sur chaque système de fichiers monté, ainsi que le pourcentage d'utilisation.

7. Quelles sont les tailles (en octets) de blocs qu’il est possible de définir dans un système de fichiers de type ext4 ?

Pour un système de fichiers de type ext4, les tailles de blocs possibles sont :

- 1024 octets
- 2048 octets
- 4096 octets
- 8192 octets (rare)

Vous pouvez vérifier la taille des blocs d’un système de fichiers existant avec la commande suivante :

```bash
 tune2fs -l /dev/sdX | grep 'Block size'
```

8. L'utilisateur pierre est en train de visualiser son fichier `.profile` (/home/pierre/profile) grâce à la commande `more`. L'administrateur peut-il démonter le FS `/home` ? Si non, pourquoi ? Que doit-il faire pour y arriver ?

Non, l’administrateur **ne peut pas démonter** le système de fichiers `/home` tant que le fichier est en cours d’utilisation.

Pour voir quel processus utilise ce fichier, vous pouvez utiliser la commande `lsof` ou `fuser` :

```bash
lsof /home
```
ou

```bash
fuser -m /home
```

Pour démonter `/home`, vous devez soit :
1. Demander à l'utilisateur de fermer le fichier.
2. Forcer la fermeture avec :

```bash
fuser -k /home
```

9. Réalisez la vérification d’une partition de votre système (fsck).

Pour vérifier une partition, vous pouvez utiliser la commande `fsck` (file system check). Par exemple :

```bash
 fsck /dev/sda1
```

Cela vérifie et répare les erreurs sur la partition `/dev/sda1`. Assurez-vous que la partition n'est pas montée lors de l'exécution de cette commande.

10. Affichez les informations sur le système de fichiers d’une partition (dumpe2fs).

La commande suivante affiche les informations du système de fichiers d’une partition spécifique :

```bash
 dumpe2fs /dev/sda1
```

Vous y trouverez des informations comme :
- **Nombre de blocs et d'inodes libres**
- **Nombre de blocs par groupe de blocs**
- **Date de la dernière vérification du système de fichiers**


11. Créez, sur un nouveau disque dur virtuel, un système de fichier ext4 dont les blocs ont une taille de 4096 octets (mkfs.ext4).

Pour créer un système de fichiers ext4 avec une taille de bloc de 4096 octets, utilisez la commande suivante :

```bash
 mkfs.ext4 -b 4096 /dev/sdX
```

Remplacez `/dev/sdX` par le nom du périphérique du disque dur virtuel.

---

## Manip eight - Ordonnancement de travaux
### PDF
![[08_Labo_Linux_at,cron_-ELEVES-.pdf]]
### Réponses
1. **Est-ce que l'application "crond" est active (ps) ? Si oui, quel est son PID ? Sinon comment la démarrer ?**

   - Pour vérifier si `crond` est actif et obtenir son PID, vous pouvez utiliser la commande suivante :

 ```bash
	 ps aux | grep crond
 ```

     Si `crond` est actif, vous verrez une ligne avec son **PID** dans la deuxième colonne. Sinon, pour démarrer le service `crond` :

 ```bash
	systemctl start crond
 ```

2. **Crontab**
   
   a) **Quel est le nom du fichier "log" utilisé par le démon crond ?**
   
   Le fichier log utilisé par `crond` est généralement `/var/log/cron`.

   b) **Visualisez-le. Effacez son contenu s'il n'est pas vide.**

   Pour visualiser le fichier :

   ```bash
	cat /var/log/cron
   ```

   Pour effacer son contenu (si vous avez les droits) :

   ```bash
	truncate -s 0 /var/log/cron
   ```

   c) **Que se passe-t-il si vous placez un script dans le répertoire `/etc/cron.daily` ?**

   Les scripts placés dans `/etc/cron.daily` sont exécutés automatiquement une fois par jour par le démon `crond`.

3. **Configurez, sous le compte de userX et à l’aide de crontab les actions suivantes :**

   a) **Une tâche périodique qui doit écrire, toutes les minutes, le message Bonjour suivi de la date, dans le fichier `/tmp/date.cron`.**

   Sous l’utilisateur `userX`, ouvrez l'éditeur de crontab :

   ```bash
   crontab -e
   ```

   Ajoutez la ligne suivante pour exécuter la tâche toutes les minutes :

   ```bash
   * * * * * echo "Bonjour $(date)" >> /tmp/date.cron
   ```

   b) **Une tâche périodique qui doit écrire, tous les quarts d'heure, de 8h à 17h du lundi au vendredi, dans le fichier `/tmp/processusX` (remplacez X par votre numéro de groupe), la liste des processus en cours d'exécution qui ont un terminal de contrôle.**

   Toujours dans l’éditeur crontab, ajoutez la ligne suivante :

   ```bash
   */15 8-17 * * 1-5 ps -eo pid,tty,etime,user | grep -v '?' >> /tmp/processusX
   ```

   - `*/15` : Exécuter tous les quarts d’heure.
   - `8-17` : Entre 8h et 17h.
   - `1-5` : Du lundi au vendredi.

   c) **Vérifiez que les tâches sont bien enregistrées (crontab –l).**

   Pour vérifier que les tâches sont bien programmées :

   ```bash
   crontab -l
   ```

   d) **Vérifiez son fonctionnement une fois programmé.**

   Attendez que le `cron` s'exécute et vérifiez les fichiers `/tmp/date.cron` et `/tmp/processusX` pour confirmer que les tâches s'exécutent correctement.

4. **Exécutions différées de commandes (at).**

   a) **Mettez en place une tâche qui affichera le message suivant dans 3 minutes : "rappel : vendredi midi, déjeuner avec la secrétaire" :-))**

   Utilisez la commande `at` pour programmer une tâche :

   ```bash
   echo 'echo "rappel : vendredi midi, déjeuner avec la secrétaire :-))"' | at now + 3 minutes
   ```

   b) **Que fait la commande `atq` ?**

   La commande `atq` affiche la liste des tâches programmées avec `at` :

   ```bash
   atq
   ```

   c) **Qu’est-ce que atd ?**

   Le service **`atd`** est le démon responsable de l'exécution des tâches différées programmées avec `at`.

   d) **Reprogrammez la même commande qu'au point 5a) mais empêchez son exécution avant qu'elle ne se produise (atrm).**

   Reprogrammez la commande :

   ```bash
   echo 'echo "rappel : vendredi midi, déjeuner avec la secrétaire :-))"' | at now + 3 minutes
   ```

   Ensuite, annulez-la avec `atrm` :

   ```bash
   atq  # Pour obtenir le numéro de la tâche
   atrm [numéro de tâche]
   ```

5. **Redémarrer le démon crond**

   a) **En utilisant la commande `systemctl`**

   Pour redémarrer le service `crond` :

   ```bash
systemctl restart crond
   ```

   b) **Le démon crond doit-il être redémarré après modification de son fichier de configuration ?**

   Non, `crond` n'a pas besoin d'être redémarré après modification du fichier de crontab. Le démon vérifie automatiquement les changements dans les fichiers crontab.

6. a) **Comment autoriser tout le monde à utiliser la commande crontab ?**

   Pour autoriser tous les utilisateurs à utiliser `crontab`, assurez-vous que les fichiers `/etc/cron.allow` et `/etc/cron.deny` sont correctement configurés :
   
   - Si le fichier `/etc/cron.allow` existe, il doit lister tous les utilisateurs autorisés.
   - Si le fichier `/etc/cron.deny` existe, il doit être vide ou ne pas inclure les utilisateurs que vous souhaitez autoriser.

   b) **Comment interdire uniquement à l'utilisateur userX d'utiliser la commande crontab ?**

   Ajoutez `userX` au fichier `/etc/cron.deny` :

   ```bash
   echo "userX" |  tee -a /etc/cron.deny
   ```

   c) **Si vous interdisez l’accès à la commande crontab à un utilisateur, cela a-t-il une influence sur les tâches périodiques déjà programmées par cet utilisateur ?**

   Non, les tâches déjà programmées continueront de s'exécuter, mais l'utilisateur ne pourra plus ajouter ou modifier des tâches via `crontab`.

7. **Mettez en place une tâche périodique qui met à jour la base de données de la commande locate (updatedb). Cette mise à jour doit être réalisée une fois par semaine, pendant votre pause.**

   Ouvrez le crontab avec `crontab -e` et ajoutez la ligne suivante pour exécuter la mise à jour une fois par semaine (par exemple le mercredi à midi) :

   ```bash
   0 12 * * 3 /usr/bin/updatedb
   ```

Cela exécute `updatedb` chaque mercredi à midi, ce qui correspond à une pause potentielle.

---

## Manip nine - Interface réseau
### PDF
![[09_LaboLinux_interface_reseau-ELEVES-.pdf]]
### Réponses
1. **Identifiez votre périphérique réseau (lspci ou lshw).**

   - Avec `lspci`, vous pouvez lister tous les périphériques, y compris la carte réseau :

 ```bash
 lspci | grep -i net
 ```

   - Avec `lshw`, vous pouvez obtenir des informations détaillées sur votre matériel réseau (nécessite les droits `root`) :

 ```bash
  lshw -C network
 ```

   Cela vous donnera des informations telles que le modèle de votre carte réseau et son état.

2. **Vérifiez que le pilote logiciel est bien chargé. (lsmod)**

   Utilisez la commande `lsmod` pour vérifier si le module de pilote de votre carte réseau est chargé :

   ```bash
   lsmod | grep <nom_du_pilote>
   ```

   Le nom du pilote est souvent mentionné dans la sortie de la commande précédente (`lshw` ou `lspci`), par exemple `e1000` ou `r8169`.

3. **Affichez l'état des interfaces réseaux (nmcli, ip, ifconfig). Déterminez quelle est l'adresse IP et l'adresse MAC de votre carte réseau.**

   Utilisez une des commandes suivantes pour afficher l'état des interfaces réseau et obtenir l'adresse IP et l'adresse MAC :

   - Avec `nmcli` :

 ```bash
 nmcli device show
 ```

   - Avec `ip` :

 ```bash
 ip addr show
 ```

   - Avec `ifconfig` (peut nécessiter d'être installé) :

 ```bash
 ifconfig
 ```

   La **MAC address** est généralement marquée comme `ether` et l'**adresse IP** sera répertoriée sous `inet`.

4. **Activez/désactivez une interface réseau (nmcli)**

   Pour désactiver une interface réseau (par exemple `eth0`) :
	
   ```bash
   nmcli device disconnect eth0
   ```

   Pour l'activer à nouveau :

   ```bash
   nmcli device connect eth0
   ```

5. **Configurez manuellement (pas de DHCP) votre ordinateur de manière à vous connecter à Internet voir votre configuration NAT (ifconfig, route, /etc/resolv.conf, /etc/host.conf)**

   - Configurez l'adresse IP statique avec `ifconfig` :

 ```bash
  ifconfig eth0 192.168.1.100 netmask 255.255.255.0 up
 ```

   - Définissez la passerelle par défaut :

 ```bash
  route add default gw 192.168.1.1
 ```

   - Configurez les serveurs DNS dans `/etc/resolv.conf` :

 ```bash
  nano /etc/resolv.conf
 ```

     Ajoutez le serveur DNS, par exemple :

 ```
 nameserver 8.8.8.8
 ```

   - Vérifiez la configuration NAT si vous utilisez une VM avec NAT.

6. **Redémarrez votre machine et vérifiez votre adresse IP, que se passe-t-il ?**

   Après redémarrage, si votre configuration réseau n'est pas persistante (non configurée dans un fichier réseau), l'adresse IP peut revenir à l'adresse attribuée par DHCP. Vérifiez l'adresse IP avec `ip addr show` ou `ifconfig`.

7. **Configurez votre interface réseau en fonction du réseau NAT dans lequel vous êtes ainsi que la passerelle et votre DNS (nmcli) et redémarrez la machine. Que se passe-t-il ?**

   Utilisez `nmcli` pour configurer l'interface réseau en fonction de votre NAT :

   ```bash
	   nmcli con mod eth0 ipv4.addresses 192.168.1.100/24
	   nmcli con mod eth0 ipv4.gateway 192.168.1.1
	   nmcli con mod eth0 ipv4.dns 8.8.8.8
	   nmcli con mod eth0 ipv4.method manual
	   nmcli con up eth0
   ```

   Après redémarrage, ces paramètres devraient persister. Si cela fonctionne, l'adresse IP et la connexion réseau devraient rester stables.

8. **Dans le répertoire `/etc/NetworkManager/system-connections`, recherchez le fichier qui configure votre carte réseau. Analysez son contenu.**

   Listez les fichiers de configuration de NetworkManager :

   ```bash
	ls /etc/NetworkManager/system-connections/
   ```

   Analysez le fichier de configuration correspondant à votre interface réseau (souvent un fichier `.nmconnection`) :

   ```bash
	cat /etc/NetworkManager/system-connections/<nom-du-fichier>
   ```

   Ce fichier contient les paramètres IP, DNS, et d'autres configurations de l'interface.

9. **Test de la communication (ping)**

   a) **Testez la communication vers google et vers le serveur DNS de l’institut :**

   ```bash
   ping google.com
   ping <adresse_IP_DNS_institut>
   ```

   b) **Testez la connectivité de la passerelle en spécifiant des paquets de taille 1500 octets et en envoyant que 5 paquets :**

   ```bash
   ping -s 1500 -c 5 192.168.1.1
   ```

   Cela envoie 5 paquets de 1500 octets à la passerelle (adresse IP à remplacer par celle de votre passerelle).

10. **Affichez l'état de la table de routage locale (route ou netstat). Quelle est la signification des indicateurs d'état suivants : U, H, G.**

   Utilisez `route` pour afficher la table de routage :

	   ```bash
	   route -n
	   ```

   Ou avec `netstat` :

	   ```bash
	   netstat -r
	   ```

   Signification des indicateurs :
   - **U** : L'interface est "up" (active).
   - **H** : L'entrée est une adresse de l'hôte (plutôt qu'un réseau).
   - **G** : L'entrée correspond à une passerelle.

11. **Vérifiez que la résolution des noms fonctionne (ping, nslookup, dig)**

   Utilisez `ping` pour tester la résolution de noms :
	
	   ```bash
	   ping google.com
	   ```

   Utilisez `nslookup` pour interroger un serveur DNS :
	
	   ```bash
	   nslookup google.com
	   ```

   Utilisez `dig` pour obtenir plus de détails sur la résolution DNS :

	   ```bash
	   dig google.com
	   ```

12. **Résolution des noms d'hôtes (host)**

   Utilisez la commande `host` pour obtenir des informations sur les noms d’hôtes :

	   ```bash
	   host google.com
	   ```

13. **Visualisez la table des adresses MAC connues de votre ordinateur (arp). "Pinguez" une adresse IP locale et affichez de nouveau la table des adresses MAC.**

   Pour afficher la table ARP :

	   ```bash
	   arp -a
	   ```

   Ensuite, faites un `ping` vers une adresse IP locale :
	
	   ```bash
	   ping 192.168.1.1
	   ```

   Puis vérifiez à nouveau la table ARP :
	
	   ```bash
	   arp -a
	   ```

14. **Affichez les informations sur la route suivie pour atteindre un hôte (traceroute)**

   Utilisez la commande `traceroute` pour voir le chemin suivi par les paquets vers un hôte :

	   ```bash
	   traceroute google.com
	   ```

   Cela affichera chaque saut (routeur) traversé pour atteindre l'hôte final.

---

## Manip ten - Surveiller les ressources
### PDF
![[10_LaboLinux_Gestion_ressources-ELEVES-.pdf]]
### Réponses
1. **Affichez la mémoire utilisée actuellement par le système (free)**

   Utilisez la commande `free` pour afficher l'état de la mémoire :

	   ```bash
	   free -h
	   ```

   Cela affichera l'utilisation de la mémoire de manière plus lisible avec des unités adaptées (Ko, Mo, Go).

   1.1. **Quelle est la quantité de mémoire physique utilisée/libre sur le système ?**

      La sortie de la commande `free` donne les informations suivantes :
      
      - **Mem** : Ligne qui représente la mémoire physique.
        - `used` : Quantité de mémoire physique utilisée.
        - `free` : Quantité de mémoire physique libre.

   1.2. **Quelle est la quantité de swap utilisée/libre sur le système ?**

      - **Swap** : Ligne qui représente l'espace d'échange (swap).
        - `used` : Quantité de swap utilisée.
        - `free` : Quantité de swap libre.

   1.3. **Utilisez la commande watch afin d'obtenir l'affichage de l'utilisation de la mémoire toutes les cinq secondes.**

      Utilisez la commande `watch` pour surveiller la mémoire toutes les 5 secondes :

      ```bash
      watch -n 5 free -h
      ```

   Cela mettra à jour l'affichage de l'utilisation de la mémoire toutes les 5 secondes.

2. **Avec la commande top :**

   2.1. **Listez les processus démarrés par l'utilisateur groupeX (top, u)**

      Exécutez `top` et utilisez l'option `u` pour filtrer les processus de l'utilisateur `groupeX` :

      - Lancez `top` :
      
        ```bash
        top
        ```
      
      - Appuyez sur `u` puis entrez `groupeX` pour voir les processus de cet utilisateur.

   2.2. **Classez-les par ordre décroissant d'utilisation de mémoire (top, F, n)**

      Dans `top`, pour trier par utilisation de la mémoire :
      
      - Appuyez sur `F` pour ouvrir le menu de tri.
      - Appuyez sur `n` pour trier par la colonne mémoire (`%MEM`).
      - Appuyez sur `Enter` pour appliquer le tri.

   2.3. **Afficher seulement les processus actifs de l’utilisateur groupeX (top, i)**

      Dans `top`, pour masquer les processus inactifs (zombies ou en veille), appuyez sur `i` pour ne montrer que les processus actifs.

      Si vous voulez filtrer en plus par utilisateur, utilisez la combinaison des commandes précédentes (`u` et `i`).

3. **A l'aide de la commande vmstat :**

   3.1. **Déterminez quel est le pourcentage de temps pendant lequel le CPU exécute un code de niveau utilisateur et un code de niveau système**

      La commande `vmstat` affiche l’utilisation CPU, y compris le temps utilisateur et système :

      ```bash
      vmstat 1
      ```

      Les colonnes `us` et `sy` indiquent respectivement le pourcentage de temps CPU utilisé en mode utilisateur et en mode système.

   3.2. **Utilisez vmstat pour afficher 15 fois de suite ces informations (points 3.1) sur l'utilisation des ressources avec un délai de 5 secondes entre chaque affichage.**

      Utilisez cette commande pour un affichage avec une fréquence de 5 secondes sur 15 cycles :

      ```bash
      vmstat 5 15
      ```

   3.3. **Que pensez-vous de la première ligne de résultats proposée par vmstat ?**

      La première ligne de `vmstat` affiche des moyennes cumulatives depuis le démarrage du système, elle n'est donc pas directement représentative de l’état actuel. Les lignes suivantes montrent l'état instantané à chaque intervalle spécifié.

4. **Affichez les informations fournies par la commande uptime**

   La commande `uptime` montre la durée pendant laquelle le système est actif, le nombre d'utilisateurs connectés, et la charge moyenne du système :

	   ```bash
	   uptime
	   ```

1. **Afficher les informations concernant la fréquence du processeur ainsi que la taille du cache (cat /proc/cpuinfo)**

   Utilisez la commande suivante pour afficher des informations détaillées sur le CPU, y compris la fréquence et la taille du cache :
	
	   ```bash
	   cat /proc/cpuinfo
	   ```

   Recherchez les lignes contenant `cpu MHz` pour la fréquence et `cache size` pour la taille du cache.

6. **Affichez les informations concernant les utilisateurs actuellement connectés (w)**

   La commande `w` affiche les utilisateurs connectés, les processus en cours, et les temps d’inactivité :

	   ```bash
	   w
	   ```

   6.1. **La commande w affiche-t-elle des informations concernant les utilisateurs connectés en mode graphique ?**

      Oui, la commande `w` affiche les informations des utilisateurs connectés à la fois en mode graphique (via un terminal) et en ligne de commande.

   6.2. **Si un hôte est connecté à distance, la commande w permet-t-elle de connaître l'origine d'un hôte distant ?**

      Oui, la commande `w` affiche l'adresse IP ou le nom d'hôte de la machine distante dans la colonne `FROM` si un utilisateur est connecté via SSH ou un autre protocole de connexion distante.

7. **Utilisez la commande time afin d'évaluer les ressources et le temps employés par la commande updatedb.**

   Utilisez `time` pour mesurer le temps d'exécution de la commande `updatedb` :

	   ```bash
	    time updatedb
	   ```

   La sortie vous donnera trois valeurs :
   - **real** : Temps réel écoulé.
   - **user** : Temps CPU utilisé en mode utilisateur.
   - **sys** : Temps CPU utilisé en mode système.

---

## Manip eleven - Gestion des quotas
### PDF
![[11_LaboLinux_lesQuotas-ELEVES-.pdf]]
### Réponses
1. **Vérifiez que le paquetage quota est bien installé (sinon, installez-le), quelle version avez-vous ?**

   Vérifiez si le paquet `quota` est installé avec la commande suivante :

	   ```bash
	   rpm -q quota
	   ```

   Si le paquet n'est pas installé, installez-le :

	   ```bash
	    yum install quota
	   ```

   Une fois installé, la commande `rpm -q quota` vous affichera la version du paquet.

2. **Vérifiez que vous disposez d'une partition dédiée à /home**

   Utilisez la commande `df` pour vérifier les partitions et leurs points de montage :

	   ```bash
	   df -h
	   ```

   Vérifiez dans la sortie qu'une partition est bien montée sur `/home`.

3. **Activez et vérifiez l'activation des quotas (utilisateurs et groupes) sur la partition /home**

   - Modifiez le fichier `/etc/fstab` pour activer les quotas sur la partition `/home`. Ajoutez les options `usrquota` et `grpquota` à la ligne correspondant à `/home` :

     ```bash
     /dev/sdaX  /home  ext4  defaults,usrquota,grpquota  0  2
     ```

   - Remontez la partition `/home` avec la commande suivante :

     ```bash
      mount -o remount /home
     ```

   - Initialisez les fichiers de quotas :

     ```bash
      quotacheck -cum /home
      quotaon /home
     ```

   - Vérifiez que les quotas sont activés :

     ```bash
      quotaon -p /home
     ```

4. **Créez un utilisateur quelconque, puis configurez-lui des quotas**

   - Créez un utilisateur :

     ```bash
      useradd testuser
      passwd testuser
     ```

   a) **Fixez ses limites d'espace disque à 100 Ko (limite douce) et 300 Ko (limite dure)**

   Utilisez la commande `edquota` pour configurer les quotas pour `testuser` :

	   ```bash
	    edquota -u testuser
	   ```

   Dans l'éditeur, définissez les valeurs comme suit :

	   ```
	   Disk quotas for user testuser (uid 1001):
	     Filesystem  blocks  soft  hard  inodes  soft  hard
	     /dev/sdaX       0    100   300       0     0     0
	   ```

   - **blocks** : taille en Ko, ajustez selon les besoins.

   b) **Vérifiez que ces quotas ont bien été pris en compte en générant un rapport avec la commande repquota**

   Utilisez la commande suivante pour afficher un rapport des quotas :

	   ```bash
	    repquota /home
	   ```

   c) **Vérifiez que ces quotas fonctionnent en copiant des fichiers dans le répertoire de l'utilisateur**

   Copiez des fichiers dans le répertoire de l'utilisateur jusqu'à atteindre la limite douce (100 Ko). Lorsque cette limite est atteinte, l'utilisateur reçoit un avertissement, mais peut encore écrire des fichiers.

   d) **Que se passe-t-il lorsque l'utilisateur dépasse la limite dure ?**

   Une fois la limite dure (300 Ko) atteinte, l'utilisateur ne pourra plus écrire de fichiers.

   e) **Si un utilisateur atteint sa limite dure, root peut-il encore ajouter des fichiers dans le répertoire personnel de l’utilisateur ?**

   Oui, l'utilisateur `root` n'est pas limité par les quotas et peut toujours écrire dans le répertoire de l'utilisateur.

   f) **Après avoir atteint la limite de son quota, l'utilisateur efface des fichiers dans son répertoire personnel. Peut-il créer de nouveaux fichiers ?**

   Oui, si l'utilisateur efface des fichiers et que l'espace disque occupé passe en dessous de la limite, il pourra de nouveau créer des fichiers jusqu'à atteindre la limite.

   g) **Modifiez la période de grâce**

   Modifiez la période de grâce en utilisant la commande `edquota -t` :

	   ```bash
	    edquota -t
	   ```

   Cela vous permet de configurer la période de grâce pour les limites douces.

5. **Comment root peut-il désactiver la surveillance des quotas ?**

   Pour désactiver les quotas sur la partition `/home`, utilisez la commande suivante :

	   ```bash
	    quotaoff /home
	   ```

6. **Créez un nouvel utilisateur et fixez-lui les mêmes quotas que pour l'utilisateur créé au point 4**

   - Créez un nouvel utilisateur :

     ```bash
      useradd newuser
      passwd newuser
     ```

   - Configurez les mêmes quotas que pour `testuser` en utilisant la commande `edquota` :

     ```bash
      edquota -u newuser
     ```

   Modifiez les quotas de la même manière que pour `testuser` (100 Ko de limite douce et 300 Ko de limite dure).

Cela vous permet de gérer les quotas utilisateur et groupe sur votre partition `/home`.

---

## Manip twelve - Arrêt / Démarrage du système
### PDF
![[12_LaboLinux_arretETdemarrage-ELEVES-.pdf]]
### Réponses
1. **Affichez le compte rendu du démarrage (dmesg). Enregistrez ce compte rendu dans un fichier. Lisez le fichier /var/log/messages afin de vérifier qu'aucun message d'erreur n'est relatif au démarrage du système.**

   - Affichez le compte rendu du démarrage avec `dmesg` et enregistrez-le dans un fichier :

     ```bash
     dmesg > /home/groupeX/dmesg.log
     ```

   - Ensuite, vérifiez le fichier `/var/log/messages` pour détecter d'éventuelles erreurs :

     ```bash
     cat /var/log/messages | grep -i error
     ```

   Recherchez des lignes liées au démarrage du système.

2. **Affichez le mode de fonctionnement courant ainsi que l'heure à laquelle il a été initié (who –r).**

   Utilisez la commande suivante pour afficher le runlevel et l'heure d'initialisation du mode de fonctionnement :

	   ```bash
	   who -r
	   ```

   Cette commande vous montrera le niveau de fonctionnement actuel et l'heure à laquelle il a été activé.

3. **Identifiez les units actifs (systemctl). Rechercher l'utilité de quelques services, arrêtez ceux qui sont inutiles et faites-en sorte qu'ils ne soient pas exécutés lors des prochains démarrages du système.**

   - Listez les unités (services) actifs avec la commande suivante :

     ```bash
     systemctl list-units --type=service
     ```

   - Utilisez `systemd-analyze blame` pour afficher le temps de démarrage des services, ce qui peut vous aider à identifier les services à optimiser :

     ```bash
     systemd-analyze blame
     ```

   - Si vous identifiez des services inutiles, vous pouvez les arrêter avec la commande suivante (remplacez `nom_service` par le nom du service à désactiver) :

     ```bash
      systemctl stop nom_service
     ```

   - Désactivez le service pour qu'il ne démarre pas automatiquement au prochain redémarrage :

     ```bash
      systemctl disable nom_service
     ```

4. **Modifiez le niveau de fonctionnement par défaut afin de démarrer sans interface graphique.**

   - Vérifiez le niveau de fonctionnement par défaut avec la commande suivante :

     ```bash
     systemctl get-default
     ```

   - Modifiez le niveau de fonctionnement pour démarrer en mode multi-utilisateur sans interface graphique (runlevel 3) :

     ```bash
      systemctl set-default multi-user.target
     ```

5. **Indiquez la marche à suivre pour vous connecter en tant que root sans connaître le mot de passe administrateur.**

   - Redémarrez la machine et accédez au menu GRUB.
   - Sélectionnez votre entrée de démarrage, puis appuyez sur `e` pour modifier les options de démarrage.
   - Trouvez la ligne qui commence par `linux` ou `linux16` et ajoutez `init=/bin/bash` à la fin de cette ligne.
   - Appuyez sur `Ctrl+X` ou `F10` pour démarrer avec ces options modifiées.
   - Vous obtiendrez un shell root sans mot de passe. Vous pourrez alors changer le mot de passe root avec la commande suivante :

     ```bash
     passwd
     ```

6. **Comment démarrer le système sous différents niveaux de fonctionnement ?**

   - Les niveaux de fonctionnement (ou targets) peuvent être modifiés temporairement avec `systemctl`. Par exemple, pour passer en mode mono-utilisateur (runlevel 1) :

     ```bash
      systemctl isolate rescue.target
     ```

   - Pour revenir à un mode multi-utilisateur avec interface graphique :

     ```bash
      systemctl isolate graphical.target
     ```

   Vous pouvez démarrer dans un autre niveau de fonctionnement en modifiant les options de démarrage dans GRUB comme vu dans la question précédente.

7. **Créez un script qui écrit le résultat de la commande ps dans le fichier /home/groupeX/ps.log. Ce script doit s'exécuter en tant que service au démarrage.**

   - Créez un script dans `/home/groupeX/ps-script.sh` :

     ```bash
     #!/bin/bash
     ps aux > /home/groupeX/ps.log
     ```

   - Rendre le script exécutable :

     ```bash
     chmod +x /home/groupeX/ps-script.sh
     ```

   - Créez un fichier service pour ce script dans `/etc/systemd/system/pslog.service` :

     ```bash
     [Unit]
     Description=Enregistrement des processus dans ps.log

     [Service]
     ExecStart=/home/groupeX/ps-script.sh

     [Install]
     WantedBy=multi-user.target
     ```

   - Activez et démarrez le service :

     ```bash
      systemctl enable pslog.service
      systemctl start pslog.service
     ```

   - Pour tester, redémarrez la machine avec la commande suivante :

     ```bash
      shutdown -r +1 "Redémarrage dans 1 minute"
     ```

8. **Écrivez un script qui enregistre la date à la fin du fichier /home/groupeX/arret. Ce script doit être activé automatiquement à chaque démarrage du système.**

   - Créez un script `/home/groupeX/arret-script.sh` :

     ```bash
     #!/bin/bash
     echo "$(date)" >> /home/groupeX/arret
     ```

   - Rendre le script exécutable :

     ```bash
     chmod +x /home/groupeX/arret-script.sh
     ```

   - Créez un service `/etc/systemd/system/arret.service` :

     ```bash
     [Unit]
     Description=Enregistre la date à chaque démarrage

     [Service]
     ExecStart=/home/groupeX/arret-script.sh

     [Install]
     WantedBy=multi-user.target
     ```

   - Activez et démarrez le service :

     ```bash
      systemctl enable arret.service
      systemctl start arret.service
     ```

   - Redémarrez pour tester et vérifiez que la date a bien été ajoutée au fichier `/home/groupeX/arret`.

9. **Installez le serveur Web httpd à l’aide de la commande dnf. Faites que le service soit démarré automatiquement en mode multi-user.**

   - Installez le serveur Web `httpd` :

     ```bash
      dnf install httpd
     ```

   - Activez et démarrez le service :

     ```bash
      systemctl enable httpd.service
      systemctl start httpd.service
     ```

   Le service `httpd` sera maintenant démarré automatiquement en mode multi-utilisateur (`multi-user.target`).
   
---

## Manip thirteen - NFS, Network File System 
### PDF
![[13_LaboLinux_NFS-ELEVES-.pdf]]
### Réponses
1. **Répondez aux questions suivantes :**

   1.1. **Déterminez l'état du service NFS (systemctl)**

   Utilisez la commande suivante pour déterminer l'état du service NFS :

	   ```bash
	   systemctl status nfs-server
	   ```

   Cela affichera si le service est actif, en cours d'exécution ou arrêté.

   1.2. **Quelle commande permet de démarrer le service NFS ?**

   Pour démarrer le service NFS, utilisez la commande suivante :

	   ```bash
	    systemctl start nfs-server
	   ```

   1.3. **Quelle commande permet d'arrêter le service NFS ?**

   Pour arrêter le service NFS, utilisez la commande suivante :

	   ```bash
	    systemctl stop nfs-server
	   ```

   1.4. **Comment vérifier que les services RPC nécessaires à NFS sont démarrés (rpcinfo) ?**

   Utilisez la commande `rpcinfo` pour vérifier que les services RPC nécessaires à NFS sont démarrés :

	   ```bash
	   rpcinfo -p
	   ```

   Cela listera les services RPC en cours d'exécution, y compris ceux liés à NFS, comme `portmapper`, `nfs`, `mountd`, et `nlockmgr`.

2. **Mettez en place un serveur NFS de manière à répondre aux exigences suivantes :**

   2.1. **Les services NFS doivent être lancés au démarrage de l'ordinateur dans le niveau de fonctionnement multi-user graphique uniquement (systemctl)**

   Pour activer NFS afin qu'il démarre automatiquement au démarrage du système (uniquement en mode multi-utilisateur avec interface graphique), utilisez :

	   ```bash
	    systemctl enable nfs-server
	   ```

   Cela assure que le service NFS est activé en mode multi-user et graphique (runlevel 5).

   2.2. **Le serveur doit exporter un système de fichiers en lecture seule depuis `/nfs/infos` vers tous les systèmes de votre réseau local, en réprimant les tentatives d'accès en root.**

   - Modifiez le fichier `/etc/exports` pour configurer le partage NFS :

     ```bash
     /nfs/infos 192.168.1.0/24(ro,sync,no_root_squash)
     ```

   - Cela indique que le répertoire `/nfs/infos` sera exporté en lecture seule (`ro`) pour tous les systèmes du réseau local `192.168.1.0/24`. L'option `no_root_squash` réprime les tentatives d'accès en tant que root.

   2.2.1. **Quelle commande devez-vous utiliser pour exporter (rendre disponible) votre partage ?**

   Après avoir configuré `/etc/exports`, utilisez la commande suivante pour exporter les répertoires NFS :

	   ```bash
	    exportfs -a
	   ```

   2.2.2. **Quelle commande devez-vous utiliser pour accéder à ce partage depuis une machine cliente ?**

   Depuis une machine cliente, montez le partage avec la commande suivante :

	   ```bash
	    mount 192.168.1.x:/nfs/infos /mnt/nfs_infos
	   ```

   Remplacez `192.168.1.x` par l'adresse IP du serveur NFS et `/mnt/nfs_infos` par un point de montage sur la machine cliente.

   2.2.3. **Que permet la commande showmount ?**

   La commande `showmount` permet d'afficher les répertoires NFS exportés par un serveur NFS donné. Exemple d'utilisation :

	   ```bash
	   showmount -e 192.168.1.x
	   ```

   Cela affiche les systèmes de fichiers exportés par le serveur NFS.

3. **Faites-en sorte que le système de fichiers partagé au point précédent soit monté automatiquement, au démarrage, sur la machine cliente (/etc/fstab)**

   Sur la machine cliente, ajoutez une ligne dans `/etc/fstab` pour monter automatiquement le partage NFS au démarrage :

	   ```bash
	   192.168.1.x:/nfs/infos /mnt/nfs_infos nfs defaults 0 0
	   ```

   Remplacez `192.168.1.x` par l'adresse IP du serveur et `/mnt/nfs_infos` par le point de montage.

4. **Exporter un système de fichiers accessible en lecture-écriture depuis /nfs/public vers tous les systèmes de votre réseau local, en autorisant les tentatives d'accès en root.**

   - Modifiez le fichier `/etc/exports` pour configurer l'exportation en lecture-écriture avec accès root :

     ```bash
     /nfs/public 192.168.1.0/24(rw,sync,no_root_squash)
     ```

   - Après modification, utilisez la commande `exportfs` pour appliquer les modifications :

     ```bash
      exportfs -r
     ```

5. **Exporter le répertoire /nfs/perso vers les hôtes "pierre" et "paul" du réseau local en le rendant accessible en écriture. Exporter ce même répertoire /nfs/perso vers l'hôte "jean" du réseau local, mais en lecture seule cette fois.**

   - Ajoutez les lignes suivantes dans `/etc/exports` :

     ```bash
     /nfs/perso pierre(rw,sync,no_root_squash)
     /nfs/perso paul(rw,sync,no_root_squash)
     /nfs/perso jean(ro,sync,no_root_squash)
     ```

   - Exportez les nouveaux partages :

     ```bash
      exportfs -a
     ```

   5.1. **L'utilisateur pierre d’un ordinateur du réseau aura-t-il un accès en écriture au répertoire /nfs/perso ?**

   Oui, puisque l'accès en écriture est spécifiquement accordé à `pierre` avec l'option `rw`.

6. **Le fichier /etc/exports comprend les deux lignes suivantes, y a-t-il une différence entre ces deux lignes ?**

   - `/mnt/export user(rw)`
   - `/mnt/export user (rw)`

   La différence est subtile mais importante. Dans la seconde ligne, il y a un espace entre `user` et `(rw)`, ce qui pourrait entraîner une erreur de syntaxe dans le fichier `/etc/exports`. Il ne devrait pas y avoir d'espace entre le nom d'hôte et les options d'exportation.

7. **Mettez en place le partage /nfs/mapping tel que n'importe quel hôte du réseau doit y avoir accès en lecture seule. Assurez-vous qu'aucun hôte distant ne sera capable de modifier les fichiers du répertoire partagé.**

   - Ajoutez la ligne suivante à `/etc/exports` :

     ```bash
     /nfs/mapping 192.168.1.0/24(ro,sync,no_root_squash)
     ```

   - Exportez le partage :

     ```bash
      exportfs -a
     ```

   Cela rend le répertoire accessible en lecture seule pour tous les hôtes du réseau local.

8. **A l’aide de automount, monter automatiquement le partage /nfs/mapping dans le dossier /tmp/nfs à créer. Le dossier doit se démonter automatiquement pour libérer les ressources après 60 s d’inactivité.**

   - Installez `autofs` si nécessaire :

     ```bash
      dnf install autofs
     ```

   - Modifiez le fichier `/etc/auto.master` pour ajouter la configuration de montage automatique :

     ```bash
     /tmp/nfs /etc/auto.nfs --timeout=60
     ```

   - Créez le fichier `/etc/auto.nfs` avec le contenu suivant :

     ```bash
     mapping -fstype=nfs,rw 192.168.1.x:/nfs/mapping
     ```

   - Redémarrez `autofs` :

     ```bash
      systemctl restart autofs
     ```

   Le partage `/nfs/mapping` sera monté automatiquement dans `/tmp/nfs` et se démontera après 60 secondes d'inactivité.

---

## Manip fourteen - IPtables
### PDF
![[14_LaboLinux_iptables-ELEVES-.pdf]]
### Réponses
1. **Désactivez firewalld et installez iptables-services**

   - Désactivez `firewalld` avec la commande suivante :

     ```bash
      systemctl stop firewalld
      systemctl disable firewalld
     ```

   - Installez le service `iptables-services` :

     ```bash
      dnf install iptables-services
     ```

   - Démarrez et activez `iptables-services` :

     ```bash
      systemctl start iptables
      systemctl enable iptables
     ```

2. **Affichez les règles du firewall, ensuite supprimez les règles préexistantes.**

   2.1. **Affichez toutes les règles des tables de votre FW :**

   Utilisez la commande suivante pour afficher toutes les règles :

   ```bash
    iptables -L -v -n
   ```

   2.2. **Affichez toutes les règles de la chaîne OUTPUT de la table filter :**

   Pour afficher les règles de la chaîne `OUTPUT` :

   ```bash
    iptables -L OUTPUT -v -n
   ```

   2.3. **Effacez toutes les règles de la chaîne INPUT :**

   Supprimez toutes les règles de la chaîne `INPUT` :

   ```bash
    iptables -F INPUT
   ```

3. **Listez les ports ouverts d'une machine (nmap)**

   Utilisez `nmap` pour scanner les ports ouverts d'une machine spécifique. Par exemple, pour scanner votre propre machine :

   ```bash
    nmap -p- 127.0.0.1
   ```

   Cette commande scannera tous les ports sur la machine locale.

4. **Sauvegarder et charger une configuration (iptables-save et iptables-restore)**

   - Pour sauvegarder la configuration actuelle des règles `iptables` :

     ```bash
      iptables-save > /etc/iptables/rules.v4
     ```

   - Pour restaurer la configuration à partir d'une sauvegarde :

     ```bash
      iptables-restore < /etc/iptables/rules.v4
     ```

5. **Créez les règles suivantes :**

   - **Ajoutez la règle OUTPUT -j DROP (Appelez ensuite le professeur) :**

     ```bash
      iptables -A OUTPUT -j DROP
     ```

   - **Autorisez le sous-réseau 10.1.0.0/16 à envoyer des informations à votre machine :**

     ```bash
      iptables -A INPUT -s 10.1.0.0/16 -j ACCEPT
     ```

   - **Autorisez tout sauf l'hôte 10.1.10.1 à envoyer des informations à votre machine :**

     ```bash
      iptables -A INPUT -s 10.1.10.1 -j DROP
      iptables -A INPUT -s 10.1.0.0/16 -j ACCEPT
     ```

   - **Refuser les pings en entrée :**

     ```bash
      iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
     ```

   - **Acceptez les données envoyées par un site web (HTTP) et un FTP :**

     ```bash
      iptables -A INPUT -p tcp --dport 80 -j ACCEPT
      iptables -A INPUT -p tcp --dport 21 -j ACCEPT
     ```

   - **Interdisez l'adresse MAC d'un ordinateur de la classe en entrée :**

     Remplacez `00:11:22:33:44:55` par l'adresse MAC de l'ordinateur à interdire :

     ```bash
      iptables -A INPUT -m mac --mac-source 00:11:22:33:44:55 -j DROP
     ```

6. **Créez une nouvelle chaîne ayant une règle qui accepte toutes les connexions de la localloop. Testez la règle, ensuite supprimez la chaîne créée.**

   - Créez une nouvelle chaîne `LOOPBACK` :

     ```bash
      iptables -N LOOPBACK
      iptables -A LOOPBACK -i lo -j ACCEPT
     ```

   - Appliquez la chaîne à la règle :

     ```bash
      iptables -A INPUT -j LOOPBACK
     ```

   - Testez la règle en pingant `127.0.0.1` :

     ```bash
     ping 127.0.0.1
     ```

   - Supprimez la chaîne :

     ```bash
      iptables -D INPUT -j LOOPBACK
      iptables -F LOOPBACK
      iptables -X LOOPBACK
     ```

7. **Écrivez un script pour votre FW tel que :**

   - Créez un script `/etc/firewall.sh` pour les règles `iptables` :

     ```bash
     #!/bin/bash

     # Flush les règles existantes
     iptables -F
     iptables -X

     # Interdire toutes les connexions par défaut
     iptables -P INPUT DROP
     iptables -P FORWARD DROP
     iptables -P OUTPUT ACCEPT

     # Accepter les connexions de la boucle locale
     iptables -A INPUT -i lo -j ACCEPT

     # Accepter les pings provenant du réseau local
     iptables -A INPUT -p icmp --icmp-type echo-request -s 192.168.1.0/24 -j ACCEPT
     ```

   - Rendez le script exécutable :

     ```bash
      chmod +x /etc/firewall.sh
     ```

   - Créez un fichier service `/etc/systemd/system/firewall.service` pour démarrer le firewall dans les cibles graphique et non graphique multi-users :

     ```bash
     [Unit]
     Description=Firewall script

     [Service]
     ExecStart=/etc/firewall.sh

     [Install]
     WantedBy=multi-user.target graphical.target
     ```

   - Activez et démarrez le service :

     ```bash
      systemctl enable firewall.service
      systemctl start firewall.service
     ```

---

## Manip fifteen - LVM Script
### PDF
![[15_LaboLinux_LVM-Script-ELEVES-.pdf]]
### Réponses
1. **Ajoutez un nouveau disque à votre machine virtuelle de 2 Go. Partitionnez-le, créez un PV sur ce disque et ajoutez-le au VG. Augmentez la taille du LV qui contient `/home` de 1 Go.**

   - **Ajoutez et détectez le nouveau disque** :
     Une fois le disque ajouté à la machine virtuelle, détectez-le avec la commande suivante :

     ```bash
      fdisk -l
     ```

     Vous verrez apparaître un nouveau périphérique, par exemple `/dev/sdb`.

   - **Partitionnez le nouveau disque** :

     Utilisez `fdisk` pour partitionner le disque :

     ```bash
      fdisk /dev/sdb
     ```

     Créez une nouvelle partition primaire, enregistrez et quittez.

   - **Créez un Physical Volume (PV)** :

     Initialisez le nouveau disque en tant que PV :

     ```bash
      pvcreate /dev/sdb1
     ```

   - **Ajoutez le PV au Volume Group (VG)** :

     Ajoutez le PV au VG existant (par exemple `vg_home`) :

     ```bash
      vgextend vg_home /dev/sdb1
     ```

   - **Augmentez la taille du Logical Volume (LV) contenant `/home` de 1 Go** :

     Augmentez le LV contenant `/home` :

     ```bash
      lvextend -L +1G /dev/vg_home/lv_home
     ```

     Ensuite, redimensionnez le système de fichiers :

     ```bash
      resize2fs /dev/vg_home/lv_home
     ```

2. **Diminuez la taille du LV de `/home` pour le remettre à 1 Go.**

   - **Démontez `/home`** :

     Avant de réduire la taille du LV, démontez la partition :

     ```bash
      umount /home
     ```

   - **Vérifiez le système de fichiers** :

     Utilisez `fsck` pour vérifier le système de fichiers avant de le redimensionner :

     ```bash
      e2fsck -f /dev/vg_home/lv_home
     ```

   - **Redimensionnez le système de fichiers à 1 Go** :

     Réduisez la taille du système de fichiers à 1 Go :

     ```bash
      resize2fs /dev/vg_home/lv_home 1G
     ```

   - **Réduisez la taille du LV à 1 Go** :

     Ensuite, réduisez la taille du LV :

     ```bash
      lvreduce -L 1G /dev/vg_home/lv_home
     ```

   - **Remontez `/home`** :

     Enfin, remontez `/home` :

     ```bash
      mount /home
     ```

3. **Réalisez une commande « toto » qui ouvrira en édition le fichier de configuration de l’interface réseau.**

   - Créez un alias ou un script pour la commande `toto` :
     - **Option 1 : Alias** (ajoutez cette ligne dans `~/.bashrc`) :

       ```bash
       alias toto=' nano /etc/sysconfig/network-scripts/ifcfg-eth0'
       ```

       Rechargez le shell avec :

       ```bash
       source ~/.bashrc
       ```

     - **Option 2 : Script** :

       Créez un script `/usr/local/bin/toto` :

       ```bash
        nano /usr/local/bin/toto
       ```

       Contenu du script :

       ```bash
       #!/bin/bash
        nano /etc/sysconfig/network-scripts/ifcfg-eth0
       ```

       Rendez-le exécutable :

       ```bash
        chmod +x /usr/local/bin/toto
       ```

4. **Réalisez un script qui vérifie les fichiers modifiés dans `/etc` lors des dernières 24h et écrit la liste de ces fichiers dans un fichier. Ce script devra être lancé automatiquement tous les soirs à 20h.**

   - **Création du script** :
     Créez un script `/usr/local/bin/check_etc.sh` :

     ```bash
      nano /usr/local/bin/check_etc.sh
     ```

     Contenu du script :

     ```bash
     #!/bin/bash
     find /etc -type f -mtime -1 > /home/groupeX/modified_files.txt
     ```

     Rendez le script exécutable :

     ```bash
      chmod +x /usr/local/bin/check_etc.sh
     ```

   - **Planification avec cron** :
     Ajoutez la tâche cron pour l'exécuter chaque soir à 20h :

     ```bash
      crontab -e
     ```

     Ajoutez la ligne suivante :

     ```bash
     0 20 * * * /usr/local/bin/check_etc.sh
     ```

5. **Réalisez un script qui prend comme paramètre le nom de l’utilisateur et son mot de passe. Il créera cet utilisateur, le rajoutera automatiquement au groupe `userX` et l’obligera à modifier son mot de passe à sa première connexion.**

   - **Création du script** :
     Créez un script `/usr/local/bin/create_user.sh` :

     ```bash
      nano /usr/local/bin/create_user.sh
     ```

     Contenu du script :

     ```bash
     #!/bin/bash
     if [ $# -ne 2 ]; then
         echo "Usage: $0 <username> <password>"
         exit 1
     fi

     username=$1
     password=$2

     # Créer l'utilisateur
      useradd -m $username
     echo "$username:$password" |  chpasswd

     # Ajouter au groupe userX
      usermod -aG userX $username

     # Forcer le changement de mot de passe à la première connexion
      chage -d 0 $username
     ```

     Rendez-le exécutable :

     ```bash
      chmod +x /usr/local/bin/create_user.sh
     ```

   - **Exécution du script** :

     ```bash
      /usr/local/bin/create_user.sh <nom_utilisateur> <mot_de_passe>
     ```


6. **Écrire un script bash permettant d'afficher tous les comptes locaux d'un système Linux hormis root.**

   - **Création du script** :
     Créez un script `/usr/local/bin/list_users.sh` :

     ```bash
      nano /usr/local/bin/list_users.sh
     ```

     Contenu du script :

     ```bash
     #!/bin/bash
     getent passwd | awk -F: '$3 >= 1000 && $1 != "root" {print $1}'
     ```

     Cela filtrera les comptes locaux avec un UID >= 1000 (excepté root) qui correspondent aux utilisateurs standards sur la plupart des systèmes Linux.

   - **Rendre le script exécutable** :

     ```bash
      chmod +x /usr/local/bin/list_users.sh
     ```

   - **Exécution du script** :

     ```bash
     /usr/local/bin/list_users.sh
     ```

---
