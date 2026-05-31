# COVID-19 Data Tracker using Python

A simple and interactive COVID-19 Data Tracker built using Python, Pandas, and Matplotlib.  
This project analyzes real-world COVID-19 data, visualizes the top affected countries, and allows users to search country-specific statistics with CSV export functionality.

---

# Features

- Load real-time COVID-19 dataset
- Filter and clean dataset using Pandas
- Display Top 5 countries by total COVID cases
- Generate bar chart visualization
- Format Y-axis labels for better readability
- Search country-wise COVID statistics
- Export searched data to CSV
- Append search history without overwriting previous data

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- CSV Handling
- File Handling (`os` module)

---

# Dataset Source

Dataset provided by:

[Our World in Data](https://ourworldindata.org/covid-cases)

Direct CSV Dataset:

[OWID COVID Dataset CSV](https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv)

---

# Project Structure

```text
covid-data-tracker/
│
├── covid_tracker.py
├── owid-covid-data.csv
├── filtered_data.csv
└── README.md
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/covid-data-tracker.git
```

```bash
cd covid-data-tracker
```

---

# Install Required Libraries

```bash
pip install pandas matplotlib
```

---

# How to Run

```bash
python covid_tracker.py
```

---

# Workflow

## 1. Load Dataset

The program reads the COVID dataset using Pandas.

```python
df = pd.read_csv("owid-covid-data.csv")
```

---

## 2. Data Cleaning

- Removes missing values
- Filters only valid countries using `iso_code`

```python
data=data.dropna()
data = data[data["iso_code"].str.len() == 3]
```

---

## 3. Latest Country Data

Extracts the latest COVID statistics for each country.

```python
latest_data = data.sort_values("date").groupby("location").tail(1)
```

---

## 4. Visualization

Displays a bar chart of the top 5 countries with the highest COVID cases.

---

## 5. Country Search

Users can search for a specific country to view:
- Total Cases
- Total Deaths
- New Cases

---

## 6. CSV Export

Searched country data is stored in:

```text
filtered_data.csv
```

The project uses append mode so previous searches remain saved.

---

# Example Output

## Top 5 Countries

```text
USA
India
France
Germany
Brazil
```

---

## Country Search

```text
Enter country name: India
```

Output:

```text
Location: India
Total Cases: 45,000,000
Total Deaths: 530,000
New Cases: 120
```
---

# Graph:
<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/88172182-784b-490c-8d8a-4e028efac3c2" />

# Graph Features
- Bar chart visualization
- Proper Y-axis number formatting
- Readable labels using commas

---

# Future Improvements

Possible enhancements:

- Interactive hover effects
- Streamlit dashboard
- Flask web application
- Multiple country comparison
- Pie charts and line charts
- Live API integration
- Dark mode dashboard
- Vaccination statistics

---

# Learning Outcomes

This project helped in understanding:

- Data analysis using Pandas
- Data visualization using Matplotlib
- File handling in Python
- CSV operations
- Real-world dataset processing

---

# License

This project is open-source and available for educational purposes.
