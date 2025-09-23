# CO2 Emissions Project

This repository is a running project exploring global CO2 emissions, renewable energy, and related World Bank indicators.  It is actively under development; code, structure, and results will evolve as the analysis progresses.  

---

## Project Structure
```
co2-emissions/
├─ data/
│  ├─ raw/           # original OWID + WB CSVs
│  ├─ bronze/        # extracted
│  ├─ silver/        # transformed
│  └─ gold/          # analysis-ready
├─ notebooks/
│  ├─ owid_analysis.ipynb   # OWID dataset exploration
│  ├─ wb_analysis.ipynb     # World Bank dataset exploration
│  ├─ merged_analysis.ipynb # merged dataset (future)
│  └─ forecasting.ipynb     # forecasting experiments (future)
├─ src/
│  ├─ utils/
│  │  ├─ __init__.py
│  │  ├─ checks.py
│  │  ├─ config.py
│  │  ├─ io.py
│  │  ├─ log.py
│  │  ├─ schema.py
│  │  └─ transform.py
│  ├─ bronze_owid.py
│  ├─ bronze_wb.py
│  ├─ silver_owid.py
│  ├─ silver_wb.py
│  ├─ silver_merged.py
│  └─ gold_co2.py    # prepare data for analysis
├─ reports/
│  └─ figures/      # saved plots/outputs
├─ requirements.txt
└─ README.md
```

---

## Variables
**UNDER CONSTRUCTION**

---

## Current Progress
- Raw → Bronze → Silver → Gold pipeline
   - Current culmination: `silver_merged.py`
- Initial OWID, WB, Merged, and Forecast notebooks created  
- Merged analysis and forecasting coming soon  

---

## How to Run
**UNDER CONSTRUCTION**
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/co2-emissions.git
   cd co2-emissions
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the transformation pipeline:
   ```bash
   **UNDER CONSTRUCTION**
   ```

4. Open the notebooks (start Jupyter from the repo root):
   ```bash
   jupyter notebook
   ```

---

## Notes
- This project is ongoing; notebooks and results may change as methods are refined.  
- Final deliverables will include merged datasets, visualizations, and forecasts.  

---

## Planned Features
- Impute missing values in `silver_merged.ipynb`.
- Implement `gold_co2.ipynb1`. 
- Enhanced exploratory data analysis (EDA) with time series plots and country comparisons.  
- Forecasting experiments with ARIMA, Prophet, or ML-based models.  
- Dashboards and polished visuals for reporting.  

---

### Acknowledgements
This project is being built with the help of [ChatGPT (OpenAI)](https://chat.openai.com), which has guided me through setting up the pipeline, notebooks, and project structure. This project serves as a practice for creating data pipelines, organizing projects, and making data digestible for non-academic audiences. I hope you enjoy!
