SELECT 
    c.name
FROM customers c
LEFT JOIN orders O 
    ON c.id=o.customer_id
WHERE customer_id IS NULL 


