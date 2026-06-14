-- =========================================
-- Coffee Market Analysis Transformations
-- =========================================

-- Create Dimension Table

CREATE TABLE IF NOT EXISTS dim_country (
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    country_code VARCHAR(20)
);

-- Create Coffee Fact Table

CREATE TABLE IF NOT EXISTS fact_coffee (
    coffee_id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    country_code VARCHAR(20),
    market_year INTEGER,
    attribute_description VARCHAR(255),
    value NUMERIC
);

-- =========================================
-- Market Analysis View
-- =========================================

DROP VIEW IF EXISTS vw_market_analysis;

CREATE VIEW vw_market_analysis AS

SELECT
    c.country_name,
    c.market_year,
    c.domestic_consumption,
    c.production,
    c.imports,
    c.exports,
    p.population,

    CASE
        WHEN p.population > 0
        THEN c.domestic_consumption * 1000.0 / p.population
        ELSE NULL
    END AS consumption_per_capita

FROM fact_coffee c

INNER JOIN dim_country d
    ON c.country_code = d.iso2_code

INNER JOIN fact_population p
    ON d.iso3_code = p.country_code
    AND c.market_year = p.year;

-- =========================================
-- Market Scoring Model
-- =========================================

DROP TABLE IF EXISTS market_score;

CREATE TABLE market_score AS

WITH base AS (
    SELECT
        country_name,
        AVG(domestic_consumption) AS avg_consumption,
        AVG(population) AS avg_population,
        AVG(consumption_per_capita) AS avg_per_capita
    FROM vw_market_analysis
    GROUP BY country_name
),

scored AS (
    SELECT
        *,
        avg_consumption /
            MAX(avg_consumption) OVER() AS consumption_score,

        avg_population /
            MAX(avg_population) OVER() AS population_score,

        avg_per_capita /
            MAX(avg_per_capita) OVER() AS per_capita_score
    FROM base
)

SELECT
    country_name,
    avg_consumption,
    avg_population,
    avg_per_capita,

    (
        consumption_score * 0.4 +
        population_score * 0.3 +
        per_capita_score * 0.3
    ) AS market_score

FROM scored;
