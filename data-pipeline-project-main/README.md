# COVID-19 ETL Data Pipeline Project

This project is to build a basic **ETL (Extract, Transform, Load)** pipeline built with Python. It retrieves **real-time COVID-19 data** from [Our World in Data](https://ourworldindata.org/coronavirus-source-data), processes and transforms key indicators, and generates a cleaned dataset ready for analysis or visualization.

---

## Inspiration

As the COVID-19 pandemic continues to influence global health and policy, having access to reliable and clean data is essential for:

- Public health analysis
- Government decision-making
- Academic research
- Data science and machine learning projects

This project helps demonstrate how raw data can be fetched, cleaned, and prepared for downstream applications.

---

## Working of Pipeline

### Extract  
Downloads the latest worldwide COVID-19 data in CSV format from a trusted open-source GitHub repository.

### Transform  
Filters and cleans the dataset to include:

- `location` (country/region)
- `total_cases`
- `total_deaths`
- `population`
- Derived metric: `cases_per_million`

Removes rows with missing values for consistent analysis.

### Load  
Saves the cleaned and enriched dataset as `transformed_covid_data.csv` and prints the first few rows for inspection.

---

## Files

- `etl_covid.py` – The core ETL script
- `requirements.txt` – Python dependencies
- `README.md` – Project documentation

---

## How to Run

 Install required Python packages:

   ```bash
   pip install -r requirements.txt

