# Coffee Market Analysis Dashboard

An interactive dashboard designed to support coffee market expansion decisions through data-driven insights. Built using Python, PostgreSQL, Streamlit, and Plotly.

## Live Demo

https://coffee-market-analysis-c7uo9heitb3w738euvwfuu.streamlit.app/

## Features

* Interactive dashboard for market analysis
* KPI tracking and performance monitoring
* Data visualizations using Plotly
* PostgreSQL database integration
* Streamlit-based web application

## Tech Stack

* Python
* Streamlit
* Pandas
* Plotly
* SQLAlchemy
* PostgreSQL (Neon)

## Project Objective

Analyze coffee market data and identify potential opportunities for business expansion through interactive visualizations and key performance indicators.

## Repository Structure

```text
Dashboard/
│
├── app.py

sql/
├── schema.sql
├── transformation_queries.sql
├── database_output.sql

requirements.txt
README.md
```

## Database Components

### Schema

* `schema.sql` contains the database schema definitions.
* Includes dimension, fact, and analytical tables used throughout the project.

### SQL Transformations

* `transformation_queries.sql` contains the SQL logic used to:

  * Build analytical views
  * Calculate consumption per capita
  * Generate market scores
  * Rank countries based on market potential

### Database Output

* `database_output.sql` contains sample output from the final analytical tables used by the dashboard.

## ETL Pipeline

The ETL pipeline performs the following steps:

1. Extract coffee market and population datasets.
2. Clean and standardize country information.
3. Load dimension and fact tables into PostgreSQL (Neon).
4. Execute SQL transformations to generate analytical views and market scoring tables.
5. Surface insights through an interactive Streamlit dashboard.

## How to Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database Connection

Update the database connection string using environment variables:

```python
DATABASE_URL = os.environ["DATABASE_URL"]
```

### Run Streamlit Application

```bash
streamlit run app.py
```

## Key Insights

* Brazil and the United States rank among the highest opportunity markets based on overall market score.
* Population size alone does not determine attractiveness; consumption per capita plays a significant role.
* Combining market size, population, and consumption metrics provides a more balanced expansion strategy.

## Reflection

### Approach

I designed the solution using a dimensional data model with fact and dimension tables to support scalable analysis and reporting.

### Challenges

* Integrating coffee market data with population data across multiple country code standards.
* Creating a consistent country mapping between datasets.
* Building a scoring methodology that balances market size, population, and consumption behavior.

### Learnings

* Improved experience in designing ETL pipelines using Python and PostgreSQL.
* Strengthened SQL skills through analytical transformations and view creation.
* Gained hands-on experience deploying analytical applications using Streamlit Cloud.

## Dashboard

The dashboard provides an interactive interface for exploring coffee market opportunities and comparing countries using KPI-driven analysis.
