# Segmentation intelligente des clients d'un distributeur en gros

Projet académique de Machine Learning 2 pour les étudiants ingénieurs de l'ENSAM Rabat.

## Objectif

Découvrir et interpréter des groupes de clients selon leurs dépenses annuelles, puis comparer K-Means, la classification ascendante hiérarchique (CAH) et DBSCAN avec des métriques adaptées.

## Données

Le projet utilise le jeu de données **Wholesale Customers** du UCI Machine Learning Repository (ID 292). Le fichier original est conservé à la racine du projet. Une copie intacte destinée au projet se trouve dans `data/raw/`.

## Étapes prévues

1. Initialiser le projet et vérifier la structure du dataset.
2. Réaliser l'analyse exploratoire et préparer les variables.
3. Appliquer et comparer K-Means, CAH et DBSCAN.
4. Interpréter les segments et produire les visualisations et tableaux de résultats.

L'étape 1 est la seule traitée pour le moment. Aucun prétraitement, aucune EDA et aucun algorithme de clustering n'est exécuté dans cette étape.

## Vérification du dataset

Depuis la racine du projet, après activation de l'environnement virtuel :

```powershell
python src/check_dataset.py
```
