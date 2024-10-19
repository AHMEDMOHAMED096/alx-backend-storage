-- Create a new table to store the results
CREATE TABLE IF NOT EXISTS glam_rock_bands AS
SELECT
    band_name,
    CASE
        WHEN split IS NULL THEN 2022 - formed
        ELSE split - formed
    END AS lifespan
FROM bands
WHERE
    main_style = 'Glam rock'
ORDER BY lifespan DESC;

-- Select the results
SELECT * FROM glam_rock_bands;