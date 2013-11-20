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

CREATE EXTERNAL TABLE IF NOT EXISTS alcohol_religion (
 year STRING,
 word STRING,
 freq BIGINT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
LOCATION 's3://wambia660fall2013/alcohol_religion/';     

INSERT OVERWRITE TABLE alcohol_religion
SELECT
year,
lower(gram) AS word,
occurrences
FROM
ngrams
WHERE
lower(gram)='alcohol' OR
lower(gram)='religion';

