# Script de soutenance — ML2 Customer Segmentation

Durée cible : **13 min 55 s**. Saad présente les diapositives 1 à 15, puis Hassan présente les diapositives 16 à 29. Les transitions sont volontairement courtes afin de réserver le temps aux méthodes et aux résultats.

## Saad Sahraoui — comprendre et préparer

### Diapositive 1 — 2026/2027 / Machine Learning 2 · Projet académique — 20 s

Bonjour à toutes et à tous. Nous présentons notre projet de segmentation de clients d’un distributeur en gros, réalisé dans le cadre de Machine Learning 2 à l’ENSAM Rabat. Nous sommes Saad Sahraoui et Hassan El Hajjam, encadrés par le professeur Safaâ Dafrallah.

Le projet compare K-Means, la CAH Ward et DBSCAN sur des dépenses clients réelles.

**Transition :** Nous commençons par la logique générale de la soutenance.

### Diapositive 2 — Plan de la soutenance — 15 s

La présentation suit quatre étapes. Nous allons d’abord comprendre le contexte, les données et leur qualité. Nous préparerons ensuite l’espace des distances. Nous présenterons les trois méthodes de clustering, puis nous terminerons par la comparaison, les profils et les perspectives.

**Transition :** La première partie pose la question métier.

### Diapositive 3 — Comprendre — 15 s

Cette diapositive sépare la phase de compréhension du reste du projet. Nous partons du contexte, de la structure du dataset et des contrôles de qualité avant d’appliquer une distance ou un algorithme.

**Transition :** Pourquoi chercher des groupes de clients ?

### Diapositive 4 — Contexte métier & problématique — 30 s

Un distributeur peut servir des clients dont les comportements d’achat sont très différents. Les dépenses annuelles mélangent plusieurs catégories et ne donnent pas directement des segments lisibles.

Notre question est donc : quels groupes émergent naturellement des six dépenses, et quelle méthode fournit le compromis le plus utile ? Il n’y a pas de classe cible fournie à l’avance. Nous sommes donc dans un problème d’apprentissage non supervisé.

**Transition :** Cette question devient plusieurs objectifs mesurables.

### Diapositive 5 — Objectifs du projet — 25 s

Nous poursuivons trois objectifs analytiques : découvrir des groupes homogènes, comparer trois familles d’algorithmes, puis mesurer la qualité, la couverture et les effectifs.

Les objectifs métier restent prudents : décrire les profils de dépenses, éviter d’interpréter les corrélations comme des causes et produire une segmentation exploitable uniquement après validation.

**Transition :** Ces objectifs sont organisés dans un workflow reproductible.

### Diapositive 6 — Démarche générale du projet — 25 s

Le workflow part de la source UCI, passe par la compréhension de la structure, l’EDA, le prétraitement, la segmentation et l’interprétation. Les données brutes restent intactes et les transformations sont exportées séparément.

La présentation se concentre sur les résultats réellement obtenus à chaque étape.

**Transition :** Regardons maintenant la matière première du projet.

### Diapositive 7 — Dataset : 440 clients, 8 variables — 25 s

Le dataset Wholesale Customers contient 440 clients et huit variables. Six variables représentent des dépenses annuelles : Fresh, Milk, Grocery, Frozen, Detergents_Paper et Delicassen. Channel et Region sont deux variables de contexte.

Le contrôle initial indique zéro valeur manquante. La source est le dépôt UCI Machine Learning Repository, dataset ID 292.

**Transition :** Les huit colonnes n’ont pas le même rôle dans les distances.

### Diapositive 8 — Description des variables — 25 s

Les six dépenses sont les features du clustering. Channel et Region sont codées en entiers, mais leur nature reste catégorielle. Une différence entre deux codes ne représente pas automatiquement une distance commerciale.

Nous excluons donc Channel et Region des distances, tout en les conservant pour une interprétation ultérieure.

**Transition :** Avant toute transformation, il faut vérifier la qualité des observations.

### Diapositive 9 — Qualité des données — 30 s

Les contrôles montrent zéro valeur manquante, zéro doublon exact et zéro dépense négative. Les six variables de dépenses ont été contrôlées.

La conséquence méthodologique est importante : nous pouvons comparer les méthodes sur les 440 observations sans imputation et sans suppression préalable.

**Transition :** La qualité est satisfaisante, mais les distributions peuvent encore influencer les distances.

### Diapositive 10 — Préparer — 10 s

Cette transition ouvre la partie consacrée à l’EDA, aux transformations et à la standardisation. L’objectif est de comprendre l’échelle des dépenses avant de construire les clusters.

**Transition :** Commençons par la forme des distributions.

### Diapositive 11 — EDA — distributions & asymétrie — 30 s

Les six dépenses sont étirées vers les grandes valeurs. Les coefficients de skewness sont positifs, avec notamment 2,561 pour Fresh, 5,908 pour Frozen et 11,152 pour Delicassen.

Cela signifie que quelques clients dépensent beaucoup plus que la majorité. Les moyennes sont donc sensibles à ces gros acheteurs. Cette observation motive l’étude d’une transformation log1p avant les distances.

