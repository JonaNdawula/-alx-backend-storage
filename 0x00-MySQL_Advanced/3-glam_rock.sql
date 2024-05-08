-- An SQL Script that lists all bands with Glam rock
-- as their main style, ranked by their longevity

SELECT band_name, (2022 - formed - IFNULL(split, 2022)) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
