#!/usr/bin/env python2
import psycopg2

DBNAME = "news"

query1 = """select articles.title,count(*) as articles_sum from articles,log
where log.path LIKE concat('%',articles.slug) group by articles.title order
by articles_sum DESC LIMIT 3"""

query 2 = """select authors.name,count(*) as author_sum from articles,
authors,log where authors.id = articles.author
and log.path LIKE concat('%',articles.slug)
group by authors.name order by  author_sum DESC"""

query3 = """select date(time),
round(100.00*sum(CASE WHEN status = '404 NOT FOUND'
THEN 1 ELSE 0 END) / count(log.status),2)
as bug from log group by date(time) order by bug DESC LIMIT 1"""


def popular_article(query1):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query1)
    results = c.fetchall()
    d = len(results)
    for i in range(0, d):
        title = results[i][0]
        views = results[i][1]
        print("%s--->%d" % (title, views))
    db.close()


def popular_authors(query2):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query2)
    results = c.fetchall()
    d = len(results)
    for i in range(0, d):
        name = results[i][0]
        views = results[i][1]
        print("%s--->%d" % (name, views))
    db.close()


def percent_error(query3):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query3)
    results = c.fetchall()
    d = len(results)
    for i in range(0, d):
        date = results[i][0]
        err_prc = results[i][1]
        print("%s--->% .1f %%" % (date, err_prc))

if __name__ == "__main__":
    print("Most Popular Three Article of all time:")
    popular_article(query1)
    print("\n")
    print("Most POPULAR AUTHORS of all time:")
    popular_authors(query2)
    print("\n")
    print("Percentage 1 Request")
    percent_error(query3)
