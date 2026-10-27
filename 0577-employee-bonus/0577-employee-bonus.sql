# Write your MySQL query statement below
SELECT e.name, b.bonus 
FROM Employee e
LEFT JOIN Bonus b on b.empID = e.empID
WHERE b.bonus IS NULL OR b.bonus < 1000;