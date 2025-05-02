# CO₂ Emissions and Global Temperature Anomalies

This project investigates the relationship between global carbon dioxide (CO₂) emissions and global surface temperature anomalies using publicly available historical data.

## 🔍 Research Question

**How do CO₂ emissions correlate with global temperature anomalies over time?**

## 📊 Summary of Findings

- A strong positive correlation was found between global CO₂ emissions and temperature anomalies (r = 0.95).
- Linear regression analysis showed that CO₂ emissions significantly predicted temperature anomalies:
  - **b** = 0.00003, **t**(142) = 31.05, **p** < .001, **R²** = .87
- This supports the hypothesis that increasing greenhouse gas emissions contribute significantly to global warming.

## 📁 Project Structure

```
climate-emissions-temp-analysis/
│
├── data/
│   ├── owid-co2-data.csv              # CO₂ emissions dataset
│   └── GLB.Ts+dSST.csv                # NASA GISTEMP temperature anomalies
│
├── analysis/
│   └── emissions_temperature_analysis.ipynb  # Data cleaning, analysis, and modeling
│
├── output/
│   └── CO2_Emissions_and_Temperature_Anomalies_Report.pdf  # Final APA-style report
│
├── README.md
└── requirements.txt
```

## 🧰 Tools Used

- Python (Pandas, Matplotlib, Seaborn, Scikit-learn, Statsmodels)
- Jupyter Notebook
- Microsoft Word (for the APA-style report)

## 📦 Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the notebook in the `analysis/` folder

## 📚 Data Sources

- [NASA GISTEMP Surface Temperature Data](https://data.giss.nasa.gov/gistemp/)
- [Our World in Data – CO₂ and Greenhouse Gas Emissions](https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions)

## 📄 License

This project is for educational and demonstration purposes. Data sources remain under their original licenses.

---

Feel free to explore, adapt, or build upon this project. Contributions are welcome!
