CREATE EXTERNAL TABLE IF NOT EXISTS names_in_books (
 year STRING,
 names STRING,
 freq BIGINT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
LOCATION 's3://wambia660fall2013/names_in_books/';     

INSERT OVERWRITE TABLE names_in_books
SELECT
year,
CASE WHEN 
(words[0] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
AND
words[1] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
)
THEN CONCAT(words[0],'-',words[1])
WHEN
(words[0] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
AND
words[2] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
)
THEN CONCAT(words[0],'-',words[2])
WHEN
(words[0] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
AND
words[3] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
)
THEN CONCAT(words[0],'-',words[3])
WHEN
(words[0] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
AND
words[4] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
)
THEN CONCAT(words[0],'-',words[4])
WHEN
(words[1] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
AND
words[2] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
)
THEN CONCAT(words[1],'-',words[2])
WHEN
(words[1] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
AND
words[3] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
)
THEN CONCAT(words[1],'-',words[3])
WHEN
(words[1] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
AND
words[4] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
)
THEN CONCAT(words[1],'-',words[4])
WHEN
(words[2] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
AND
words[3] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
)
THEN CONCAT(words[2],'-',words[3])
WHEN
(words[2] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
AND
words[4] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
)
THEN CONCAT(words[2],'-',words[4])
WHEN
(words[3] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
AND
words[4] IN ('john','william','robert','james','michael','mary','helen','dorothy','linda','lisa')
)
THEN CONCAT(words[3],'-',words[4])
END names,
freq
FROM
grams_in_books;