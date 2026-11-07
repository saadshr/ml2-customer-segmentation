"""Vérifie la structure du dataset Wholesale Customers sans le modifier."""

from pathlib import Path

import pandas as pd


EXPECTED_COLUMNS = [
    "Channel",
    "Region",
    "Fresh",
    "Milk",
    "Grocery",
    "Frozen",
    "Detergents_Paper",
    "Delicassen",
]
EXPECTED_SPENDING_COLUMNS = [
    "Fresh",
    "Milk",
    "Grocery",
    "Frozen",
    "Detergents_Paper",
    "Delicassen",
]


def main() -> None:
    """Charge le CSV et affiche les contrôles de qualité demandés."""
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "data" / "raw" / "Wholesale customers data.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Fichier CSV introuvable : {csv_path}")

    data = pd.read_csv(csv_path)

    print("=== Vérification du dataset Wholesale Customers ===")
    print(f"Fichier : {csv_path}")
    print(f"Dimension : {data.shape[0]} lignes x {data.shape[1]} colonnes")
    print("\nColonnes et types :")
    print(data.dtypes.to_string())
    print("\nCinq premières lignes :")
    print(data.head().to_string(index=False))
    print("\nValeurs manquantes par colonne :")
    print(data.isna().sum().to_string())
    print(f"\nLignes dupliquées : {data.duplicated().sum()}")

    actual_columns = list(data.columns)
    missing_columns = [column for column in EXPECTED_COLUMNS if column not in actual_columns]
    unexpected_columns = [column for column in actual_columns if column not in EXPECTED_COLUMNS]
    missing_spending = [
        column for column in EXPECTED_SPENDING_COLUMNS if column not in actual_columns
    ]

    print("\n=== Contrôles d'anomalies ===")
    anomalies = []
    if data.shape != (440, 8):
        anomalies.append(
            f"dimension différente de (440, 8) : {data.shape[0], data.shape[1]}"
        )
    if missing_columns:
        anomalies.append(f"colonnes attendues absentes : {missing_columns}")
    if unexpected_columns:
        anomalies.append(f"colonnes inattendues : {unexpected_columns}")
    if missing_spending:
        anomalies.append(f"colonnes de dépenses absentes : {missing_spending}")
    if data.isna().any().any():
        anomalies.append("au moins une valeur manquante est présente")
    if data.duplicated().any():
        anomalies.append("au moins une ligne dupliquée est présente")

    if anomalies:
        print("ANOMALIES DÉTECTÉES :")
        for anomaly in anomalies:
            print(f"- {anomaly}")
    else:
        print("Aucune anomalie détectée pour les contrôles de l'étape 1.")

    print("\nVérification des six colonnes de dépenses :")
    for column in EXPECTED_SPENDING_COLUMNS:
        status = "présente" if column in actual_columns else "ABSENTE"
        print(f"- {column}: {status}")


if __name__ == "__main__":
    main()
