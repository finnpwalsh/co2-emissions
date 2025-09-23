import pandas as pd

def null_report(df: pd.DataFrame, top: int = 12) -> None:
    # prints top columns by null count
    s = df.isna().sum().sort_values(ascending=False)
    print("\n[NULL REPORT]")
    print(s.head(top))

def expect_columns(df: pd.DataFrame, expected: list[str]) -> None:
    missing = [c for c in expected if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

def expect_unique_key(df: pd.DataFrame, cols: list[str], name: str = "key") -> None:
    dup = df.duplicated(subset=cols).sum()
    if dup:
        raise ValueError(f"{dup} duplicate {name} rows for {cols}")

def expect_shape_at_least(df: pd.DataFrame, min_rows: int, min_cols: int) -> None:
    r, c = df.shape
    if r < min_rows or c < min_cols:
        raise ValueError(f"Shape too small: {df.shape}, expected ≥({min_rows},{min_cols})")
    
def type_report(df, expected=None):
    print("\n[TYPE REPORT]")
    for col, dtype in df.dtypes.items():
        line = f"{col} {dtype}"
        if expected and col in expected and str(dtype) != expected[col]:
            line += f"  (expected {expected[col]})"
        print(line)
