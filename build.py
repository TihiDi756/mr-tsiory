#!/usr/bin/env python3
"""Génère le site statique dans ./public. Usage : python3 build.py
Toutes les coordonnées et textes à compléter sont en haut de ce fichier."""
import os, html, re
E = "andriamanjarisoatsiory@gmail.com"
SITE = "https://Mr-Tsiory.netlify.app"   # À REMPLACER par l'URL Netlify ou le domaine réel
TEL = "+261389722961"        # À COMPLÉTER : numéro professionnel (ex. +261 ...)
WHATSAPP = "+261376790839"   # À COMPLÉTER : numéro WhatsApp (format international sans +)
TAGLINE = "Organiser. Contrôler. Piloter. Progresser."
OUT = "public"
TODO = '<span class="todo">[À compléter par MR TSIORY]</span>'

SERVICES = [
 ("Diagnostic & Business Analysis","150 000 Ar","Analyser le fonctionnement de l'entreprise et identifier les problèmes, les risques et les possibilités d'amélioration.",
  ["Analyse du fonctionnement","Identification des dysfonctionnements","Évaluation des méthodes de gestion","Identification des risques","Analyse des besoins","Recommandations et plan d'amélioration"],"Rapport de diagnostic et plan d'action."),
 ("Business Organization","250 000 à 400 000 Ar","Structurer l'organisation de l'entreprise.",
  ["Organisation des processus","Définition des responsabilités","Élaboration des procédures","Circuits de validation","Organisation du contrôle","Définition des indicateurs"],"Dossier d'organisation et procédures opérationnelles."),
 ("Management Systems Implementation","500 000 à 800 000 Ar","Concevoir et installer un système de gestion adapté.",
  ["Analyse des besoins et conception","Achats et fournisseurs","Stocks","Ventes et charges","Centralisation, automatisation","Tableaux de bord, rapports, formation"],"Système configuré, testé, documenté et installé."),
 ("Digital Transformation","À partir de 1 000 000 Ar","Moderniser les processus et intégrer des solutions numériques.",
  ["Analyse des possibilités de digitalisation","Modernisation des processus","Centralisation des données","Intégration des systèmes","Automatisation avancée","Déploiement et formation"],"Solution intégrée et plan de transformation."),
 ("Technical Support & Maintenance","100 000 à 200 000 Ar/mois","Assurer le suivi technique des systèmes installés.",
  ["Assistance technique","Correction des dysfonctionnements","Vérification du fonctionnement","Maintenance préventive","Suivi périodique"],"Service d'assistance selon contrat."),
]
SECTEURS = [
 ("Restaurants","Achats, fournisseurs, réceptions, stocks, inventaires, recettes, coûts de revient, ventes, marges, charges, rentabilité."),
 ("Bars","Approvisionnements, gestion des boissons, entrées et sorties, contrôle des ventes, stocks, dépenses, rapports."),
 ("Hôtels","Organisation des opérations, suivi des activités, gestion des responsabilités, centralisation des informations, rapports."),
 ("Commerces et distribution","Achats, fournisseurs, stocks, inventaires, ventes, marges, rapports."),
 ("Établissements scolaires et centres de formation","Gestion administrative, suivi des paiements, organisation des activités, centralisation des données, tableaux de bord."),
 ("PME","Organisation générale, procédures, gestion opérationnelle, digitalisation, pilotage."),
]
METHODE = [("Comprendre","Échanger sur l'activité, les contraintes et les objectifs."),("Diagnostiquer","Analyser le fonctionnement réel et repérer les écarts."),
 ("Concevoir","Définir l'organisation et le système adaptés."),("Installer","Mettre en place les outils et les procédures."),
 ("Tester et former","Valider le fonctionnement et former les utilisateurs."),("Livrer et documenter","Remettre les livrables et la documentation.")]
FAQ = [
 ("Qu'est-ce que MR TSIORY ?","Une activité de conseil et de conception de systèmes de gestion d'entreprise. Elle accompagne les dirigeants dans l'organisation, le contrôle des opérations et le pilotage des performances."),
 ("À quelles entreprises s'adressent vos services ?","Notamment aux restaurants, bars, hôtels, commerces, établissements scolaires, centres de formation et PME."),
 ("Travaillez-vous uniquement avec les restaurants ?","Non. La restauration est un secteur important, mais les prestations couvrent plusieurs types d'entreprises."),
 ("Proposez-vous uniquement des logiciels ?","Non. Le travail comprend aussi le diagnostic, le conseil, l'organisation des processus, la définition des responsabilités et la structuration des méthodes de gestion."),
 ("Quelle est la différence entre organisation et système de gestion ?","L'organisation définit les responsabilités, les processus et les procédures. Le système de gestion permet de suivre, enregistrer, contrôler et analyser les opérations qui en découlent."),
 ("Comment se déroule une première collaboration ?","Par une prise de contact et une compréhension des besoins. Selon la situation, un diagnostic peut être réalisé avant de proposer une solution adaptée."),
 ("Le diagnostic est-il obligatoire ?","Il permet de mieux définir les besoins et le périmètre d'intervention. Les modalités sont précisées selon la nature de la demande."),
 ("Combien coûtent vos prestations ?","Les tarifs indicatifs figurent sur la page Tarifs. Le prix définitif dépend du périmètre, de la complexité et des livrables."),
 ("Combien de temps dure une intervention ?","Cela dépend de la prestation, de la complexité du projet et de la disponibilité des informations nécessaires. La durée est précisée dans la proposition commerciale."),
 ("Travaillez-vous à distance ?","Les modalités d'intervention sont définies selon la nature du projet, sa localisation et les besoins de l'entreprise."),
 ("Formez-vous les utilisateurs ?","Oui, lorsque le projet comprend l'installation d'un système nécessitant une prise en main."),
 ("Les systèmes sont-ils personnalisables ?","Ils sont conçus ou configurés selon les besoins et contraintes de chaque entreprise, dans les limites techniques et contractuelles du projet."),
 ("Qu'est-ce que Food Profit 360 ?","Une solution de gestion destinée aux établissements de restauration : achats, stocks, recettes, ventes, charges et suivi de la rentabilité."),
 ("Assurez-vous la maintenance après installation ?","Une assistance et une maintenance peuvent être proposées selon les conditions d'un contrat spécifique."),
 ("Mes informations sont-elles confidentielles ?","Elles sont traitées conformément aux engagements de confidentialité et aux dispositions légales applicables."),
 ("Comment demander un devis ?","Utilisez le formulaire de diagnostic ou contactez MR TSIORY par e-mail."),
 ("Êtes-vous disponible pour des projets spécifiques ?","Oui. Les demandes particulières sont étudiées pour vérifier leur pertinence, leur faisabilité et les ressources nécessaires."),
 ("Comment commencer ?","Contactez MR TSIORY et présentez votre entreprise ainsi que les difficultés que vous souhaitez résoudre."),
]
NAV = [("/","Accueil"),("/a-propos/","À propos"),("/services/","Services"),("/secteurs/","Secteurs"),("/methode/","Méthode"),
       ("/solutions/","Solutions"),("/tarifs/","Tarifs"),("/faq/","FAQ"),("/contact/","Contact")]
