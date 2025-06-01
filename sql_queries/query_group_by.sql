-- Group products by category and get average rating
SELECT
    category,
    AVG(rating) AS avg_rating
FROM product_features
GROUP BY category;
