from utils.config import BRONZE, SILVER
from utils.io import read_parquet, write_parquet
from utils.schema import RENAME_WB, DTYPES
from utils.transform import coerce_dtypes
from utils.checks import null_report, type_report


IN = BRONZE / "wb_bronze.parquet"
OUT = SILVER / "wb_silver.parquet"

REQUIRED = ["country", "year", "ren_share_pct", "population_growth", "population", "urban_growth"]

def run():
    df = read_parquet(IN)

    # control for duplicates
    df = (
        df.sort_values(["country", "year", "indicator_code"])
          .drop_duplicates(["country", "year", "indicator_code"], keep="last")
    )

    # pivot
    df = df.pivot_table(
        index=["country", "year"],
        columns="indicator_code",
        values="value",
        aggfunc="last"
    ).reset_index()
    
    df.columns.name = None # removes "indicator code" label above headers

    # standardize 
    df = df.rename(columns=RENAME_WB)
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