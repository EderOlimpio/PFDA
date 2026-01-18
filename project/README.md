# Wind Resource Analysis – Programming for Data Analytics Project

This folder contains my final project for the **Programming for Data Analytics** module.

The goal of the project is to analyse **wind resources in Ireland** using historic
hourly windspeed observations from **Met Éireann**, and to explore how suitable a
site like Knock Airport might be for **wind energy (wind farms)**.

---

## Contents

- `wind_resource_ireland.ipynb`  
  Main project notebook. It is organised into the following sections:

  1. **Introduction and Data Sources** – describes the aim of the project and the
     Met Éireann data used (hourly observations from Knock Airport, station 4935).
  2. **Imports and Settings** – imports Python libraries and sets up plotting
     style and display options.
  3. **Data Loading and Cleaning** – loads the `hly4935.csv` file from the Met
     Éireann climate data service, skips metadata rows, parses the date column,
     sets a datetime index and converts the windspeed column (`wdsp`) to numeric.
  4. **Exploratory Analysis (Wind Speed Patterns)** – creates daily and monthly
     aggregates, plots:
     - hourly and daily mean windspeed,
     - monthly mean windspeed,
     - the distribution of hourly windspeed (histogram and KDE),
     - seasonal patterns (average windspeed by month of year and by hour of day).
  5. **Simple Wind Power Estimation** – converts windspeed from knots to m/s and
     applies a simple idealised **turbine power curve** (cut-in, rated and
     cut-out speeds) to estimate a **normalised power output** between 0 and 1.
     A rough **capacity factor** is computed by averaging this normalised power.
  6. **Trend Analysis / Modelling** – aggregates monthly mean windspeed, then
     uses **`LinearRegression` from scikit-learn** to fit a straight-line trend
     over time and visualises the fitted trend together with the data.
  7. **Conclusions** – summarises the main findings about wind patterns, power
     potential and long-term trends at Knock.
  8. **Research Notes and References** – briefly documents external resources
     used (Met Éireann data documentation, turbine power curve references and
     library documentation).

- `data/`  
  Folder for data files used in the analysis:
  - `data/raw/` – original CSV files downloaded from Met Éireann (optional, the
    notebook can also read directly from the URL).
  - `data/processed/` – optional cleaned / aggregated data exported from the
    notebook.

(If these folders do not exist yet, they can be created as the project develops.)

---

## How to Run the Project

From the **root of this repository** (where the top-level README lives):

1. Change into the project folder:

        cd project

2. (Optional but recommended) Create and activate a virtual environment.

3. Install the required Python packages:

        pip install pandas numpy matplotlib jupyter scikit-learn

4. Start Jupyter Notebook:

        jupyter notebook

5. In the Jupyter interface, open:

        wind_resource_ireland.ipynb

6. Run all cells from top to bottom.  
   The notebook will:
   - download or load the Knock Airport hourly dataset,
   - build daily and monthly aggregates,
   - produce exploratory plots,
   - estimate simple turbine power output,
   - and fit a linear trend model to monthly mean windspeed.

---

## Techniques and Libraries Used

The project uses tools and techniques covered in the module:

- **pandas**
  - reading CSV files,
  - cleaning and transforming data,
  - resampling time series (hourly → daily → monthly),
  - grouping by month and hour of day.
- **NumPy**
  - numerical operations,
  - implementing the simple turbine power curve.
- **Matplotlib**
  - time series plots (hourly, daily, monthly),
  - histograms and density plots,
  - line plots for seasonal profiles and trends.
- **scikit-learn**
  - `LinearRegression` to model a simple linear trend in monthly mean windspeed.

---

## Research Notes

A short description of external resources is recorded in the notebook itself
(Section 8), including:

- **Met Éireann climate data** documentation and access pages – used as the
  source for the Knock Airport hourly dataset (`hly4935.csv`).
- Introductory material on **wind turbine power curves** – used to design the
  simple cut-in / rated / cut-out model implemented in the code.
- Official documentation for **pandas**, **NumPy**, **Matplotlib** and
  **scikit-learn** – used for function references and examples of best practice.

All analysis code in this project was written specifically for this module.