# Guide de soutenance — ML2 Customer Segmentation

## 1. Organisation générale

- **Durée cible : 13 min 55 s**.
- **Saad Sahraoui : diapositives 1 à 15**, compréhension du contexte, dataset, qualité, EDA et prétraitement.
- **Hassan El Hajjam : diapositives 16 à 29**, algorithmes, évaluation, comparaison, profils et conclusion.
- Les diapositives 3, 10, 15 et 24 sont des transitions rapides.
- Le script détaillé se trouve dans [SCRIPT_SOUTENANCE.md](./SCRIPT_SOUTENANCE.md).

## 2. Plan complet des 29 diapositives

| N° | Titre exact | Intervenant | Durée |
|---:|---|---|---:|
| 1 | 2026/2027 / Machine Learning 2 · Projet académique | Saad | 20 s |
| 2 | Plan de la soutenance | Saad | 15 s |
| 3 | Comprendre | Saad | 15 s |
| 4 | Contexte métier & problématique | Saad | 30 s |
| 5 | Objectifs du projet | Saad | 25 s |
| 6 | Démarche générale du projet | Saad | 25 s |
| 7 | Dataset : 440 clients, 8 variables | Saad | 25 s |
| 8 | Description des variables | Saad | 25 s |
| 9 | Qualité des données | Saad | 30 s |
| 10 | Préparer | Saad | 10 s |
| 11 | EDA — distributions & asymétrie | Saad | 30 s |
| 12 | EDA — outliers & boxplots | Saad | 25 s |
| 13 | EDA — corrélations & relations | Saad | 30 s |
| 14 | Prétraitement — pourquoi transformer ? | Saad | 30 s |
| 15 | Segmenter | Saad | 15 s |
| 16 | K-Means — principe | Hassan | 40 s |
| 17 | K-Means — choisir K | Hassan | 40 s |
| 18 | K-Means — résultats & profils | Hassan | 35 s |
| 19 | PCA — une projection visuelle | Hassan | 25 s |
| 20 | CAH — principe & méthode Ward | Hassan | 40 s |
| 21 | CAH Ward — dendrogramme & résultat | Hassan | 35 s |
| 22 | DBSCAN — principe, eps & bruit | Hassan | 30 s |
| 23 | DBSCAN — résultats expérimentaux | Hassan | 40 s |
| 24 | Décider | Hassan | 15 s |
| 25 | Comparaison finale des méthodes | Hassan | 45 s |
| 26 | Interprétation business des profils | Hassan | 50 s |
| 27 | Conclusion scientifique | Hassan | 35 s |
| 28 | Limites & perspectives | Hassan | 35 s |
| 29 | Merci pour votre attention | Hassan | 20 s |

**Total : 835 secondes, soit 13 min 55 s.** Saad dispose de 5 min 50 s et Hassan de 8 min 05 s. La répartition suit les grandes parties du projet et ne coupe pas l’explication d’un algorithme.

## 3. Résultats scientifiques à mémoriser

| Élément | Valeur à retenir |
|---|---|
| Dataset | 440 clients, 8 variables, 6 dépenses et 2 catégories |
| Qualité | 0 valeur manquante, 0 doublon exact, 0 dépense négative |
| Asymétrie | Delicassen : skewness 11,152 |
| IQR | 172 signalements cumulés sur les six dépenses |
| Corrélation principale | Grocery / Detergents_Paper : r = 0,925 |
| Prétraitement principal | log1p + StandardScaler, candidate méthodologique |
| K-Means | K=2, inertie 1844,0641, silhouette 0,2903 |
| Effectifs K-Means | Cluster 0 : 252 ; cluster 1 : 188 |
| PCA | PC1 44,08 %, PC2 27,19 %, cumul 71,27 % |
| CAH Ward | K=2, silhouette 0,2585, effectifs 178 / 262 |
| DBSCAN | eps=0,80, min_samples=5, 3 clusters |
| DBSCAN | 230 bruit, 210 évalués, couverture 47,73 %, silhouette hors bruit 0,2885 |
| Conclusion | K-Means = meilleur compromis parmi les configurations testées, séparation modeste |

## 4. Conseils pour présenter les graphiques

- Toujours annoncer ce que montre le graphique avant de donner la conclusion.
- Pour l’EDA, distinguer clairement asymétrie, signalement IQR et erreur de mesure.
- Pour l’Elbow, rappeler que l’inertie baisse mécaniquement avec K et qu’elle ne suffit pas seule.
- Pour la silhouette, préciser si elle porte sur les 440 clients ou uniquement sur les 210 points non bruités de DBSCAN.
- Pour le dendrogramme, expliquer la hauteur de fusion et la coupe K=2 avant de citer 0,2585.
- Pour DBSCAN, annoncer les paramètres avant les résultats et toujours mentionner la couverture de 47,73 %.
- Pour les profils, revenir aux dépenses originales et ne jamais comparer directement les numéros de clusters entre méthodes.
- Ne pas présenter les applications commerciales comme une validation métier déjà réalisée.

## 5. Checklist avant la soutenance

- [ ] Ouvrir le fichier officiel et vérifier qu’il contient 29 diapositives.
- [ ] Tester le mode diaporama et les animations éventuelles.
- [ ] Vérifier que les logos, titres et pieds de page sont visibles.
- [ ] Répéter avec un chronomètre pour rester entre 12 et 15 minutes.
- [ ] Saad mémorise les transitions entre compréhension, EDA et prétraitement.
- [ ] Hassan mémorise les définitions de silhouette, inertie, Ward et DBSCAN.
- [ ] Préparer une réponse sur la non-comparabilité directe de la silhouette DBSCAN.
- [ ] Préparer une réponse sur les 172 signalements IQR et l’absence de suppression.
- [ ] Préparer une réponse sur la séparation modeste de K-Means.
- [ ] Préparer une réponse sur l’absence d’étude de stabilité réalisée.
- [ ] Vérifier que les notebooks et les résultats scientifiques restent inchangés.
- [ ] Garder une copie locale du PPTX officiel et du script.

