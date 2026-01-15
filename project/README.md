# Wind Resource Analysis – Programming for Data Analytics Project

This folder contains my final project for the **Programming for Data Analytics** module.

The goal of the project is to analyse **wind speed data in Ireland** using
historic hourly observations from Met Éireann, and to explore how suitable
different locations might be for **wind energy (wind farms)**.

---

## Contents

- `wind_resource_ireland.ipynb`  
  Main project notebook.  
  This notebook:
  - loads hourly wind speed data from one or more Met Éireann weather stations  
  - cleans and prepares the data (parsing dates, handling missing values)  
  - calculates daily and monthly statistics for wind speed  
  - explores the distribution of wind speeds at each site  
  - uses simple models to estimate potential wind power output  
  - creates a range of plots to visualise patterns over time and by season

- `data/`  
  Folder for data files used in the analysis.
  - `data/raw/` – original CSV files downloaded from Met Éireann  
  - `data/processed/` – optional cleaned / aggregated data exported from the notebook  

(If a file or folder is not present yet, it will be created as the project develops.)

---

## How to Run the Project

From the root of the repository (where the top-level README is):

1. Change into the `project` folder:

        cd project

2. (Recommended) Create and activate a virtual environment (optional but good practice).

3. Install required Python packages:

        pip install pandas numpy matplotlib jupyter scikit-learn

4. Start Jupyter Notebook:

        jupyter notebook

5. In the Jupyter interface, open:

        wind_resource_ireland.ipynb

6. Run the cells from top to bottom.

The notebook is designed to be **self-contained**: it will explain which data
files it expects to find under `data/` and how they are used in the analysis.

---

## Techniques Used

The project uses tools and techniques from the module, including:

- **pandas** for:
  - reading CSV files
  - cleaning and transforming data
  - resampling time series (hourly → daily → monthly)
- **numpy** for basic numeric calculations
- **matplotlib** for visualisation
- **scikit-learn** for simple modelling (e.g. trend analysis with linear regression)

---

## Research & Data Sources

- Met Éireann climate data (hourly wind speed and related variables)  
  Documentation and data access: Met Éireann’s official climate data pages.
- Introductory resources on wind energy and turbine power curves  
  (used to build a simple model of potential wind power output).

A short list of links and a description of how they were used is included
at the end of the main notebook.