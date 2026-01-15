# Programming for Data Analytics – Weekly Assignments

This repository contains my weekly assignments for the **Programming for Data Analytics** module.

The work is mainly in **Python** and **Jupyter Notebooks**, and covers topics like:
- basic Python scripting
- working with CSV data
- data cleaning and transformation with **pandas**
- simple visualisation with **matplotlib**
- basic descriptive statistics

---

## Repository Structure

Current key files:

- `assignment02-bankholdiays.py`  
  Northern Ireland bank holidays program (Python script).

- `assignment03-pie.ipynb`  
  Email domain analysis and pie chart (Jupyter Notebook).

- `assignment05-population.ipynb`  
  Population by sex, age and region in Ireland (Jupyter Notebook).

- `assignment_6_Weather.ipynb`  
  Knock Airport weather analysis (Jupyter Notebook).

You can open the notebooks directly in **Jupyter**, **VS Code**, or **PyCharm Professional**.

---

## How to Run the Code

### 1. Clone the repository

From a terminal:

    git clone <your-repo-url>.git
    cd <your-repo-folder>

### 2. Recommended Python environment

- Python 3.9+ (or similar)
- Install dependencies:

    pip install pandas numpy matplotlib jupyter

### 3. Running the Python script

For **Assignment 02**:

    python assignment02-bankholdiays.py

This prints:
- all bank holidays in Northern Ireland for a given year (hard-coded in the script),
- the subset of holidays that are **unique to Northern Ireland** (do not occur elsewhere in the UK).

### 4. Running the notebooks

From the repo folder:

    jupyter notebook

Then open any of:

- `assignment03-pie.ipynb`
- `assignment05-population.ipynb`
- `assignment_6_Weather.ipynb`

and run the cells in order.

---

## Assignment Summaries

### Assignment 02 – Northern Ireland Bank Holidays (`assignment02-bankholdiays.py`)

- Defines a list of **Northern Ireland bank holidays** for a specific year.
- Prints all holidays with their dates.
- Compares them with bank holidays in **England & Wales** and **Scotland**.
- Prints only the holidays that are **unique to Northern Ireland**  
  (e.g. St Patrick’s Day, Battle of the Boyne).

---

### Assignment 03 – Email Domain Pie Chart (`assignment03-pie.ipynb`)

- Loads a CSV of 1000 people from a given URL.
- Extracts the **email domain** (e.g. `gmail.com`, `yahoo.com`) from each email address.
- Counts how many people use each domain.
- Builds a **pie chart** of the most common domains, grouping all smaller ones into an **"Other"** slice.
- Focuses on:
  - basic data wrangling with `pandas`
  - a clear, readable pie chart with `matplotlib`.

---

### Assignment 05 – Population by Sex, Age and Region (`assignment05-population.ipynb`)

Uses CSO census data (FY006A) to analyse population by age, sex and Irish administrative county.

**Part 1**

- Cleans the data so **single years of age** run from 0–100.
- Aggregates population by **sex** (Male/Female) and age for **Ireland as a whole**.
- Calculates the **weighted mean age** for each sex.
- Computes and visualises the **difference between the sexes by age** (Female − Male).

**Part 2**

- Defines a **target age** (e.g. 35) and an age band of ±5 years.
- Computes the total male and female population in that band.
- Calculates the **population difference** between the sexes in that band.

**Part 3**

- For the same age band, aggregates population by **region (administrative county)** and sex.
- Finds the county with the **largest absolute difference** between female and male population.
- Visualises the differences across regions.

---

### Assignment 06 – Knock Airport Weather (`assignment_6_Weather.ipynb`)

Uses hourly climate data from **Knock Airport (station 4935)**.

**Part A – Temperature**

- Loads the hourly data and parses the time column as a proper datetime index.
- Plots:
  - **Hourly temperature**
  - **Daily mean temperature**
  - **Monthly mean temperature**
- Shows how aggregation (hourly → daily → monthly) smooths the series and highlights trends.

**Part B – Wind**

- Works with the `wdsp` column (hourly mean windspeed, with some missing data).
- Plots:
  - **Hourly windspeed** (gaps show missing values)
  - **24-hour rolling mean windspeed**
  - **Daily maximum windspeed**
  - **Monthly mean of the daily maximum windspeeds**
- Demonstrates how to combine rolling windows and resampling:
  - hourly → daily max → monthly mean of daily max.

---

## Tools & Libraries

- **Python**
- **pandas** – data loading, cleaning, and resampling
- **numpy** – numeric calculations (e.g. weighted means)
- **matplotlib** – plotting
- **Jupyter Notebook** – interactive analysis

---

## Notes

- The code is written for teaching/learning purposes and mirrors the style and techniques used in the course lectures.
- Data is loaded directly from external URLs where possible, so an internet connection may be required to re-run everything from scratch.
