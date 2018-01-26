
import psycopg2 
import datetime

def get_report_one():
    DB = psycopg2.connect("dbname = news")
    content_cursor = DB.cursor()
    sql_query = "SELECT title, count(*) as views from articles a , log b \
        WHERE path = concat('/article/', slug) \
        and method = 'GET' \
        and status = '200 OK' \
        group by title \
        order by views desc\
        limit 3"
    content_cursor.execute(sql_query)
    report_lines = content_cursor.fetchall()
    print "\n Report One: What are the most popular three articles of all time?"
    for row in report_lines:
        print row[0] + " -- " + str(row[1]) + " views"
    DB.close()

def get_report_two():
    DB = psycopg2.connect("dbname = news")
    content_cursor = DB.cursor()
    sql_query = "SELECT name as authors_name, count(*) as views from authors a, articles b, log c \
        WHERE b.author = a.id \
        and path = concat('/article/', slug) \
        and method = 'GET' \
        and status = '200 OK' \
        and substring(path,2,1) <> ' ' \
        group by name \
        order by views desc"
    content_cursor.execute(sql_query)
    report_lines = content_cursor.fetchall()
    print '\n Report Two: Who are the most popular article authors of all time?'
    for row in report_lines:
        print row[0] + ' -- ' + str(row[1]) + ' views'
    DB.close()

def get_report_three():
    DB = psycopg2.connect("dbname = news")
    content_cursor = DB.cursor()
    sql_query = "SELECT to_char(access_date, 'Month DD, YYYY'), \
        round(100.0 * errors / access_per_day, 1) as percent_of_errors \
        from log_errors a, num_of_access_per_day b \
        WHERE access_date = error_date \
        order by percent_of_errors desc"
    content_cursor.execute(sql_query)
    report_lines = content_cursor.fetchall()
    print '\n Report Three: On which days did more than 1% of requests lead to errors'
    for row in report_lines:
    	if row[1] > 1:
            print row[0] + ' -- ' + str(row[1]) + '% errors'
    DB.close()

get_report_one()
get_report_two()
get_report_three()