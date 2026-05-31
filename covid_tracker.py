import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as ticker


df = pd.read_csv("owid-covid-data.csv")

data = df[[
    "location",
    "date",
    "total_cases",
    "total_deaths",
    "new_cases",
    "iso_code"
]]

data = data.dropna()

data = data[data["iso_code"].str.len() == 3]

latest_data = data.sort_values("date").groupby("location").tail(1)

top5 = latest_data.sort_values(
    by="total_cases",
    ascending=False
).head(5)

print("\nTop 5 Countries by Total Cases:\n")
print(top5[["location", "total_cases"]])

plt.figure(figsize=(10, 6))

plt.bar(
    top5["location"],
    top5["total_cases"]
)

plt.title("Top 5 Countries by COVID Cases")
plt.xlabel("Country")
plt.ylabel("Total Cases")

plt.ticklabel_format(style='plain', axis='y')
plt.gca().yaxis.set_major_formatter(
    ticker.StrMethodFormatter('{x:,.0f}')
)

plt.show()

country = input("\nEnter country name: ")

country_data = latest_data[
    latest_data["location"].str.lower() == country.lower()
]

if not country_data.empty:

    print("\nCOVID Statistics:\n")
    print(country_data[[
        "location",
        "total_cases",
        "total_deaths",
        "new_cases"
    ]])

    file_exists = os.path.isfile("filtered_data.csv")

    country_data.to_csv(
        "filtered_data.csv",
        mode="a",
        header=not file_exists,
        index=False
    )

    print("\nData appended to filtered_data.csv")

else:
    print("Country not found.")