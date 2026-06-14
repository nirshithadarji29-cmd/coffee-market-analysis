-- =========================================
-- Coffee Market Analysis Database Schema
-- =========================================

CREATE TABLE coffee_fact (
    Country_Code TEXT,
    Country_Name TEXT,
    Market_Year BIGINT,
    Attribute_Description TEXT,
    Value DOUBLE PRECISION
);

CREATE TABLE country_dim (
    iso2_code TEXT,
    iso3_code TEXT,
    country_name TEXT
);

CREATE TABLE dim_country (
    iso2_code TEXT,
    iso3_code TEXT,
    country_name TEXT
);

CREATE TABLE fact_coffee (
    country_name TEXT,
    country_code TEXT,
    market_year BIGINT,
    beginning_stocks DOUBLE PRECISION,
    domestic_consumption DOUBLE PRECISION,
    ending_stocks DOUBLE PRECISION,
    exports DOUBLE PRECISION,
    imports DOUBLE PRECISION,
    production DOUBLE PRECISION
);

CREATE TABLE fact_population (
    country_name TEXT,
    country_code TEXT,
    year BIGINT,
    population DOUBLE PRECISION
);

CREATE TABLE market_analysis (
    country_name TEXT,
    market_year BIGINT,
    coffee_consumption DOUBLE PRECISION,
    population DOUBLE PRECISION,
    consumption_per_capita DOUBLE PRECISION
);

CREATE TABLE market_score (
    country_name TEXT,
    avg_consumption DOUBLE PRECISION,
    avg_population DOUBLE PRECISION,
    avg_per_capita DOUBLE PRECISION,
    market_score DOUBLE PRECISION
);

CREATE TABLE population_fact (
    "Country Name" TEXT,
    "Country Code" TEXT,
    year BIGINT,
    population DOUBLE PRECISION
);

CREATE TABLE test_connection (
    id INTEGER,
    name VARCHAR(255)
);

CREATE VIEW vw_market_analysis AS
SELECT
    country_name,
    market_year,
    domestic_consumption,
    production,
    imports,
    exports,
    population,
    consumption_per_capita
FROM market_analysis;
