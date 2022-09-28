# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE FROM PERSON
WHERE ID NOT IN (
SELECT * FROM (
SELECT MIN(ID) FROM PERSON GROUP BY EMAIL
) AS P
)