e = html.escape
ul = lambda items: "<ul>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"
def btn(href, label, cls=""): return f'<a class="btn {cls}" href="{href}">{e(label)}</a>'
def slug(s): return re.sub(r"[^a-z0-9]+","-",s.lower().replace("é","e").replace("è","e").replace("ô","o")).strip("-")

LOGO = '<svg class="logo-mark" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="6" fill="#14263F"/><path d="M9 29V11h4l7 10 7-10h4v18h-4V18l-7 10-7-10v11z" fill="#fff"/><rect x="9" y="32" width="22" height="2" fill="#C69B54"/></svg>'

def faq_html(items):
    return '<div class="faq">' + "".join(
        f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q,a in items) + '</div>'

def contact_form(form_name="contact"):
    return f'''<form name="{form_name}" method="POST" action="/merci/" data-netlify="true" netlify-honeypot="bot-field" class="form js-form" novalidate>
<input type="hidden" name="form-name" value="{form_name}">
<p class="hp"><label>Ne pas remplir <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<label>Nom<input name="nom" required autocomplete="name"></label>
<label>Adresse e-mail<input type="email" name="email" required autocomplete="email"></label>
<label>Votre message<textarea name="message" rows="5" required minlength="10"></textarea></label>
<label class="check"><input type="checkbox" name="consentement" required> J'accepte que mes données soient utilisées pour traiter ma demande (<a href="/confidentialite/">confidentialité</a>).</label>
<button class="btn primary" type="submit">Envoyer ma demande</button>
<p class="status" role="status" aria-live="polite"></p></form>'''

def diag_form():
    def f(n, label, t="text", req=True, extra=""):
        r = " required" if req else ""
        if t == "area": return f'<label>{label}<textarea name="{n}" rows="3"{r}></textarea></label>'
        return f'<label>{label}<input type="{t}" name="{n}"{r} {extra}></label>'
    diffs = ["Organisation","Achats","Fournisseurs","Stocks","Ventes","Encaissements","Charges","Gestion financière","Rentabilité","Ressources humaines","Digitalisation","Rapports"]
    dchecks = "".join('<label class="check"><input type="checkbox" name="difficultes" value="' + d + '"> ' + d + '</label>' for d in diffs)
    sopts = "".join("<option>" + e(x[0]) + "</option>" for x in SECTEURS)
    return f'''<form name="diagnostic" method="POST" action="/merci/" data-netlify="true" netlify-honeypot="bot-field" class="form js-form js-steps" novalidate>
<input type="hidden" name="form-name" value="diagnostic">
<p class="hp"><label>Ne pas remplir <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>
<fieldset class="step"><legend>1. Identification</legend>
{f("entreprise","Nom de l'entreprise")}{f("dirigeant","Nom du dirigeant","text",True,'autocomplete="name"')}{f("fonction","Fonction")}
<label>Secteur<select name="secteur" required><option value="">Choisir…</option>{sopts}<option>Autre</option></select></label>
{f("localisation","Localisation")}{f("telephone","Téléphone","tel",True,'autocomplete="tel"')}{f("email","Adresse e-mail","email",True,'autocomplete="email"')}
{f("employes","Nombre d'employés","number",False,'min="0"')}{f("etablissements","Nombre d'établissements","number",False,'min="0"')}</fieldset>
<fieldset class="step"><legend>2. Organisation actuelle</legend>
{f("fonctionnement","Comment fonctionne l'entreprise ?","area")}{f("responsabilites","Comment sont organisées les responsabilités ?","area")}
{f("outils","Quels outils sont utilisés ?","area",False)}{f("procedures","Existe-t-il des procédures écrites ?","area",False)}{f("suivi","Comment sont suivies les opérations ?","area",False)}</fieldset>
<fieldset class="step"><legend>3. Difficultés rencontrées</legend><div class="checks">{dchecks}</div></fieldset>
<fieldset class="step"><legend>4. Objectifs</legend>{f("resultats","Résultats attendus","area")}{f("priorites","Améliorations prioritaires","area",False)}{f("echeance","Échéance souhaitée","text",False)}{f("budget","Budget envisagé (facultatif)","text",False)}</fieldset>
<fieldset class="step"><legend>5. Confirmation</legend><div id="recap" class="recap" aria-live="polite"></div>
<label class="check"><input type="checkbox" name="consentement" required> J'accepte le traitement de mes données personnelles pour répondre à ma demande (<a href="/confidentialite/">politique de confidentialité</a>).</label>
<button class="btn primary" type="submit">Envoyer ma demande</button></fieldset>
<div class="steps-nav"><button type="button" class="btn" data-prev>Précédent</button><span class="stepno" aria-live="polite"></span><button type="button" class="btn primary" data-next>Suivant</button></div>
<p class="status" role="status" aria-live="polite"></p></form>'''

