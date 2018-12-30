# Logs Analysis

Retrieves the three most popular articles, most popular article authors, and which day(s) had more than 1% of requests lead to errors. Using a secret wizardry called sql and python. Files that should be included are log_analysis.py, log_analysis_output.txt, and README.md 

## Requirements:
 
- Python 2.7 installed on your machine or virtual machine
- Terminal application 
- Files (log_analysis.py and newsdata.sql)

### Usage

Open your terminal program in the directory hosting your log analysis files. First create a VIEW called "articles_log".

``` sh
CREATE VIEW articles_log as SELECT articles.author as author_id, articles.title as title, log_views as views FROM articles JOIN (SELECT regexp_replace(path,'/article/','') as slug, COUNT(path) as log_views FROM log WHERE status='200 OK' GROUP BY slug ORDER BY log_views DESC) as subq ON articles.slug LIKE subq.slug ORDER BY views DESC;
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

After that, type:
``` sh
$ Python log_analysis.py
```
Or 
```sh
$ py log_analysis.py
```
