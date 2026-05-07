-- Write your query below
SELECT name
FROM customers
WHERE id NOT IN (SELECT CUSTOMER_ID FROM ORDERS);