def page(path, title, desc, body, h1=None, crumbs=True, schema=""):
    url = SITE + path
    def nav_item(h, l):
        cur = ' aria-current="page"' if h == path else ""
        return f'<li><a href="{h}"{cur}>{l}</a></li>'
    nav = "".join(nav_item(h, l) for h, l in NAV)
    crumb_label = "Fil d'Ariane"
    bc = f'<nav class="crumbs" aria-label="{crumb_label}"><a href="/">Accueil</a> / <span>{e(h1 or title)}</span></nav>' if crumbs and path != "/" else ""
    head = f'<header class="pagehead"><div class="wrap">{bc}<h1>{e(h1)}</h1></div></header>' if h1 else ""
    wa = f'<a class="btn" href="https://wa.me/{WHATSAPP}" rel="noopener noreferrer" target="_blank">WhatsApp</a>' if WHATSAPP else ""
    tel = f'<li><a href="tel:{e(TEL)}">{e(TEL)}</a></li>' if TEL else ""
    full = f"{title} | MR TSIORY" if path != "/" else title
    return f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(full)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{url}">
<meta name="theme-color" content="#14263F"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="manifest" href="/manifest.webmanifest">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_FR"><meta property="og:site_name" content="MR TSIORY"><meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary"><meta name="twitter:title" content="{e(full)}"><meta name="twitter:description" content="{e(desc)}">
<link rel="stylesheet" href="/style.css">{schema}</head><body>
<a class="skip" href="#main">Aller au contenu</a>
<header class="top"><div class="wrap bar"><a class="brand" href="/" aria-label="MR TSIORY, accueil">{LOGO}<span>MR TSIORY<small>Business Consulting &amp; Management Systems</small></span></a>
<button class="burger" aria-expanded="false" aria-controls="menu">Menu</button>
<nav id="menu" aria-label="Navigation principale"><ul>{nav}</ul>{btn("/diagnostic/","Demander un diagnostic","gold")}</nav></div></header>
<main id="main">{head}{body}</main>
<footer class="foot"><div class="wrap cols"><div><div class="brand light">{LOGO}<span>MR TSIORY</span></div><p>{TAGLINE}</p><p>Conseil, organisation, digitalisation, pilotage.</p><p><strong>ALWAYS QUALITY FIRST.</strong></p></div>
<div><h2>Navigation</h2><ul>{"".join(f'<li><a href="{h}">{l}</a></li>' for h,l in NAV[:-1])}<li><a href="/engagements/">Engagements</a></li></ul></div>
<div><h2>Services</h2><ul>{"".join(f'<li><a href="/services/#{slug(s[0])}">{e(s[0])}</a></li>' for s in SERVICES)}</ul></div>
<div><h2>Contact</h2><ul><li><a href="mailto:{E}">{E}</a></li>{tel}<li><a href="/contact/">Formulaire de contact</a></li></ul>{wa}</div></div>
<div class="wrap legal"><a href="/mentions-legales/">Mentions légales</a><a href="/confidentialite/">Confidentialité</a><a href="/cookies/">Cookies</a><a href="/conditions-generales/">Conditions générales</a><span>© {2026} MR TSIORY</span></div></footer>
<a class="totop" href="#main" aria-label="Retour en haut">↑</a><script src="/site.js" defer></script></body></html>'''

def write(path, content):
    d = os.path.join(OUT, path.strip("/"))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(content)

def sec(inner, cls=""): return f'<section class="sec {cls}"><div class="wrap">{inner}</div></section>'
def cta(title="Votre entreprise peut fonctionner avec davantage de structure et de visibilité.",
        txt="Commençons par comprendre votre organisation et identifier les améliorations qui peuvent réellement faire la différence.", b="Demander un diagnostic"):
    return f'<section class="sec cta"><div class="wrap"><h2>{e(title)}</h2><p>{e(txt)}</p>{btn("/diagnostic/",b,"gold")}</div></section>'

def build_pages():
    org = {"@context":"https://schema.org","@type":"ProfessionalService","name":"MR TSIORY — Business Consulting & Management Systems","url":SITE,"email":E,
           "slogan":TAGLINE,"areaServed":"MG","description":"Conseil en organisation et conception de systèmes de gestion d'entreprise."}
    import json
    schema = f'<script type="application/ld+json">{json.dumps(org, ensure_ascii=False)}</script>'
    probs = ["Informations dispersées","Absence de procédures claires","Difficultés de contrôle des stocks","Manque de visibilité sur les achats","Écarts de caisse",
             "Dépenses mal suivies","Marges difficiles à connaître","Dépendance excessive au dirigeant","Rapports de gestion insuffisants","Décisions prises sans informations fiables"]
    piliers = [("Organiser","Structurer les activités, définir les responsabilités et formaliser les procédures."),("Contrôler","Suivre les opérations, centraliser les données et renforcer les mécanismes de contrôle."),("Piloter","Analyser les résultats, suivre les indicateurs et faciliter les décisions.")]
    cards = "".join(f'<article class="card"><h3>{e(s[0])}</h3><p>{e(s[2])}</p>{ul(s[3][:3])}<a href="/services/#{slug(s[0])}">Découvrir le service</a></article>' for s in SERVICES)
    fp = ["Fournisseurs et achats","Réceptions et factures","Paiements fournisseurs","Stocks et inventaires","Ingrédients et compositions","Recettes et coûts","Ventes et chiffre d'affaires","Charges et dépenses","Marges et rentabilité","Tableaux de bord et rapports"]
    why = ["Des solutions adaptées aux réalités de l'entreprise","Une approche structurée","Des livrables clairement définis","Des outils compréhensibles","Des systèmes documentés","Une attention particulière à la fiabilité","Une logique d'amélioration continue"]
    hero = f'''<section class="hero"><div class="wrap heroin"><div><h1>Organisez votre entreprise. Maîtrisez vos opérations. Pilotez vos performances.</h1>
