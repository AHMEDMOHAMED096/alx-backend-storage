-- Create a new table to store the ranking
CREATE TABLE IF NOT EXISTS country_fan_ranking AS
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY
    origin
ORDER BY nb_fans DESC;

-- Select the results
SELECT * FROM country_fan_ranking;