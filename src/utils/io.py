import pandas as pd
from pathlib import Path
from .config import NA_VALUES
from .log import info

def read_csv(path: Path, **kw) -> pd.DataFrame:
    return pd.read_csv(path, na_values=NA_VALUES, low_memory=False, **kw)

def read_parquet(path: Path, **kw) -> pd.DataFrame:
    return pd.read_parquet(path, **kw)

def write_parquet(df: pd.DataFrame, path: Path, **kw) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False, **kw)
    info(f"parquet→ {path} shape={df.shape}")

def write_csv(df: pd.DataFrame, path: Path, **kw) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, **kw)
    info(f"csv→ {path} shape={df.shape}")

def write_dual(df: pd.DataFrame, base_path: Path, **kw) -> None:
    """Write both .parquet and .csv with same basename."""
    write_parquet(df, base_path.with_suffix(".parquet"), **kw)
    write_csv(df, base_path.with_suffix(".csv"))