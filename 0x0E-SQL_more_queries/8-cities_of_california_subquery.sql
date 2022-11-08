-- Lists all cities of California that can be found in the database `hbtn_0d_usa`
SELECT id, name
FROM cities
ORDER BY id
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name='california'
);
