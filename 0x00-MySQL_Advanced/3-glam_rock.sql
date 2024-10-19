-- Create a new table to store the results
CREATE TABLE IF NOT EXISTS glam_rock_bands AS
SELECT band_name, COALESCE(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

-- Select the results
SELECT * FROM glam_rock_bands;