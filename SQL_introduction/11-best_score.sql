-- Select records from second_table with score >= 10, ordered in descending order of score.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
