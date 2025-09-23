CANON = {
    "country": "country",
    "year": "year",
    "co2_pc_t": "co2_pc_t",                         # tonnes per person
    "ren_share_pct": "ren_share_pct",               # % of final energy
    "population": "population",
    "population_growth": "population_growth",
    "urban_growth": "urban_growth",
}

DTYPES = {
    "country": "string",
    "year": "Int64",
    "co2_pc_t": "float64",
    "ren_share_pct": "float64",
    "population": "float64",
    "population_growth": "float64",
    "urban_growth": "float64",
}

# Our World in Data
RENAME_OWID = {
    "Entity": "country",
    "Year": "year",
    "Annual CO₂ emissions (per capita)": "co2_pc_t",   # per-capita (tonnes)
}

# World Bank
RENAME_WB = {
    "country": "country",
    "year": "year",
    # energy consumption (final energy basis)
    "EG.FEC.RNEW.ZS": "ren_share_pct",
    # population
    "SP.POP.GROW": "population_growth",
    "SP.POP.TOTL": "population",
    "SP.URB.GROW": "urban_growth",
}

# helper, WB Bronze
RENAME_WB_BRONZE = {
    "Country Name" : "country",
    "Country Code" : "code",
    "Series Name" : "indicator",
    "Series Code" : "indicator_code",
}

# helper, WB Bronze
DTYPES_WB_BRONZE = {
    "country" : "string",
    "code" : "string",
    "indicator" : "string",
    "year" : "Int64",
    "value" : "float64",
}