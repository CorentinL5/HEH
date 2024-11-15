---
created: 2024-10-01
tags:
  - Lessons/School/HEH/Bloc2/Quad1
---

# # 📚  M5 - Serveur DNS
> **Création de la note à *`08:20`* le *`2024-10-01`.***
---

# 📝 Prise de Notes - Cours

---
Sans serveur DNS, rien ne fonctionne 

qqchose.qqchose pour une adresse
mais faut être logique et ne pas mettre n'importe quoi


Serveur de nom
	SOA
	NS
	A / AAAA : redirection
	PTR
	CNAME
	MX : mail
	SRV

11. Zone de stub #exam 
		Permet de 


## Questions d'examen 
> #exam 
> ![[Windows Server v2019.pdf#page=79|noscroll]]
> ![[Windows Server v2019.pdf#page=80|noscroll]]
1. **Rôle du champ TTL :**
	   Le champ TTL (Time To Live) définit combien de temps un enregistrement DNS peut être mis en cache par un résolveur avant d'être revalidé auprès du serveur DNS d'origine.

2. **Type d'enregistrement pour www.société.be pointant vers srv.société.be :**
	   Utiliser un enregistrement **CNAME** pour que `www.société.be` redirige vers `srv.société.be`.

3. **Commande pour forcer le réenregistrement DNS :** 
   ```
	   ipconfig /registerdns
   ```
   Cette commande met à jour le nom d'hôte et l'adresse IP auprès du serveur DNS.

4. **Commande pour afficher le cache DNS :** 
   ```
	   ipconfig /displaydns
   ```
   Elle montre les enregistrements DNS mis en cache localement.

5. **Commande pour vider le cache DNS :** 
   ```
	   ipconfig /flushdns
   ```
	   Cela vide le cache DNS local, obligeant à réinterroger les serveurs DNS.

6. **Vous mettez en œuvre deux serveurs DNS. L'un d'eux hébergera une zone principale standard et le second une zone secondaire standard dans un souci de tolérance de panne et de répartition de charge. Les mises à jour dynamiques sont activées. 
   Est-ce qu'un client DNS Windows du serveur DNS hébergeant la zone secondaire standard (donc en lecture seule) sera capable d'enregistrer dynamiquement ses enregistrements auprès de son serveur DNS ?**
	Non, un client DNS Windows **ne pourra pas enregistrer dynamiquement ses enregistrements** auprès d'un serveur DNS hébergeant une **zone secondaire standard**, car cette zone est en lecture seule. Les mises à jour dynamiques ne sont possibles que sur la **zone principale standard**. Pour enregistrer ses enregistrements, le client doit s'adresser au serveur hébergeant la zone principale.
	
	Si vous voulez que plusieurs serveurs acceptent des mises à jour dynamiques et assurent la tolérance de panne, il vaut mieux utiliser une **zone intégrée à Active Directory (AD-integrated)**, qui permet la réplication entre les serveurs et supporte les écritures sur plusieurs serveurs DNS
