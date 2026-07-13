WITH info AS (
SELECT fragrance.id, name, site_name, price, scraped_at
FROM fragrance
LEFT JOIN price_history
ON fragrance.id = price_history.fragrance_id)

SELECT info.id, name, info.site_name, price, scraped_at, url
FROM info
LEFT JOIN fragrance_link
ON info.id = fragrance_link.fragrance_id
AND info.site_name = fragrance_link.site_name
ORDER BY site_name, scraped_at DESC