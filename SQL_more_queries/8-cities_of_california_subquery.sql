-- Lists all the cities of california.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "california") ORDER BY id;
