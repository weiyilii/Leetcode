/* 
 Please write a DELETE statement and DO NOT write a SELECT statement.
 Write your T-SQL query statement below
 */
DELETE PERSON 
WHERE ID IN
(SELECT T.ID FROM
(SELECT ID, ROW_NUMBER() OVER (PARTITION BY EMAIL ORDER BY ID ASC) NUM FROM PERSON) T
WHERE T.NUM > 1)