import pandas as pd
from pathlib import Path

RAW_DATA_DIR = Path(__file__).parent.parent / "data" / "raw"
PROCESSED_DATA_DIR = Path(__file__).parent.parent / "data" / "processed"


def load_raw_data(filename: str) -> pd.DataFrame:
    """Load a raw dataset file from the data/raw directory."""
    filepath = RAW_DATA_DIR / filename
    suffix = filepath.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(filepath)
    elif suffix in (".xlsx", ".xls"):
        return pd.read_excel(filepath)
    elif suffix == ".json":
        return pd.read_json(filepath)
    else:
        raise ValueError(f"Unsupported file format: {suffix}")


def load_processed_data(filename: str) -> pd.DataFrame:
    """Load a processed dataset file from the data/processed directory."""
    filepath = PROCESSED_DATA_DIR / filename
    return pd.read_csv(filepath)


def save_processed_data(df: pd.DataFrame, filename: str) -> None:
    """Save a DataFrame to the data/processed directory."""
    filepath = PROCESSED_DATA_DIR / filename
    df.to_csv(filepath, index=False)
    print(f"Saved to {filepath}")