<p class="lead">MR TSIORY accompagne les entreprises dans leur organisation, leur gestion opérationnelle et leur transformation numérique grâce à des méthodes professionnelles et des systèmes de gestion adaptés à leurs activités.</p>
<p class="btns">{btn("/services/","Découvrir nos services","gold")}{btn("/diagnostic/","Demander un diagnostic","ghost")}</p></div>
<figure class="ph" role="img" aria-label="Emplacement réservé : photographie professionnelle d'un tableau de bord ou d'une situation de travail"><span>Image à remplacer<br><small>/images/hero.webp</small></span></figure></div></section>'''
    body = hero + sec(f'<h2>Une entreprise peut travailler beaucoup sans toujours maîtriser ses performances.</h2><ul class="grid2 plain">{"".join(f"<li>{e(p)}</li>" for p in probs)}</ul><p class="note">Ces difficultés ne nécessitent pas toujours davantage de travail. Elles nécessitent souvent une meilleure organisation et des systèmes de gestion adaptés.</p>','alt')
    body += sec(f'<h2>Notre réponse : trois piliers</h2><div class="grid3">{"".join(f"<article class=card><h3>{a}</h3><p>{b}</p></article>" for a,b in piliers)}</div>')
    body += sec(f'<h2>Nos services</h2><div class="grid3">{cards}</div>','alt')
    sect_tags = "".join('<li><a href="/secteurs/#' + slug(x[0]) + '">' + e(x[0].replace(" et centres de formation", "")) + '</a></li>' for x in SECTEURS)
    body += sec('<h2>Nos secteurs d\'intervention</h2><ul class="tags">' + sect_tags + '</ul>')
    body += sec(f'<h2>Des systèmes conçus pour transformer la gestion en véritable outil de pilotage.</h2><p>Food Profit 360, solution de gestion pour la restauration :</p>{ul(fp)}<p>{btn("/solutions/","Découvrir Food Profit 360")}</p>','alt')
    body += sec(f'<h2>Notre méthode</h2><ol class="steps">{"".join(f"<li><strong>{a}</strong> {b}</li>" for a,b in METHODE)}</ol>')
    body += sec(f'<h2>Pourquoi travailler avec MR TSIORY ?</h2>{ul(why)}<p class="note">MR TSIORY est une activité de conseil indépendante : vous échangez directement avec la personne qui analyse et conçoit votre solution.</p>','alt')
    body += cta() + sec(f'<h2>Questions fréquentes</h2>{faq_html(FAQ[:6])}<p>{btn("/faq/","Toutes les questions")}</p>')
    write("/", page("/","MR TSIORY — Consultant en organisation et systèmes de gestion à Madagascar","Conseil en organisation, systèmes de gestion et digitalisation pour restaurants, hôtels, commerces et PME à Madagascar. Demandez un diagnostic.",body,schema=schema))

    # À propos
    b = sec(f'''<p class="lead">MR TSIORY est une activité professionnelle portée par un consultant qui privilégie l'analyse, la structuration et les résultats concrets.</p>
