# Write your MySQL query statement below
SELECT 
    id,
    CASE
        -- If ID is odd, grab the next student's name. If no next student exists, keep the current name.
        WHEN MOD(id, 2) = 1 THEN COALESCE(LEAD(student) OVER(ORDER BY id), student)
        -- If ID is even, grab the previous student's name.
        ELSE LAG(student) OVER(ORDER BY id)
    END AS student
FROM 
    Seat;