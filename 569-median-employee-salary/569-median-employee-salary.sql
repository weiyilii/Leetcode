# Write your MySQL query statement below
SELECT id, company, salary
FROM
(SELECT *, 
ROW_NUMBER() OVER (PARTITION BY COMPANY ORDER BY SALARY DESC, ID DESC) AS R_H,
ROW_NUMBER() OVER (PARTITION BY COMPANY ORDER BY SALARY ASC, ID ASC) AS R_L
FROM EMPLOYEE) T
WHERE R_H BETWEEN R_L - 1 AND R_L + 1