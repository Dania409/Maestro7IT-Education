import requests
import pandas as pd

# Extract
def extract_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"
    response = requests.get(url)
    with open("covid_data.csv", "wb") as f:
        f.write(response.content)
    print("Data extracted successfully.")

# Transform
def transform_data():
    df = pd.read_csv("covid_data.csv")
    df = df[["location", "total_cases", "total_deaths", "population"]]
    df = df.dropna()
    df["cases_per_million"] = (df["total_cases"] / df["population"]) * 1_000_000
    df.to_csv("transformed_covid_data.csv", index=False)
    print("Data transformed successfully.")

# Load
def load_data():
    df = pd.read_csv("transformed_covid_data.csv")
    print("Sample data loaded:")
    print(df.head())

if __name__ == "__main__":
    extract_data()
    transform_data()
    load_data()
