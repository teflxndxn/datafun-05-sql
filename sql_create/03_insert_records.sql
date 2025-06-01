-- Insert categories
INSERT INTO categories (category_id, category_name) VALUES (1, 'Electronics');
INSERT INTO categories (category_id, category_name) VALUES (2, 'Clothing');
INSERT INTO categories (category_id, category_name) VALUES (3, 'Books');

-- Insert products
INSERT INTO products (product_id, product_name, price, quantity, category_id) VALUES (101, 'Smartphone', 699.99, 50, 1);
INSERT INTO products (product_id, product_name, price, quantity, category_id) VALUES (102, 'Laptop', 999.99, 30, 1);
INSERT INTO products (product_id, product_name, price, quantity, category_id) VALUES (103, 'T-Shirt', 19.99, 100, 2);
INSERT INTO products (product_id, product_name, price, quantity, category_id) VALUES (104, 'Jeans', 49.99, 60, 2);
INSERT INTO products (product_id, product_name, price, quantity, category_id) VALUES (105, 'Novel', 14.99, 80, 3);
INSERT INTO products (product_id, product_name, price, quantity, category_id) VALUES (106, 'Textbook', 89.99, 40, 3);
INSERT INTO products (product_id, product_name, price, quantity, category_id) VALUES (107, 'Headphones', 129.99, 70, 1);
INSERT INTO products (product_id, product_name, price, quantity, category_id) VALUES (108, 'Sweater', 39.99, 45, 2);
INSERT INTO products (product_id, product_name, price, quantity, category_id) VALUES (109, 'Notebook', 5.99, 120, 3);
INSERT INTO products (product_id, product_name, price, quantity, category_id) VALUES (110, 'Monitor', 199.99, 25, 1);
