import pandas as pd
import numpy as np


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows."""
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicate rows.")
    return df


def handle_missing_values(df: pd.DataFrame, strategy: str = "drop") -> pd.DataFrame:
    """Handle missing values. Strategy: 'drop', 'mean', 'median', or 'mode'."""
    if strategy == "drop":
        return df.dropna()
    elif strategy == "mean":
        return df.fillna(df.mean(numeric_only=True))
    elif strategy == "median":
        return df.fillna(df.median(numeric_only=True))
    elif strategy == "mode":
        return df.fillna(df.mode().iloc[0])
    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def convert_dtypes(df: pd.DataFrame, column_types: dict) -> pd.DataFrame:
    """Convert column data types. Example: {'age': int, 'date': 'datetime64'}"""
    for col, dtype in column_types.items():
        if col in df.columns:
            df[col] = df[col].astype(dtype)
    return df


def rename_columns(df: pd.DataFrame, mapping: dict) -> pd.DataFrame:
    """Rename columns using a dictionary mapping."""
    return df.rename(columns=mapping)


def get_summary(df: pd.DataFrame) -> None:
    """Print a summary of the DataFrame."""
    print(f"Shape: {df.shape}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")
    print(f"\nDescriptive Stats:\n{df.describe()}")
