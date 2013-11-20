CREATE EXTERNAL TABLE IF NOT EXISTS ngrams (
 gram string,
 year int,
 occurrences bigint,
 pages bigint,
 books bigint
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS SEQUENCEFILE
LOCATION 's3://datasets.elasticmapreduce/ngrams/books/20090715/eng-us-all/1gram/';

CREATE EXTERNAL TABLE IF NOT EXISTS names1gram (
 year STRING,
 word STRING,
 freq BIGINT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
LOCATION 's3://wambia660fall2013/names1gram/';     

INSERT OVERWRITE TABLE names1gram
SELECT
year,
lower(gram) AS word,
occurrences
FROM
ngrams
WHERE
lower(gram)='john' OR
lower(gram)='william' OR
lower(gram)='robert' OR
lower(gram)='james' OR
lower(gram)='michael' OR
lower(gram)='mary' OR
lower(gram)='helen' OR
lower(gram)='dorothy' OR
lower(gram)='linda' OR
lower(gram)='lisa';

