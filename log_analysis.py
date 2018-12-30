#!/usr/bin/env Python 2.7.12

import psycopg2

DBName = "news"


# Returns three popular articles.

def get_popular_articles():

    query = 'SELECT title, views FROM articles_log ORDER BY views DESC LIMIT 3'

    db = psycopg2.connect(database=DBName)

    cursor = db.cursor()

    cursor.execute(query)

    articles = cursor.fetchall()

    db.close()

    print ('\n')

    print ('Top Three articles:')

    print ('\n')

    for article in articles:

        print ('"%s" => %s views'%(article[0],article[1]))

    return


# Print most popular authors.

def get_popular_authros():

    query = '''SELECT authors.name as author, total_views FROM authors,

    (SELECT articles_log.author_id as author_id, SUM(articles_log.views)

    as total_views FROM articles_log GROUP BY articles_log.author_id

    ORDER BY total_views DESC) as subq WHERE authors.id =

    subq.author_id;'''

    db = psycopg2.connect(database=DBName)

    cursor = db.cursor()

    cursor.execute(query)

    authors = cursor.fetchall()

    db.close()

    print ('\n')

    print ('Most popular article authors: ')

    print ('\n')

    for author in authors:

        print ('%s => %s views'%(author[0],author[1]))

    return


# Prints days which lead to mare than 1% error.

def get_days_percent_error():

    query = '''SELECT date, percent FROM (SELECT to_char(time,'MON DD
    YYYY') as date, round(100.0*SUM(case log.status when '404 NOT FOUND'
    then 1 else 0 end)/count(log.status),2) as percent FROM log GROUP BY
    date ORDER BY percent DESC) as subq WHERE percent>1.00;'''

    db = psycopg2.connect(database=DBName)

    cursor = db.cursor()

    cursor.execute(query)

    errors = cursor.fetchall()

    db.close()

    print ('\n')

    print ('Days which requests lead to more than 1% of the errors:')

    print ('\n')

    for error in errors:

        print ('%s => %s%% errors'%(error[0],error[1]))

    return


get_popular_articles()
get_popular_authros()
get_days_percent_error()
