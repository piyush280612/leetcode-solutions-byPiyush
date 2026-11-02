# Write your MySQL query statement below
WITH FirstLogin AS (
    SELECT 
        player_id, 
        event_date AS first_date,
        RANK() OVER (PARTITION BY player_id ORDER BY event_date ASC) AS fl
    FROM Activity
)
SELECT 
    ROUND(
        COUNT(a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 
        2
    ) AS fraction
FROM FirstLogin f
JOIN Activity a 
    ON f.player_id = a.player_id 
   AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)
WHERE f.fl = 1;