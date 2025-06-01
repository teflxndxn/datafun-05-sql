-- Aggregation: count, avg, sum per category
SELECT
    category,
    COUNT(*) AS product_count,
    AVG(price) AS avg_price,
    SUM(stock) AS total_stock
FROM product_features
GROUP BY category;
