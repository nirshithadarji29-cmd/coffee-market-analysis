-- =========================================
-- Database Output Samples
-- Coffee Market Analysis
-- =========================================

-- Top 20 countries by market score

SELECT *
FROM market_score
ORDER BY market_score DESC
LIMIT 20;

/*
Sample Output

Brazil         | 12816.32 | 149701232.58 | 0.08501329 | 0.44960421
United States  | 8564.28  | 260178746.55 | 0.02735010 | 0.35236143
Australia      | 1646.52  | 53166.74     | 31.60654912| 0.35140560
India          | 962.95   | 920345540.00 | 0.00111480 | 0.33006456
Algeria        | 2084.35  | 86723.43     | 24.06668044| 0.29351498
*/

-- Market Analysis View

SELECT *
FROM vw_market_analysis
LIMIT 20;
