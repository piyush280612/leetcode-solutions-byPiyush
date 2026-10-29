# Write your MySQL query statement below
SELECT s.score,
DENSE_RANK() OVER (ORDER BY score DESC) as 'rank'
FROM Scores s
ORDER BY s.score DESC;