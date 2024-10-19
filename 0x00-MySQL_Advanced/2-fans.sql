-- Create a new table to store the ranking
CREATE TABLE IF NOT EXISTS band_origins_ranked AS
SELECT origin, SUM(nb_fans) AS total_fans
FROM bands
GROUP BY
    origin
ORDER BY total_fans DESC;