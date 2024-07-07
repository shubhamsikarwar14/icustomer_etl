-- 1. Total number of interactions per day
SELECT DATE(timestamp) AS interaction_date, COUNT(*) AS total_interactions
FROM user_interactions
GROUP BY DATE(timestamp)
ORDER BY interaction_date;

-- 2. Top 5 users by the number of interactions
SELECT user_id, COUNT(*) AS interaction_count
FROM user_interactions
GROUP BY user_id
ORDER BY interaction_count DESC
LIMIT 5;

-- 3. Most interacted products based on the number of interactions
SELECT product_id, COUNT(*) AS interaction_count
FROM user_interactions
GROUP BY product_id
ORDER BY interaction_count DESC
LIMIT 5;
