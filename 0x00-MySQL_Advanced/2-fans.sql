-- An SQL script that ranks country origins of bands ordered 
-- by the number of (non-unique) fans

SELECT orgin, SUM(fans) AS nb_fans FROM metal_bands
GROUP BY orgin ORDER BY nb_fans DESC;