**Transition :** L’asymétrie se traduit aussi par des valeurs signalées par la règle IQR.

### Diapositive 12 — EDA — outliers & boxplots — 25 s

La règle IQR signale 172 valeurs cumulées sur les six dépenses. Ce nombre représente des signalements par variable et pas nécessairement 172 clients distincts.

Ces valeurs peuvent correspondre à des clients importants. Nous ne les supprimons donc pas. Nous cherchons plutôt à réduire leur influence dans l’espace transformé.

**Transition :** Une autre information utile concerne les relations entre dépenses.

### Diapositive 13 — EDA — corrélations & relations — 30 s

La corrélation de Pearson la plus forte concerne Grocery et Detergents_Paper, avec r égal à 0,925. Cela indique une association linéaire forte dans cet échantillon.

Cette association suggère des comportements d’achat qui peuvent être liés entre catégories. Elle ne prouve cependant aucune causalité et ne remplace pas l’analyse des profils.

**Transition :** Nous pouvons maintenant préparer l’espace dans lequel les distances seront calculées.

### Diapositive 14 — Prétraitement — pourquoi transformer ? — 30 s

Trois stratégies sont comparées : StandardScaler seul, log1p puis StandardScaler, et log1p puis RobustScaler. log1p applique log(1+x), ce qui compresse les grandes dépenses. StandardScaler centre et réduit ; RobustScaler utilise la médiane et l’IQR.

La stratégie B, log1p plus StandardScaler, est retenue comme candidate principale parce qu’elle répond aux asymétries et aux différences d’échelle observées. Les résultats disponibles ne démontrent pas qu’elle est universellement optimale ; A et C restent des stratégies de sensibilité.

**Transition :** Nous passons maintenant aux méthodes de segmentation.

### Diapositive 15 — Segmenter — 15 s

Cette transition introduit les trois méthodes : K-Means, CAH Ward et DBSCAN. Elles utilisent les six dépenses préparées, tandis que Channel et Region restent hors des distances.

**Transition :** Hassan présente d’abord le fonctionnement de K-Means.

## Hassan El Hajjam — segmenter et décider

### Diapositive 16 — K-Means — principe — 40 s

K-Means cherche K centroïdes. Chaque client est affecté au centroïde le plus proche, puis les centroïdes sont recalculés à partir des affectations. Ces deux étapes se répètent jusqu’à convergence.

Dans notre expérience, l’initialisation utilise K-Means++, avec 20 initialisations et random_state égal à 42. L’objectif est de minimiser l’inertie intra-classe, c’est-à-dire la somme des distances au centroïde de chaque cluster.

La méthode est efficace et lisible, mais elle demande K à l’avance et préfère des groupes relativement compacts.

**Transition :** Il faut donc comparer plusieurs valeurs de K avant de choisir le modèle final.

### Diapositive 17 — K-Means — choisir K — 40 s

Nous testons K de 2 à 10. La courbe Elbow montre la baisse de l’inertie quand K augmente, mais cette baisse ne suffit pas à imposer un coude unique.

La silhouette complète l’analyse en comparant la cohésion d’un client dans son groupe et sa séparation avec le groupe voisin. K=2 donne la meilleure silhouette observée, 0,2903. Les effectifs restent raisonnables et l’interprétation est simple.

Le score 0,2903 correspond néanmoins à une séparation modeste : les groupes se distinguent, mais leurs frontières ne sont pas parfaitement nettes.

**Transition :** Nous retenons donc K=2 pour entraîner le modèle final.

### Diapositive 18 — K-Means — résultats & profils — 35 s

Le modèle final contient deux clusters. L’inertie vaut 1844,0641 et la silhouette vaut 0,2903 sur les 440 clients. Le cluster 0 regroupe 252 clients, soit 57,27 %, et le cluster 1 regroupe 188 clients, soit 42,73 %.

Les profils sont ensuite calculés dans les dépenses originales afin de conserver une interprétation commerciale compréhensible.

**Transition :** Nous utilisons ensuite la PCA uniquement pour représenter la structure en deux dimensions.

### Diapositive 19 — PCA — une projection visuelle — 25 s

La PCA projette les six dimensions préparées sur deux axes. Dans notre résultat, PC1 explique 44,08 % de la variance et PC2 27,19 %, soit 71,27 % cumulés.

Cette projection sert à visualiser approximativement les labels K-Means. Le modèle n’a pas été entraîné sur PC1 et PC2, mais sur les six variables préparées. Une projection 2D peut masquer une partie de la structure réelle.

**Transition :** La deuxième méthode construit une hiérarchie au lieu de choisir directement des centroïdes.

### Diapositive 20 — CAH — principe & méthode Ward — 40 s

La CAH commence avec un groupe par observation, puis fusionne progressivement les groupes proches. La méthode de Ward choisit les fusions qui augmentent le moins la variance intra-classe.

