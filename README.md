Ce projet utilise Stramlit, une BDD sous Docker ainsi qu'un espace virtuel sous WSL, les bibliothèques pandas, matplotlib et mysql.connector afin d'afficher les horaires des lignes de bus et des statistiques.

Voici le brief du projet : 

    A partir de la base de donnée décrit par le schéma en PJ, mettre en place la base de données Breizhibus et importer les données.

    Attention : pour des raisons de sécurité, il ne faut pas utiliser le compte root dans le code Python. Vous devez donc créer un utilisateur pour votre appli qui n'a de droit que sur la base Breizhibus.

    Puis créer une appli Streamlit qui exploite cette bdd et qui contient 2 pages :

        - la première affiche le nom de l'appli, la carte du réseau de bus (une image trouvée sur le web suffit), et les horaires par lignes. Ce dernier affichage doit être interactif, c'est à dire que l'utilisateur peut choisir sa ligne et la page affiche les horaires correspondantes.
        - la deuxième sert pour les services internes de Breizhibus. Elle affiche 3 graphiques : un histogramme des fréquentations par lignes, un graphique des fréquentations par heures et un camenbert des fréquentations par jours.
