-- Lists all cities of California found in the db
SELECT id, name
FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = "California") ORDER BY id;
