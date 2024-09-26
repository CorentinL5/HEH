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

## Manip two 
### PDF
![[02_Labo_Linux_Les_commandes_de_bases_suite-ELEVES-.pdf]]   
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
     find / -name fstab 2>/dev/null
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

### Réponses aux questions suivantes :

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

## Manip three
### PDF
![[03_Labo_Linux_Permissions_acces-ELEVES-.pdf]] 
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
## Manip four
### PDF 
![[03_Labo_Linux_Permissions_acces-ELEVES-.pdf]] 
### Réponses


