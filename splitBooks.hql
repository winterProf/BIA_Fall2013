CREATE TABLE IF NOT EXISTS grams_in_books (
 year STRING,
 words Array<string>,
 freq BIGINT
);

INSERT OVERWRITE TABLE grams_in_books
SELECT
year,
SPLIT(LOWER(gram),',') as words,
occurrences as freq
FROM 
ngrams;