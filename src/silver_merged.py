import pandas as pd
from utils.io import read_parquet, write_parquet
from utils.config import SILVER, GOLD
from utils.schema import CANON, DTYPES
from utils.checks import null_report, type_report

IN_WB = SILVER / "wb_silver.parquet"
IN_OWID = SILVER / "owid_silver.parquet"
OUT = GOLD / "co2.parquet"
REQUIRED = ["country", "year", "co2_pc_t", "ren_share_pct", "population", "population_growth", "urban_growth"]

def run():
    # read
    wb = read_parquet(IN_WB)
    owid = read_parquet(IN_OWID)

    # merge
    df = pd.merge(owid, wb,
                  on=["country", "year"],
                  how="left"
    )

    # impute
    # TODO
    
    
    # report
    null_report(df)
    type_report(df, DTYPES)
    print(df.head())

    # write
    # write_parquet(df, OUT)


if __name__ in "__main__":
    run()