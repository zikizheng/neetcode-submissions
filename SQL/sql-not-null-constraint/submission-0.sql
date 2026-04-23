CREATE TABLE PRODUCTS(
  NAME TEXT NOT NULL DEFAULT 'Unknown',
  PRICE INTEGER NOT NULL,
  QUANTITY INTEGER DEFAULT 0
);






-- Do not modify below this line --
SELECT column_name, data_type, is_nullable, column_default
FROM information_schema.columns
WHERE table_name = 'products';
