# Write your MySQL query statement below
SELECT PLAYER_ID player_id, MIN(EVENT_DATE) first_login
FROM ACTIVITY
GROUP BY PLAYER_ID