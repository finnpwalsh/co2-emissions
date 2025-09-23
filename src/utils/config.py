from pathlib import Path

# Root folders
DATA    = Path("data")
RAW     = DATA / "raw"
BRONZE  = DATA / "bronze"
SILVER  = DATA / "silver"
GOLD    = DATA / "gold"
REPORTS = Path("reports")
FIGS    = REPORTS / "figures"

for p in (RAW, BRONZE, SILVER, GOLD, REPORTS, FIGS):
    p.mkdir(parents=True, exist_ok=True)

# Project-wide defaults
NA_VALUES = ["", " ", "NA", "NaN", "nan", ".."]
YEAR_MIN, YEAR_MAX = 2000, 2024