<h2>Une approche fondée sur la compréhension du terrain</h2><p>Chaque entreprise possède ses propres réalités. Avant de proposer un outil ou une méthode, il est essentiel de comprendre ses activités, ses contraintes, ses processus et ses objectifs.</p>
<h2>Mission</h2><p>Aider les entreprises à mieux s'organiser, mieux contrôler leurs opérations et mieux piloter leurs performances grâce à des systèmes de gestion adaptés à leur activité.</p>
<h2>Vision</h2><p>Contribuer à la modernisation des entreprises en développant des organisations plus structurées, des opérations mieux maîtrisées et des systèmes de gestion durables.</p>
<h2>Philosophie</h2><p>La performance repose sur une organisation claire, un contrôle efficace des opérations et un pilotage fondé sur des informations fiables.</p>
<h2>Valeurs</h2>{ul(["Professionnalisme","Qualité","Fiabilité","Organisation","Transparence","Simplicité d'utilisation","Efficacité opérationnelle","Évolutivité","Responsabilité"])}
<h2>Le fondateur</h2><figure class="ph small" role="img" aria-label="Emplacement réservé : photographie professionnelle du fondateur"><span>Photo à ajouter<br><small>/images/fondateur.webp</small></span></figure>
<p>{TODO} Présentation personnelle du fondateur (parcours, motivations).</p><p>{btn("/methode/","Voir la méthode d'intervention")} {btn("/diagnostic/","Parler de mon projet","primary")}</p>''')
    write("/a-propos/", page("/a-propos/","À propos","Comprendre l'entreprise avant de transformer sa gestion : mission, vision, valeurs et approche de MR TSIORY.",b,"Comprendre l'entreprise avant de transformer sa gestion."))

    # Services
    parts = ""
    for n,price,obj,inter,liv in SERVICES:
        parts += f'<article class="svc" id="{slug(n)}"><h2>{e(n)}</h2><p class="price">Tarif indicatif : {e(price)}</p><p><strong>Objectif :</strong> {e(obj)}</p><h3>Interventions</h3>{ul(inter)}<p><strong>Livrable :</strong> {e(liv)}</p><p>{btn("/diagnostic/","Demander un devis")}</p></article>'
    parts += '<p class="note">Ces tarifs sont indicatifs. Le devis final dépend de la complexité et du périmètre du projet.</p>'
    write("/services/", page("/services/","Nos services","Cinq prestations : diagnostic, organisation, systèmes de gestion, transformation digitale, maintenance. Tarifs indicatifs en Ariary.",sec(parts),"Nos services"))

    # Secteurs
    parts = "".join(f'<article class="svc" id="{slug(n)}"><h2>{e(n)}</h2><p>{e(t)}</p><p>{btn("/diagnostic/","Étudier les besoins de mon entreprise")}</p></article>' for n,t in SECTEURS)
    write("/secteurs/", page("/secteurs/","Secteurs d'intervention","Restaurants, bars, hôtels, commerces, établissements scolaires et PME : les besoins de gestion que MR TSIORY accompagne.",sec(parts),"Nos secteurs d'intervention"))

    # Méthode
    b = sec(f'<ol class="steps big">{"".join(f"<li><h2>{a}</h2><p>{c}</p></li>" for a,c in METHODE)}</ol>'
            '<h2>Votre rôle</h2><p>Fournir les informations nécessaires sur l\'activité, valider les étapes clés et désigner un interlocuteur.</p>'
            '<h2>Ce que vous recevez à la fin de l\'intervention</h2>'+ul(["Les livrables définis dans la proposition","Un système ou des procédures testés","Une documentation d\'utilisation","Une prise en main des utilisateurs, si prévue"])+
            '<p class="note">Aucun résultat financier n\'est garanti : les bénéfices dépendent de la situation de chaque entreprise et de l\'usage des outils.</p>')
    write("/methode/", page("/methode/","Notre méthode","Six étapes : comprendre, diagnostiquer, concevoir, installer, tester et former, livrer et documenter.",b+cta(),"Notre méthode d'intervention"))

    # Solutions
    b = sec(f'''<p class="lead">MR TSIORY conçoit des systèmes de gestion et des applications métier adaptés à l'activité de chaque entreprise.</p>
{ul(["Systèmes de gestion opérationnelle","Outils de centralisation des données","Tableaux de bord","Rapports automatisés","Applications métier","Solutions de digitalisation"])}
<h2 id="food-profit-360">Food Profit 360</h2><p>Solution de gestion destinée aux établissements de restauration (restaurants, bars, hôtels-restaurants). Objectif : transformer la gestion en outil de pilotage de la rentabilité.</p>
<h3>Modules</h3>{ul(fp)}<h3>Captures d'écran</h3><figure class="ph small" role="img" aria-label="Emplacement réservé : capture d'écran réelle de Food Profit 360"><span>Captures réelles à ajouter<br><small>/images/fp360-1.webp</small></span></figure>
<p>{btn("/contact/","Poser une question","primary")}</p>''')
    write("/solutions/", page("/solutions/","Solutions numériques","Systèmes de gestion, tableaux de bord et applications métier. Découvrez Food Profit 360 pour la restauration.",b,"Solutions numériques"))

    # Engagements
    eng = ["Professionnalisme","Qualité","Fiabilité","Clarté","Transparence","Documentation","Maintenabilité","Évolutivité","Respect des délais convenus","Confidentialité des informations clients"]
    write("/engagements/", page("/engagements/","Nos engagements","Professionnalisme, qualité, transparence, documentation et confidentialité : les engagements de MR TSIORY.",
        sec(ul(eng)+'<p class="note">Chaque intervention est encadrée par des objectifs, des livrables, des délais et des conditions clairement établis.</p>')+cta(),"Nos engagements"))

    # Tarifs
    rows = "".join(f"<tr><th scope='row'>{e(s[0])}</th><td>{e(s[1])}</td></tr>" for s in SERVICES)
    write("/tarifs/", page("/tarifs/","Offres et tarifs","Tarifs indicatifs des cinq prestations de MR TSIORY, en Ariary. Devis définitif après analyse des besoins.",
        sec(f'<div class="scroll"><table><caption class="sr">Tarifs indicatifs</caption><thead><tr><th scope="col">Prestation</th><th scope="col">Tarif indicatif</th></tr></thead><tbody>{rows}</tbody></table></div><p class="note">Les tarifs définitifs sont établis après compréhension des besoins, évaluation de la complexité et définition des livrables.</p><p>{btn("/diagnostic/","Demander un devis","primary")}</p>'),"Offres et tarifs"))

    # Diagnostic, contact, faq, merci
    write("/diagnostic/", page("/diagnostic/","Demander un diagnostic","Formulaire de demande de diagnostic pour votre entreprise : décrivez votre organisation et vos difficultés.",sec("<p>Cinq étapes courtes. Vos réponses servent uniquement à préparer notre échange.</p>"+diag_form()),"Demander un diagnostic"))
    wa = f'<p>{btn("https://wa.me/"+WHATSAPP,"WhatsApp")}</p>' if WHATSAPP else ""
    b = sec(f'<div class="grid2"><div><h2>Écrire à MR TSIORY</h2><p>Je réponds aux demandes par e-mail ; indiquez votre activité et votre besoin.</p>'
            f'<p><a class="btn primary" href="mailto:{E}?subject=Demande%20de%20contact">{E}</a></p><p><button class="btn" type="button" data-copy="{E}">Copier l\'adresse e-mail</button> <span class="status" role="status" aria-live="polite" id="copied"></span></p>'
            f'<p>Téléphone : {e(TEL) if TEL else TODO}</p>{wa}<p>{btn("/diagnostic/","Demander un diagnostic")}</p></div><div><h2>Formulaire de contact</h2>{contact_form()}</div></div>')
    write("/contact/", page("/contact/","Contact","Contactez MR TSIORY par e-mail ou via le formulaire pour poser une question ou demander un devis.",b,"Contact"))
    write("/faq/", page("/faq/","FAQ","Réponses aux questions fréquentes sur les services, tarifs, méthode et confidentialité de MR TSIORY.",sec(faq_html(FAQ)+f'<p>{btn("/diagnostic/","Demander un diagnostic","primary")}</p>'),"Foire aux questions"))
    write("/merci/", page("/merci/","Merci","Votre demande a été transmise.",sec("<p>Merci pour votre demande. Votre message a bien été transmis à MR TSIORY. Nous reviendrons vers vous par les coordonnées communiquées.</p>"+btn("/","Retour à l'accueil")),"Merci",crumbs=False))
    # Légal (modèles à compléter)
    note = '<p class="warn"><strong>Modèle à compléter et à faire valider juridiquement avant publication.</strong></p>'
    legal = {
     "mentions-legales":("Mentions légales",f"<h2>Éditeur</h2><p>MR TSIORY — Business Consulting &amp; Management Systems</p><p>Statut juridique : {TODO}<br>Immatriculation : {TODO}<br>Adresse professionnelle : {TODO}<br>Contact : <a href='mailto:{E}'>{E}</a></p><h2>Responsable de publication</h2><p>{TODO}</p><h2>Hébergeur</h2><p>Netlify, Inc. — coordonnées légales à vérifier sur netlify.com au moment de la publication.</p><h2>Propriété intellectuelle</h2><p>Les contenus du site sont la propriété de MR TSIORY, sauf mention contraire.</p><h2>Responsabilité</h2><p>Les informations et tarifs sont indicatifs ; seuls les devis et contrats signés engagent MR TSIORY.</p>"),
     "confidentialite":("Politique de confidentialité",f"<h2>Données collectées</h2><p>Les informations saisies dans les formulaires de contact et de diagnostic (identité, entreprise, coordonnées, description des besoins).</p><h2>Finalité</h2><p>Répondre aux demandes et préparer une éventuelle collaboration.</p><h2>Destinataires et prestataires</h2><p>MR TSIORY. Les formulaires sont traités via Netlify Forms (hébergeur).</p><h2>Durée de conservation</h2><p>{TODO} (durée à définir).</p><h2>Vos droits</h2><p>Accès, rectification, suppression : écrivez à <a href='mailto:{E}'>{E}</a>.</p><h2>Responsable du traitement</h2><p>MR TSIORY, <a href='mailto:{E}'>{E}</a>.</p>"),
     "cookies":("Politique de cookies","<p>Ce site n'utilise aucun cookie publicitaire ni de suivi. Aucune bannière de consentement n'est donc affichée. Si un outil de mesure d'audience nécessitant un consentement est ajouté, cette page et un mécanisme de consentement seront mis à jour.</p>"),
     "conditions-generales":("Conditions générales",f"<p>Les prestations sont encadrées par des devis et contrats signés ou acceptés. Sections à rédiger : {TODO} conditions d'intervention, devis, paiements, délais, livrables, modifications, responsabilités, confidentialité, maintenance, résiliation.</p>"),
    }
    for s,(t,c) in legal.items():
        write(f"/{s}/", page(f"/{s}/",t,f"{t} du site MR TSIORY.",sec(note+c),t))
    nf = "<p>Cette page n'existe pas ou a été déplacée.</p>" + btn("/","Retour à l'accueil") + " " + btn("/contact/","Nous contacter")
    open(os.path.join(OUT,"404.html"),"w",encoding="utf-8").write(page("/404.html","Page introuvable","Page introuvable.",sec(nf),"Page introuvable",crumbs=False))
    paths = ["/"]+[h for h,_ in NAV[1:]]+["/engagements/","/diagnostic/"]+[f"/{s}/" for s in legal]
    open(os.path.join(OUT,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE}{p}</loc></url>" for p in paths)+"</urlset>")
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    open(os.path.join(OUT,"favicon.svg"),"w").write(LOGO.replace('class="logo-mark" ','xmlns="http://www.w3.org/2000/svg" '))
    open(os.path.join(OUT,"manifest.webmanifest"),"w").write('{"name":"MR TSIORY","short_name":"MR TSIORY","start_url":"/","display":"browser","theme_color":"#14263F","background_color":"#FFFFFF","icons":[{"src":"/favicon.svg","sizes":"any","type":"image/svg+xml"}]}')

CSS = """
:root{--navy:#14263F;--navy2:#233D5B;--gold:#C69B54;--grey:#F1F3F5;--mute:#536273;--ink:#202B38}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:5rem}
body{margin:0;font:1rem/1.65 Manrope,Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:#fff}
img,svg{max-width:100%}a{color:var(--navy2)}:focus-visible{outline:3px solid var(--gold);outline-offset:2px}
.wrap{width:min(1120px,100% - 2rem);margin:auto}.skip{position:absolute;left:-999px}.skip:focus{left:1rem;top:1rem;background:#fff;padding:.5rem;z-index:99}
h1,h2,h3{font-family:Manrope,Inter,system-ui,sans-serif;line-height:1.2;color:var(--navy);margin:1.6rem 0 .6rem}h1{font-size:clamp(1.8rem,5vw,3rem);margin-top:0}h2{font-size:clamp(1.4rem,3.2vw,2rem)}h3{font-size:1.15rem}
p,li{max-width:72ch}.lead{font-size:1.15rem}.note{border-left:4px solid var(--gold);padding-left:1rem;color:var(--mute)}.warn{background:#fff6e5;padding:.75rem 1rem;border:1px solid var(--gold)}
.todo{background:#fff6e5;border:1px dashed var(--gold);padding:0 .35rem}
.top{position:sticky;top:0;background:#fff;border-bottom:1px solid #dde2e7;z-index:50}.bar{display:flex;align-items:center;justify-content:space-between;gap:1rem;min-height:4rem;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:.6rem;text-decoration:none;color:var(--navy);font-weight:800;line-height:1.1}.brand small{display:block;font-weight:500;font-size:.62rem;color:var(--mute)}.brand.light{color:#fff}.logo-mark{width:36px;height:36px}
#menu ul{display:flex;gap:1rem;list-style:none;margin:0;padding:0;flex-wrap:wrap}#menu{display:flex;align-items:center;gap:1rem}#menu a:not(.btn){text-decoration:none;color:var(--ink);font-size:.92rem;padding:.4rem 0;border-bottom:2px solid transparent}#menu a[aria-current]{border-color:var(--gold);font-weight:700}
.burger{display:none;min-height:44px;padding:0 1rem;border:1px solid var(--navy);background:#fff;border-radius:6px;font:inherit}
.btn{display:inline-block;min-height:44px;padding:.65rem 1.1rem;border:2px solid var(--navy);border-radius:6px;background:#fff;color:var(--navy);font:700 .95rem Manrope,sans-serif;text-decoration:none;cursor:pointer;margin:.2rem .3rem .2rem 0}
.btn.primary{background:var(--navy);color:#fff}.btn.gold{background:var(--gold);border-color:var(--gold);color:var(--navy)}.btn.ghost{background:transparent;border-color:#fff;color:#fff}
.hero{background:var(--navy);color:#fff;padding:3rem 0}.hero h1{color:#fff}.heroin{display:grid;gap:2rem;align-items:center}.hero .lead{color:#dbe3ec}
.ph{margin:0;min-height:260px;display:grid;place-items:center;text-align:center;border:2px dashed var(--gold);color:var(--gold);background:rgba(255,255,255,.04)}.ph.small{min-height:180px;color:var(--mute);background:var(--grey)}
.sec{padding:3rem 0}.alt{background:var(--grey)}.cta{background:var(--navy2);color:#fff;text-align:center}.cta h2{color:#fff}.cta p{margin:0 auto 1rem}
.grid2,.grid3{display:grid;gap:1.2rem}.plain{list-style:none;padding:0}.plain li{background:#fff;padding:.8rem 1rem;border-left:4px solid var(--gold)}
.card{background:#fff;border:1px solid #dde2e7;border-radius:8px;padding:1.2rem}.card h3{margin-top:0}.tags{display:flex;flex-wrap:wrap;gap:.6rem;list-style:none;padding:0}.tags a{display:block;padding:.6rem 1rem;border:1px solid var(--navy2);border-radius:99px;text-decoration:none}
.steps{padding-left:1.2rem}.steps li{margin:.5rem 0}.svc{padding:1.2rem 0;border-bottom:1px solid #dde2e7}.price{color:var(--gold);font-weight:800;filter:brightness(.7)}
.pagehead{background:var(--grey);padding:2rem 0 1rem}.crumbs{font-size:.85rem;color:var(--mute);margin-bottom:.5rem}
.faq details{border:1px solid #dde2e7;border-radius:6px;margin:.5rem 0;background:#fff}.faq summary{cursor:pointer;padding:.9rem 1rem;font-weight:700;min-height:44px}.faq p{padding:0 1rem 1rem;margin:0}
table{border-collapse:collapse;width:100%}th,td{padding:.8rem;border-bottom:1px solid #dde2e7;text-align:left}thead th{background:var(--navy);color:#fff}.scroll{overflow-x:auto}.sr{position:absolute;left:-999px}
.form{display:grid;gap:1rem;max-width:680px}.form label{display:grid;gap:.3rem;font-weight:600}input,select,textarea{font:inherit;padding:.7rem;border:1px solid #8a97a6;border-radius:6px;min-height:44px;width:100%}
.check{display:flex!important;gap:.6rem;align-items:flex-start;font-weight:400!important}.check input{width:auto;min-height:0;margin-top:.35rem}.checks{display:grid;gap:.4rem}fieldset{border:1px solid #dde2e7;padding:1rem;border-radius:8px;display:grid;gap:1rem}legend{font-weight:800;color:var(--navy)}
.hp{position:absolute;left:-9999px}.steps-nav{display:none;justify-content:space-between;align-items:center}.js-on .steps-nav{display:flex}.js-on .step{display:none}.js-on .step.on{display:grid}
.status{font-weight:700}.status.err,.err-msg{color:#a31d1d}.status.ok{color:#17663a}input[aria-invalid=true],textarea[aria-invalid=true],select[aria-invalid=true]{border-color:#a31d1d}.recap{background:var(--grey);padding:1rem;border-radius:6px;font-size:.92rem}
.foot{background:var(--navy);color:#dbe3ec;padding:2.5rem 0 1rem}.foot a{color:#dbe3ec}.foot h2{color:#fff;font-size:1rem;margin-top:0}.foot ul{list-style:none;padding:0}.cols{display:grid;gap:1.5rem}.legal{display:flex;gap:1rem;flex-wrap:wrap;margin-top:1.5rem;padding-top:1rem;border-top:1px solid #ffffff33;font-size:.85rem}
.totop{position:fixed;right:1rem;bottom:1rem;width:44px;height:44px;display:grid;place-items:center;background:var(--navy);color:#fff;border-radius:50%;text-decoration:none;opacity:.9}
@media(min-width:760px){.heroin{grid-template-columns:1.3fr 1fr}.grid2{grid-template-columns:1fr 1fr}.grid3{grid-template-columns:repeat(3,1fr)}.cols{grid-template-columns:1.3fr 1fr 1.4fr 1.3fr}}
@media(max-width:1020px){.burger{display:block}#menu{display:none;width:100%;flex-direction:column;align-items:stretch;padding-bottom:1rem}#menu.open{display:flex}#menu ul{flex-direction:column;gap:0}#menu a:not(.btn){display:block;padding:.75rem 0}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}*{transition:none!important;animation:none!important}}
"""

JS = r"""(()=>{
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const b=$('.burger'),m=$('#menu');
if(b){b.onclick=()=>{const o=m.classList.toggle('open');b.setAttribute('aria-expanded',o)};$$('#menu a').forEach(a=>a.onclick=()=>{m.classList.remove('open');b.setAttribute('aria-expanded',false)})}
$$('[data-copy]').forEach(x=>x.onclick=async()=>{const s=$('#copied');try{await navigator.clipboard.writeText(x.dataset.copy);s.textContent='Adresse copiée.'}catch{s.textContent='Copie impossible : sélectionnez l\u2019adresse manuellement.'}});
const OK="Merci pour votre demande. Votre message a bien été transmis à MR TSIORY. Nous reviendrons vers vous par les coordonnées communiquées.";
const KO="Votre message n\u2019a pas pu être transmis. Veuillez réessayer ou nous contacter directement par e-mail.";
$$('.js-form').forEach(f=>{
 const st=$('.status',f),steps=$$('.step',f);let i=0;
 const valid=(scope)=>{let ok=true;$$('input,select,textarea',scope).forEach(el=>{if(el.name==='bot-field')return;const bad=!el.checkValidity();el.setAttribute('aria-invalid',bad);if(bad&&ok){ok=false;el.focus();st.className='status err';st.textContent='Veuillez corriger : '+(el.closest('label')?.firstChild?.textContent||el.name)+'.'}});if(ok)st.textContent='';return ok};
 const show=()=>{steps.forEach((s,k)=>s.classList.toggle('on',k===i));$('.stepno',f).textContent='Étape '+(i+1)+' sur '+steps.length;$('[data-prev]',f).hidden=i===0;$('[data-next]',f).hidden=i===steps.length-1;
  if(i===steps.length-1){const d=new FormData(f),r=$('#recap');r.textContent='';[...d.entries()].filter(([k,v])=>v&&!['form-name','bot-field','consentement'].includes(k)).forEach(([k,v])=>{const p=document.createElement('div');p.textContent=k+' : '+v;r.appendChild(p)})}};
 if(steps.length){f.classList.add('js-on');show();$('[data-next]',f).onclick=()=>{if(valid(steps[i])){i++;show()}};$('[data-prev]',f).onclick=()=>{i--;show()}}
 f.addEventListener('submit',async ev=>{ev.preventDefault();if(steps.length){f.classList.remove('js-on')}if(!valid(f)){if(steps.length)f.classList.add('js-on');return}
  const btn=$('button[type=submit]',f);btn.disabled=true;st.className='status';st.textContent='Envoi en cours…';
  try{const body=new URLSearchParams(new FormData(f)).toString();const r=await fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body});
   if(!r.ok)throw new Error(r.status);st.className='status ok';st.textContent=OK;f.reset();$$('.step',f).forEach(s=>s.style.display='none')}
  catch{st.className='status err';st.textContent=KO;btn.disabled=false;if(steps.length)f.classList.add('js-on')}});
});})();"""

TOML = """[build]
  command = "python3 build.py"
  publish = "public"

[build.environment]
  PYTHON_VERSION = "3.11"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "camera=(), microphone=(), geolocation=()"
    Content-Security-Policy = "default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; form-action 'self'; frame-ancestors 'none'; base-uri 'self'"
    Strict-Transport-Security = "max-age=31536000"

[[headers]]
  for = "/*.css"
  [headers.values]
    Cache-Control = "public, max-age=86400"
"""

README = """# MR TSIORY — site statique

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
"""

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    build_pages()
    open(os.path.join(OUT,"style.css"),"w").write(CSS)
    open(os.path.join(OUT,"site.js"),"w").write(JS)
    open("netlify.toml","w").write(TOML)
    open("README.md","w").write(README)
    open(".gitignore","w").write(".DS_Store\nnode_modules\n")
    print("OK")
