DATA-LOADING-AND-EXPLORATION
import pandas as pd

df = pd.read_csv("owid-covid-data.csv")

df.head()

df.columns

df.isnull().sum()

DATA-CLEANING
countries = ["Kenya", "India", "United States"]
df = df[df["location"].isin(countries)]

df["date"] = pd.to_datetime(df["date"])

df = df.dropna(subset=["total_cases", "total_deaths", "total_vaccinations"])

df = df.fillna(method="ffill")


EXPLORATORY-DATA-ANALYSIS
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df["location"] == country]
    plt.plot(country_data["date"], country_data["total_cases"], label=country)

plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True)
plt.show()


VACCINATION-PROGRESS
plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df["location"] == country]
    plt.plot(country_data["date"], country_data["total_vaccinations"], label=country)

plt.title("COVID-19 Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.grid(True)
plt.show()


CHOROPLETH-MAP
import plotly.express as px


latest_df = df[df["date"] == df["date"].max()]

fig = px.choropleth(latest_df,
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    title="Global COVID-19 Cases (Latest)",
                    color_continuous_scale="Reds")

fig.show()
