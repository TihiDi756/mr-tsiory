# MR TSIORY — site statique

Site HTML/CSS/JS sans dépendance. Python 3 génère les pages (aucun npm requis).

## Modifier les contenus
Ouvrez `build.py` : coordonnées (`TEL`, `WHATSAPP`, `SITE`) et textes (services, FAQ…) sont en haut. Puis : `python3 build.py`.
Les textes marqués « À compléter par MR TSIORY » sont des champs à remplir (juridique, fondateur, durée de conservation).

## Remplacer les images
Placez vos fichiers WebP dans `public/images/` (créez le dossier) et remplacez les blocs `.ph` dans `build.py` par `<img src="/images/..." alt="..." width= height= loading="lazy">`.

## Déployer gratuitement sur Netlify
1. Mettez ce dossier sur GitHub. 2. Netlify > Add new site > Import from Git. 3. Build : `python3 build.py`, publication : `public` (déjà dans `netlify.toml`).
4. Mettez l'URL réelle dans `SITE` (build.py), puis redéployez.
5. Formulaires : Netlify > Forms détecte `contact` et `diagnostic` au déploiement. Activez les notifications e-mail vers andriamanjarisoatsiory@gmail.com (Forms > Settings > Notifications). Offre gratuite : environ 100 envois/mois.
6. Domaine : Domain management > Add domain (ex. mrtsiory.com), puis suivez les DNS indiqués. Google Search Console : ajoutez la propriété et soumettez `/sitemap.xml`.

## Reste à fournir
Téléphone, WhatsApp, adresse, photo du fondateur, logo définitif, domaine, informations juridiques (à faire valider), témoignages autorisés, captures réelles de Food Profit 360, réseaux sociaux.
Aucun test Lighthouse ni de déploiement réel n'a été exécuté : à faire après publication.
