# Questions et réponses — soutenance ML2 Customer Segmentation

## Dataset et objectifs

### 1. Pourquoi avoir choisi ce dataset ? *(Slides 4 et 7)*

Le dataset UCI Wholesale Customers contient 440 clients, six catégories de dépenses et deux variables de contexte. Il est suffisamment concret pour étudier la préparation des données, les distances et l’interprétation de clusters, sans fournir de labels prédéfinis.

### 2. Pourquoi utiliser un apprentissage non supervisé ? *(Slide 4)*

Aucune classe cible ne décrit à l’avance le type de client. Les algorithmes recherchent donc des groupes de clients qui se ressemblent selon les six dépenses sélectionnées.

### 3. Pourquoi ne pas utiliser Channel et Region dans les distances ? *(Slide 8)*

Ces colonnes sont stockées comme entiers, mais elles représentent des catégories. La distance entre les codes 1 et 2 n’a pas nécessairement un sens quantitatif. Les inclure créerait une fausse métrique.

### 4. Pourquoi conserver Channel et Region ? *(Slides 8 et 28)*

Elles peuvent aider à décrire la composition des clusters après l’entraînement. Elles restent toutefois des variables d’interprétation et ne deviennent pas des preuves causales.

## Analyse exploratoire

### 5. Que signifie une skewness positive élevée ? *(Slide 11)*

Elle indique une distribution étirée vers les grandes valeurs. Delicassen présente une skewness de 11,152, ce qui signifie que quelques clients ont des dépenses très supérieures à la majorité.

### 6. Pourquoi la moyenne peut-elle être trompeuse ici ? *(Slide 11)*

Les très grandes dépenses tirent la moyenne vers le haut. La médiane est souvent plus représentative du client central lorsque la distribution est fortement asymétrique.

### 7. Que représentent les 172 signalements IQR ? *(Slide 12)*

Il s’agit du cumul des valeurs signalées par la règle IQR sur les six variables. Ce nombre ne représente pas nécessairement 172 clients distincts. Nous n’avons supprimé aucune observation.

### 8. Que signifie la corrélation Grocery–Detergents_Paper de 0,925 ? *(Slide 13)*

Elle indique une forte association linéaire dans l’échantillon. Elle ne démontre pas qu’une dépense cause l’autre et ne suffit pas à construire une stratégie commerciale.

## Prétraitement

### 9. Pourquoi appliquer log1p ? *(Slide 14)*

log1p applique log(1+x). La transformation compresse les grandes valeurs, réduit l’effet des longues queues positives et accepte les dépenses égales à zéro.

### 10. Quelle différence entre StandardScaler et RobustScaler ? *(Slide 14)*

StandardScaler utilise la moyenne et l’écart-type pour centrer et réduire. RobustScaler utilise la médiane et l’IQR, ce qui le rend moins sensible aux extrêmes.

### 11. Pourquoi retenir log1p + StandardScaler ? *(Slide 14)*

Cette stratégie répond directement aux deux constats de l’EDA : asymétrie forte et amplitudes différentes. Elle est retenue comme candidate principale, mais le projet ne démontre pas qu’elle est optimale sans comparaison complète des performances de clustering pour chaque prétraitement.

### 12. Avez-vous supprimé les valeurs extrêmes ? *(Slides 12 et 14)*

Non. Les 172 signalements IQR cumulés ont été conservés. La transformation vise à limiter leur influence dans l’espace des distances.

## K-Means

### 13. Comment fonctionne K-Means ? *(Slide 16)*

L’algorithme initialise K centroïdes, affecte chaque observation au centroïde le plus proche, recalcule les centroïdes, puis répète ces étapes jusqu’à convergence.

### 14. Pourquoi utiliser K-Means++ et n_init=20 ? *(Slide 16)*

K-Means++ améliore l’initialisation des centroïdes. `n_init=20` lance plusieurs initialisations, tandis que `random_state=42` rend l’expérience reproductible.

### 15. Que mesure l’inertie ? *(Slides 16 et 17)*

L’inertie est la somme des distances au carré entre chaque client et le centroïde de son cluster. Elle diminue mécaniquement lorsque K augmente, donc elle doit être interprétée avec d’autres critères.

### 16. Pourquoi K=2 ? *(Slide 17)*

K=2 obtient la meilleure silhouette parmi les K testés de 2 à 10, avec des effectifs de 252 et 188 clients. Le choix est aussi lisible. Il reste dépendant de l’espace préparé et des configurations étudiées.

