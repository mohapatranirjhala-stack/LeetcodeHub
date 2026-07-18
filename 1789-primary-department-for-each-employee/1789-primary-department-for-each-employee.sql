# Write your MySQL query statement below
-- Case 1: Employees belonging to multiple departments (select the one marked 'Y')
SELECT 
    employee_id, 
    department_id
FROM 
    Employee
WHERE 
    primary_flag = 'Y'

UNION

-- Case 2: Employees belonging to exactly one department
SELECT 
    employee_id, 
    department_id
FROM 
    Employee
GROUP BY 
    employee_id
HAVING 
    COUNT(department_id) = 1;