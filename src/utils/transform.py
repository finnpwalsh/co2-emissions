import pandas as pd

def group_linear_interpolate(df: pd.DataFrame, group: str, cols: list[str]) -> pd.DataFrame:
    df = df.sort_values([group, "year"])
    for col in cols:
        if col in df.columns:
            df[col] = df.groupby(group)[col].transform(
                lambda s: s.interpolate(method="linear", limit_direction="both")
            )
    return df

def add_lags(df: pd.DataFrame, group: str, cols: list[str], lags: int = 1) -> pd.DataFrame:
    for col in cols:
        if col in df.columns:
            for k in range(1, lags + 1):
                df[f"{col}_lag{k}"] = df.groupby(group)[col].shift(k)
    return df

def within_demean(df: pd.DataFrame, group: str, cols: list[str]) -> pd.DataFrame:
    for col in cols:
        if col in df.columns:
            df[f"{col}_within"] = df[col] - df.groupby(group)[col].transform("mean")
    return df

def dropna_for(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    return df.dropna(subset=[c for c in cols if c in df.columns])

def coerce_dtypes(df, dtypes: dict, required: list[str] | None = None):
    """Coerce columns to project dtypes with safe numeric parsing."""
    if required:
        missing = [c for c in required if c not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

    for col, dt in dtypes.items():
        if col not in df.columns:
            continue
        if dt == "string":
            df[col] = df[col].astype("string").str.strip()
        elif dt == "Int64":  # nullable integer
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
        else:  # floats, etc.
            df[col] = pd.to_numeric(df[col], errors="coerce").astype(dt)
    return df