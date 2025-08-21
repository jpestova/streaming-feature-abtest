-- DAU по группам
SELECT
    ab_group,
    DATE(timestamp) AS event_date,
    COUNT(DISTINCT user_id) AS dau
FROM events
GROUP BY ab_group, DATE(timestamp);

-- Конверсия в подписку
SELECT
    ab_group,
    COUNT(DISTINCT CASE WHEN subscribed = 1 THEN user_id END) * 1.0 / COUNT(DISTINCT user_id) AS conversion_rate
FROM events
GROUP BY ab_group;

-- Дельта конверсии
WITH conversion AS (
    SELECT
        ab_group,
        COUNT(DISTINCT CASE WHEN subscribed = 1 THEN user_id END) * 1.0 / COUNT(DISTINCT user_id) AS conversion_rate
    FROM events
    GROUP BY ab_group
)
SELECT
    MAX(conversion_rate) - MIN(conversion_rate) AS delta_conversion
FROM conversion;
