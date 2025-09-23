from utils.config import RAW, BRONZE
from utils.io import read_csv, write_parquet
from utils.schema import RENAME_OWID, DTYPES
from utils.transform import coerce_dtypes
from utils.checks import null_report, type_report

IN = RAW / "owid.csv"
OUT = BRONZE / "owid_bronze.parquet"
REQUIRED = ["country", "year", "co2_pc_t"]

def run():
    df = read_csv(IN)
    
    # standardize
    df = df.rename(columns=RENAME_OWID)
    df = coerce_dtypes(df, DTYPES, required=REQUIRED)
    df = df.reindex(columns=REQUIRED)
    
    # report
    null_report(df)
    type_report(df, DTYPES)
    print(df.head())
    
    # write
    write_parquet(df, OUT)


if __name__ == "__main__":
    run()
