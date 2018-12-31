# Logs Analysis

This project simulates a real-world tasks while working for a fictional news site and sets up a prefilled mock PostgreSQL database to query using a secret wizardry called sql and python with psycopg2. 

This project is an internal reporting tool that answers these questions: 
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

## Requirements:
 
- Python 2.7 and psql installed on your machine or virtual machine
- Terminal application 
- Files:    
    - log_analysis.py
    - [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
        - Make sure to click the link above to download newsdata.zip and you will need to unzip it in the same directory as log_analysis.py
        - To unzip in Windows 7, 8, and 10 you will have to right click the zip file and click Extract all then just follow the instructions.
        - To unzip in a Mac, just double click the zip file and it will unzip in the residing directory 

### Usage
1. You need to load the data into the directory hosting your log analysis files. To do so, you will need to run this command in your terminal (in the same directory as the log_analysis files). 
```sh
psql -d news -f newsdata.sql
```
 2. Create a VIEW called "articles_log".

``` sh
CREATE VIEW articles_log as
SELECT articles.author as author_id, articles.title AS title, log_views AS views
FROM articles
JOIN (
  SELECT path, COUNT(path) AS log_views
  FROM log
  WHERE status='200 OK'
  GROUP BY path
) as subq
ON '/article/' || articles.slug = subq.path
ORDER BY views DESC;
```
**Output:**
```sh
news=> SELECT * FROM articles_log;
 author_id |               title                | views
-----------+------------------------------------+--------
         2 | Candidate is jerk, alleges rival   | 338647
         1 | Bears love berries, alleges bear   | 253801
         3 | Bad things gone, say good people   | 170098
         1 | Goats eat Google's lawn            |  84906
         2 | Trouble for troubled troublemakers |  84810
         4 | Balloon goons doomed               |  84557
         1 | There are a lot of bears           |  84504
         1 | Media obsessed with bears          |  84383
(8 rows)
```

 3. Exit out of psql, type the command below and hit enter. Or just open a new terminal in the same directory.
 ```sh
 news => \q
 ```
 4. Run log_analysis.py 
``` sh
$ python log_analysis.py
```
Or 
```sh
$ py log_analysis.py
```
### References:

to_char()
https://www.postgresql.org/docs/current/functions-formatting.html

SUM(CASE....
Udacity student hub 
Jakob K.
1:01 AM, Dec 28
