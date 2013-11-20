INSERT OVERWRITE TABLE alcohol_religion
SELECT
year,
lower(gram),
occurrences
FROM
english_1grams
WHERE
lower(gram)='alcohol' OR
lower(gram)='religion';