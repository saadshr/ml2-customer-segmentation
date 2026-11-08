"""Fonctions réutilisables pour préparer les dépenses du dataset Wholesale Customers."""

from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler, StandardScaler


SPENDING_COLUMNS = [
    "Fresh",
    "Milk",
    "Grocery",
    "Frozen",
    "Detergents_Paper",
    "Delicassen",
]


def build_preprocessing_strategies(
    data: pd.DataFrame,
) -> Tuple[Dict[str, pd.DataFrame], Dict[str, object]]:
    """Construit les trois versions demandées et retourne aussi les transformateurs."""
    features = data[SPENDING_COLUMNS].copy()

    standard_scaler = StandardScaler()
    standard = standard_scaler.fit_transform(features)

    logged_features = np.log1p(features)
    log_standard_scaler = StandardScaler()
    log_standard = log_standard_scaler.fit_transform(logged_features)

    log_robust_scaler = RobustScaler()
    log_robust = log_robust_scaler.fit_transform(logged_features)

    matrices = {
        "standard_scaled": pd.DataFrame(standard, columns=SPENDING_COLUMNS, index=data.index),
        "log_standard_scaled": pd.DataFrame(
            log_standard, columns=SPENDING_COLUMNS, index=data.index
        ),
        "log_robust_scaled": pd.DataFrame(
            log_robust, columns=SPENDING_COLUMNS, index=data.index
        ),
    }
    transformers = {
        "standard_scaler": standard_scaler,
        "log_standard_scaler": log_standard_scaler,
        "log_robust_scaler": log_robust_scaler,
    }
    return matrices, transformers


def save_preprocessed_matrices(
    matrices: Dict[str, pd.DataFrame], output_dir: Path
) -> Dict[str, Path]:
    """Sauvegarde les matrices préparées avec des noms de fichiers explicites."""
    output_dir.mkdir(parents=True, exist_ok=True)
    filenames = {
        "standard_scaled": "customers_standard_scaled.csv",
        "log_standard_scaled": "customers_log_standard_scaled.csv",
        "log_robust_scaled": "customers_log_robust_scaled.csv",
    }
    saved_paths = {}
    for name, filename in filenames.items():
        path = output_dir / filename
        matrices[name].to_csv(path, index=True, index_label="customer_index")
        saved_paths[name] = path
    return saved_paths
