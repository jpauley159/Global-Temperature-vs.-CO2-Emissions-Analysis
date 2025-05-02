# Multivariate Climate Analysis: CO₂ and Global Temperature Anomalies

This project explores the relationship between greenhouse gas emissions and global temperature anomalies using historical climate data. It includes both simple and multivariate regression analyses to understand how different emissions contribute to global warming.

## 🔍 Research Questions

1. How do CO₂ emissions correlate with global temperature anomalies over time?
2. Can methane, nitrous oxide, and land use change CO₂ further explain global temperature changes in a multivariate context?

## 📊 Summary of Findings

- **Simple Linear Regression:** A strong positive correlation was found between CO₂ emissions and global temperature anomalies (r = 0.95).
- **Multivariate Regression:** A model including CO₂, methane, nitrous oxide, and land use change CO₂ explained 88% of the variance in temperature anomalies (**R² = .88**). Among these, only CO₂ was a statistically significant predictor (**p < .001**).

## 📁 Project Structure

```
climate-emissions-analysis/
│
├── data/
│   ├── owid-co2-data.csv
│   └── GLB.Ts+dSST.csv
│
├── analysis/
│   ├── emissions_temperature_analysis.ipynb  # Includes cleaning, modeling, and visualization
│
├── output/
│   ├── CO2_Emissions_and_Temperature_Anomalies_Report.docx
│   └── Multivariate_CO2_Emissions_Report.docx
│
├── README.md
└── requirements.txt
```

## 🧰 Tools Used

- **Python** (Pandas, Matplotlib, Seaborn, Statsmodels, Scikit-learn)
- **Jupyter Notebook**
- **Microsoft Word** (APA-style reporting)

## 📦 Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Open the notebook in the `analysis/` folder to explore the data and models

## 📚 Data Sources

- [NASA GISTEMP Surface Temperature Data](https://data.giss.nasa.gov/gistemp/)
- [Our World in Data – CO₂ and Greenhouse Gas Emissions](https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions)

## 📄 License

This project is for educational and demonstration purposes. Data sources are subject to their original licenses.

---

Feel free to fork, modify, and build on this project. Contributions and feedback are welcome!