### 17. Comment interpréter la silhouette de 0,2903 ? *(Slides 17 et 18)*

Elle indique une séparation modeste. Les clients sont davantage proches de leur groupe que du groupe voisin, mais les groupes se recouvrent encore partiellement. Ce n’est pas une séparation parfaite.

## CAH et Ward

### 18. Comment fonctionne la CAH agglomérative ? *(Slide 20)*

Chaque observation commence seule. La méthode fusionne progressivement les groupes proches jusqu’à former une hiérarchie complète. Une coupe du dendrogramme donne ensuite le nombre de clusters choisi.

### 19. Pourquoi utiliser Ward ? *(Slide 20)*

Ward choisit la fusion qui augmente le moins la variance intra-classe. Cette logique est cohérente avec la recherche de groupes relativement compacts dans l’espace préparé.

### 20. Comment justifier K=2 avec le dendrogramme ? *(Slides 20 et 21)*

La coupe K=2 se situe entre les deux dernières hauteurs de fusion, environ 24,45 et 35,23. La recherche de K=2 à 6 donne aussi la meilleure silhouette pour K=2, soit 0,2585.

## DBSCAN

### 21. Que signifient eps et min_samples ? *(Slide 22)*

`eps` définit le rayon du voisinage. `min_samples` fixe le nombre minimal de points dans ce voisinage, point central inclus, pour qualifier un point de cœur.

### 22. Quelle différence entre point cœur, point bord et bruit ? *(Slide 22)*

Un point cœur possède suffisamment de voisins dans son voisinage. Un point bord est proche d’une zone dense sans satisfaire nécessairement le seuil de densité. Un point bruit n’est relié à aucune zone dense selon les paramètres choisis.

### 23. Pourquoi DBSCAN produit-il 230 points de bruit ? *(Slide 23)*

Avec eps=0,80 et min_samples=5, beaucoup d’observations ne satisfont pas la densité locale demandée. La couverture tombe à 47,73 %, ce qui limite l’usage de cette configuration comme segmentation globale.

## Évaluation et comparaison

### 24. Pourquoi les silhouettes ne sont-elles pas directement comparables ? *(Slide 25)*

K-Means et CAH sont évalués sur les 440 observations. DBSCAN est évalué hors bruit, sur 210 observations seulement. Les ensembles évalués sont donc différents.

### 25. Pourquoi ne pas retenir DBSCAN malgré une silhouette hors bruit de 0,2885 ? *(Slides 23 et 25)*

La valeur 0,2885 est proche de K-Means, mais elle exclut 230 observations. Une silhouette calculée sur un sous-ensemble ne suffit pas à justifier une segmentation globale lorsque la couverture est de 47,73 %.

### 26. Pourquoi K-Means est-il retenu ? *(Slides 18, 21, 25 et 27)*

Il fournit une couverture de 100 %, une silhouette de 0,2903 sur les 440 clients, des effectifs raisonnables et des profils faciles à expliquer. Il représente le meilleur compromis parmi les configurations testées, sans constituer une vérité universelle.

## Interprétation métier, limites et perspectives

### 27. Que peut-on dire des deux profils K-Means ? *(Slide 26)*

Le profil 0 regroupe 252 clients et présente relativement plus de Fresh et Frozen. Le profil 1 regroupe 188 clients et présente relativement plus de Milk, Grocery, Detergents_Paper et Delicassen. Il s’agit de profils de dépenses, pas de catégories métier validées.

### 28. Peut-on déduire la rentabilité ou la fidélité des clients ? *(Slides 26 et 28)*

Non. Le dataset contient des dépenses agrégées, pas les marges, la fréquence de commande, la fidélité ou les coûts logistiques. Une validation métier et des variables supplémentaires seraient nécessaires.

### 29. Une étude de stabilité a-t-elle été réalisée ? *(Slide 28)*

Non. Le projet utilise `random_state=42` pour la reproductibilité, mais ne réalise pas encore une étude de stabilité par ré-échantillonnage ou répétition sur plusieurs partitions. Cette analyse reste une perspective.

### 30. Quelles sont les prochaines améliorations prioritaires ? *(Slide 28)*

Tester la stabilité, comparer systématiquement les trois prétraitements, enrichir l’interprétation avec Channel et Region et valider les profils auprès d’utilisateurs métier. Il serait aussi utile d’ajouter des variables temporelles ou économiques si elles sont disponibles.

