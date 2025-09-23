from utils.config import RAW, BRONZE
from utils.io import read_csv, write_parquet
from utils.schema import RENAME_WB_BRONZE, DTYPES_WB_BRONZE
from utils.transform import coerce_dtypes
from utils.checks import null_report, type_report

IN = RAW / "wb.csv"
OUT = BRONZE / "wb_bronze.parquet"
REQUIRED = ["country", "code", "indicator", "indicator_code", "year", "value"]

def run():
    df = read_csv(IN)
    
    # normalize headers via schema
    df = df.rename(columns=RENAME_WB_BRONZE)

    # identify year columns
    year_cols = [c for c in df.columns if c[:4].isdigit()]

    # wide -> long
    df = df.melt(
        id_vars=["country", "code", "indicator", "indicator_code"],
        value_vars=year_cols,
        var_name="year",
        value_name="value"
    )

    # extract numeric year
    df["year"] = df["year"].str[:4]

    # standardize
    df = coerce_dtypes(df, DTYPES_WB_BRONZE)
    df = df.reindex(columns=REQUIRED)

    # report 
    null_report(df)
    type_report(df, DTYPES_WB_BRONZE)
    print(df.head())

    # out
    write_parquet(df, OUT)


if __name__ == "__main__":
    run()