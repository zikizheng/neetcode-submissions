CREATE TABLE USERS (
  ID INTEGER PRIMARY KEY,
  NAME TEXT
);
CREATE TABLE PRODUCTS (
  ID INTEGER PRIMARY KEY,
  NAME TEXT
);
CREATE TABLE ORDERS (
  ID INTEGER PRIMARY KEY,
  USER_ID INTEGER,
  PRODUCT_ID INTEGER,
  FOREIGN KEY (USER_ID) REFERENCES USERS(ID),
  FOREIGN KEY (PRODUCT_ID) REFERENCES PRODUCTS(ID)
);

















-- Do not modify below this line --
SELECT 
    c.table_name, 
    c.column_name, 
    c.data_type,
    ccu.table_name AS references_table,
    ccu.column_name AS references_column
FROM 
    information_schema.columns c
LEFT JOIN 
    information_schema.key_column_usage kcu
    ON c.table_name = kcu.table_name 
    AND c.column_name = kcu.column_name
LEFT JOIN 
    information_schema.table_constraints tc
    ON kcu.constraint_name = tc.constraint_name
    AND kcu.table_name = tc.table_name
    AND tc.constraint_type = 'FOREIGN KEY'
LEFT JOIN 
    information_schema.constraint_column_usage ccu 
    ON ccu.constraint_name = tc.constraint_name
WHERE 
    c.table_schema = 'public' AND
    c.table_name IN ('users', 'products', 'orders')
ORDER BY 
    c.table_name, c.column_name;
