# Write your MySQL query statement below
SELECT 
    id, 
    COUNT(*) AS num
FROM (
    -- Gather all IDs from the requester column
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    -- Combine with all IDs from the accepter column
    SELECT accepter_id AS id FROM RequestAccepted
) AS all_friends
GROUP BY 
    id
ORDER BY 
    num DESC
LIMIT 1;