Le dendrogramme représente ces fusions. Sa hauteur indique la dissimilarité au moment de la fusion. Une coupe horizontale permet ensuite d’obtenir un nombre de groupes K.

**Transition :** Nous regardons la coupe et la performance obtenue pour les valeurs testées.

### Diapositive 21 — CAH Ward — dendrogramme & résultat — 35 s

Nous testons K de 2 à 6 avec linkage Ward. La meilleure silhouette observée est obtenue pour K=2, avec 0,2585 sur les 440 clients.

Les deux groupes contiennent 178 et 262 clients, soit 40,45 % et 59,55 %. La couverture est complète, mais la silhouette est inférieure à celle de K-Means.

**Transition :** La troisième méthode raisonne non plus par centroïdes ou hiérarchie, mais par densité locale.

### Diapositive 22 — DBSCAN — principe, eps & bruit — 30 s

DBSCAN utilise un rayon de voisinage eps et un nombre minimal de points min_samples. Un point cœur possède suffisamment de voisins dans son voisinage. Un point bord est proche d’une zone dense sans satisfaire lui-même le même critère. Un point isolé peut être classé comme bruit.

La méthode ne demande pas de fixer K à l’avance. Elle peut donc détecter des formes de densité, mais elle dépend fortement de l’échelle et du choix des paramètres.

**Transition :** Nous examinons la grille de paramètres testée et la configuration retenue.

### Diapositive 23 — DBSCAN — résultats expérimentaux — 40 s

La configuration retenue utilise eps égal à 0,80 et min_samples égal à 5. Elle produit 3 clusters, 230 observations en bruit et 210 observations regroupées.

La couverture est donc de 47,73 %. La silhouette hors bruit vaut 0,2885, calculée uniquement sur les 210 observations non bruitées. La forte proportion de bruit limite l’utilisation de cette configuration pour une segmentation globale, même si elle fournit une information sur la densité locale.

**Transition :** La comparaison doit donc tenir compte à la fois du score et de la couverture.

### Diapositive 24 — Décider — 15 s

Cette transition ouvre la dernière partie. Nous comparons maintenant les méthodes, puis nous revenons aux profils de dépenses et aux limites de l’étude.

**Transition :** La métrique seule ne suffit pas ; regardons aussi l’ensemble des observations évaluées.

### Diapositive 25 — Comparaison finale des méthodes — 45 s

K-Means et CAH couvrent les 440 clients. DBSCAN couvre 47,73 % et sa silhouette est calculée sur 210 observations non bruitées. Les trois silhouettes ne sont donc pas directement comparables comme si elles provenaient du même ensemble.

Parmi les configurations testées, K-Means fournit le meilleur compromis entre score sur l’ensemble complet, couverture et interprétabilité. Sa silhouette de 0,2903 reste modeste, donc cette conclusion doit rester prudente.

**Transition :** Nous interprétons enfin les profils dans les unités originales.

### Diapositive 26 — Interprétation business des profils — 50 s

Le profil 0 contient 252 clients. Dans les dépenses originales, il est relativement plus élevé pour Fresh et Frozen. Le profil 1 contient 188 clients et est relativement plus élevé pour Milk, Grocery, Detergents_Paper et Delicassen.

Les moyennes exactes montrent notamment Fresh à 13 973 pour le cluster 0, Milk à 10 346, Grocery à 14 697 et Detergents_Paper à 6 085 pour le cluster 1. Ces valeurs décrivent des comportements de dépenses ; elles ne prouvent ni rentabilité, ni fidélité, ni cause d’achat.

Les labels 0 et 1 sont propres à K-Means et ne doivent pas être alignés automatiquement avec ceux de la CAH ou de DBSCAN.

**Transition :** Nous pouvons maintenant formuler une conclusion proportionnée aux résultats.

### Diapositive 27 — Conclusion scientifique — 35 s

K-Means est retenu comme meilleur compromis parmi les configurations testées. Il offre une couverture complète, des profils faciles à lire et une silhouette légèrement supérieure à celle de la CAH sur les 440 clients.

La séparation reste modeste. DBSCAN apporte une lecture de la densité, mais sa proportion de bruit est trop élevée dans la configuration comparée pour une segmentation globale.

**Transition :** Ces résultats définissent aussi les limites et les prochaines étapes.

### Diapositive 28 — Limites & perspectives — 35 s

La séparation interne reste modeste et DBSCAN couvre moins de la moitié des clients. Un dataset de dépenses agrégées ne suffit pas à expliquer toute la valeur client, et les corrélations restent descriptives.

Les perspectives sont de tester la stabilité des partitions, de comparer systématiquement les trois prétraitements, d’enrichir l’interprétation par Channel et Region et de valider les profils avec des actions commerciales réelles. Ces travaux sont des perspectives, pas des expérimentations déjà réalisées.

**Transition :** Nous terminons par vos questions.

### Diapositive 29 — Merci pour votre attention — 20 s

Merci pour votre attention. Nous sommes prêts à répondre aux questions sur la sélection des variables, les transformations, le choix de K=2, la comparaison des silhouettes et le bruit observé avec DBSCAN.

