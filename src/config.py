from pathlib import Path

# create project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROC_DIR = DATA_DIR / "processed"