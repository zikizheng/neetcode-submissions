CREATE TABLE sports (
    id INTEGER PRIMARY KEY,
    name TEXT,
    total_viewers INTEGER
);

INSERT INTO sports (id, name, total_viewers) 
  VALUES (1, 'Football', 1000000),
          (2, 'Basketball', 2000000),
          (3, 'Tennis', 500000),
          (4, 'Baseball', 750000),
          (5, 'Golf', 250000);
-- Do not modify above this line. --

SELECT NAME, TOTAL_VIEWERS
FROM SPORTS
WHERE TOTAL_VIEWERS < (
  SELECT AVG(TOTAL_VIEWERS)
  FROM SPORTS
)
ORDER BY TOTAL_VIEWERS DESC
;