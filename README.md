# CO2 Emissions Project

This repository is a running project exploring global CO2 emissions, renewable energy, and related World Bank indicators.  It is actively under development — code, structure, and results will evolve as the analysis progresses.  

---

## Project Structure
```
co2-emissions/
├─ data/
│  ├─ raw/          # original OWID + WB CSVs
│  └─ processed/    # cleaned, analysis-ready versions
├─ notebooks/
│  ├─ owid_analysis.ipynb   # OWID dataset exploration
│  ├─ wb_analysis.ipynb     # World Bank dataset exploration
│  ├─ merged_analysis.ipynb # merged dataset (future)
│  └─ forecasting.ipynb     # forecasting experiments (future)
├─ src/
│  ├─ config.py     # central paths
│  └─ transform.py  # raw → processed cleaning pipeline
├─ reports/
│  └─ figures/      # saved plots/outputs
└─ README.md
```

---

## Current Progress
- Raw → processed pipeline (`transform.py`)  
- Initial OWID + WB notebooks created  
- Merged analysis and forecasting coming soon  

---

## How to Run
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
   python -m src.transform
   ```
   This produces cleaned CSVs in `data/processed/`.
4. Open the notebooks (start Jupyter from the repo root):
   ```bash
   jupyter notebook
   ```

---

## Notes
- This project is ongoing — notebooks and results may change as methods are refined.  
- Final deliverables will include merged datasets, visualizations, and forecasts.  

---

## Planned Features
- Expand cleaning pipeline with stronger type conversions (numeric coercion, handling missing values).  
- Dedicated `wb_analysis.ipynb` reshaping workflow (wide → long).  
- Merge OWID and WB datasets for joint exploration.  
- Enhanced exploratory data analysis (EDA) with time series plots and country comparisons.  
- Forecasting experiments with ARIMA, Prophet, or ML-based models.  
- Dashboards and polished visuals for reporting.  

---

### Acknowledgements
This project is being built with the help of [ChatGPT (OpenAI)](https://chat.openai.com), which has guided me through setting up the pipeline, notebooks, and project structure. This project serves as a practice for creating data pipelines, organizing projects, and making data digestible for non-academic audiences. I hope you enjoy!
