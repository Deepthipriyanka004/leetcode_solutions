SELECT email
FROM Person
GROUP BY 1
HAVING COUNT(*) > 1;