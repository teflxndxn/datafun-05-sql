-- Join product_features with orders table (assumes orders table exists)
SELECT
    pf.product_id,
    pf.category,
    o.order_id,
    o.quantity
FROM product_features pf
INNER JOIN orders o ON pf.product_id = o.product_id;
