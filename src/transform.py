# --------------------------------------------------------------
# libraries
# --------------------------------------------------------------

from pathlib import Path
import pandas as pd
from .config import RAW_DIR, PROC_DIR

# --------------------------------------------------------------
# file paths
# --------------------------------------------------------------

# input
OWID_RAW = RAW_DIR / "owid.csv"
WB_RAW = RAW_DIR / "wb.csv"

# output
OWID_OUT = PROC_DIR / "owid_transformed.csv"
WB_OUT = PROC_DIR / "wb_transformed.csv"

# --------------------------------------------------------------
# transformation functions
# --------------------------------------------------------------

# create data cleaner
def _clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    # create empty column list
    clean_cols = []
    
    # clean columns
    for name in df.columns:
        name = name.strip() # remove " " from beginning or end
        name = name.lower() # to lowercase
        name = name.replace(" ", "_")
        name = name.replace("-", "_")
        clean_cols.append(name)
    
    # replace column names
    df.columns = clean_cols

    # return
    return df


# pipeline function
def process_file(in_path: Path, out_path: Path) -> Path:
    
    df = pd.read_csv(in_path)# read
    df = _clean_columns(df)# process

    # create out file
    df.to_csv(out_path, index=False)

    # return path
    return out_path # note: not strictly necessary


# --------------------------------------------------------------
# main
# --------------------------------------------------------------

if __name__ in "__main__":
    process_file(OWID_RAW, OWID_OUT)
    process_file(WB_RAW, WB_OUT)