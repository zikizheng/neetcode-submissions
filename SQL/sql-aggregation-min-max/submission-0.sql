CREATE TABLE scores (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    score INTEGER,
    region TEXT
);

INSERT INTO scores (score, region) VALUES
    (60, 'EU'),
    (88, 'EU'),
    (75, 'NA'),
    (95, 'NA'),
    (60, 'AS'),
    (75, 'EU'),
    (45, 'NA'),
    (100, 'EU');
-- Do not modify above this line. --

SELECT MIN(SCORE) AS MIN_SCORE, MAX(SCORE) AS MAX_SCORE, ROUND(AVG(SCORE)) AS AVG_SCORE
FROM SCORES
WHERE REGION = 'EU'