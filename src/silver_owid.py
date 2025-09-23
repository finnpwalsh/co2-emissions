from utils.config import BRONZE, SILVER, YEAR_MAX, YEAR_MIN
from utils.io import read_parquet, write_parquet
from utils.schema import RENAME_OWID, DTYPES
from utils.transform import coerce_dtypes
from utils.checks import null_report, type_report

IN = BRONZE / "owid_bronze.parquet"
OUT = SILVER / "owid_silver.parquet"
REQUIRED = ["country", "year", "co2_pc_t"]

def run():
    df = read_parquet(IN)
    
    # deduplicate
    df = df.drop_duplicates()
    
    # standardize
    df = df.rename(columns=RENAME_OWID)
    df = coerce_dtypes(df, DTYPES, required=REQUIRED)
    df = df.reindex(columns=REQUIRED)

    # filter for years
    df = df[(df["year"] >= YEAR_MIN) & (df["year"] <= YEAR_MAX)]
    
    # report
    null_report(df)
    type_report(df, DTYPES)
    print(df.head())
    
    # write
    write_parquet(df, OUT)


if __name__ == "__main__":
    run()
