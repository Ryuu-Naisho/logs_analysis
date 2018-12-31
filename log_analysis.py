#!/usr/bin/env python

import psycopg2

DBName = "news"



def get_popular_articles():
    '''Prints the top three popular articles.

    Prints the top three most viewed articles. Includes the title and
    number of views, ordered by view descending.
    '''
    
    query = 'SELECT title, views FROM articles_log ORDER BY views DESC LIMIT 3'
    db = psycopg2.connect(database=DBName)
    cursor = db.cursor()
    cursor.execute(query)
    articles = cursor.fetchall()
    db.close()
    
    print ('\n')
    print ('Top Three articles:')
    print ('\n')
    
    for title, views in articles:
        print('"{}" => {} views'.format(title, views))
        
    return


def get_popular_authros():
    '''Print most popular authors.

    Prints the most popular authors in descending order by combined
    views of each of their articles. Prints the author's name and total
    views.
    '''
    
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
    
    for author, views in authors:
        print ('{} => {} views'.format(author,views))
        
    return


def get_days_percent_error():
    '''Prints days which lead to mare than 1% error.

    Prints the day and perecentage in which requests lead to more than
    1% of the errors. Aggregated by the '404 NOT FOUND' status codes collected.
    '''

    query = '''SELECT date,
    percent FROM (SELECT to_char(time,'MON DD YYYY') as date,
    round(100.0*SUM(case log.status when '404 NOT FOUND' then 1 else 0
    end)/count(log.status),2) as percent FROM log GROUP BY date ORDER BY
    percent DESC) as subq WHERE percent>1.00;'''

    db = psycopg2.connect(database=DBName)
    cursor = db.cursor()
    cursor.execute(query)
    errors = cursor.fetchall()
    db.close()
    
    print ('\n')
    print ('Days which requests lead to more than 1% of the errors:')
    print ('\n')

    for date, error in errors:
        print ('{} => {}%%'.format(date,error))
        
    return


get_popular_articles()
get_popular_authros()
get_days_percent_error()
