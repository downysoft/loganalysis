# Log Analysis 
This software provides log analysis on a blog website's three databases: author, articles and log database. The program generates three reports.  The first report returns data on the three most popular articles of all time on the website.  The second report returns data on the most popular article authors of all time.  The third report returns data on the days which more than  1% of the requests led to errors.

## Installation (Getting Started)
This installation assumes you have Virtual Box and the Virtual Machine **installed**.  It involves using Vagrant to execute PostgreSQl.  You must also have the `newsdata.zip` downloaded and installed to make the `newsdata.sql` available to this program.

#### Follow these instructions:
  - Make sure you are in your vagrant directory.
  - If you don't have Vagrant up, issue the command `vagrant up` at the  commant prompt.  Make sure you are in your vagrant folder.
  - Once the vagrant up is done, issue the command `vagrant ssh`.
  - You should now see the vagrant prompt.  At this prompt issue the PostgreSQL command `psql news`. 
  - Load the following two views using the below commands:
  		```
  		CREATE VIEW log_errors as
  		SELECT DATE(time) AS error_date, count(*) as errors 
  		FROM log 
  		WHERE METHOD = 'GET'
  		AND SUBSTRING(path,1,2) <> ' '
  		GROUP BY error_date
        ```
        ```
        CREATE VIEW num_of_access_per_day as
        SELECT DATE(time) as access_date, count(*) as access_per_day
        FROM log
        WHERE METHOD = 'GET'
        AND SUBSTRING(path,1,2) <> ' '
        GROUP BY access_date
        ```
  - Once the views are successfully loaded, run the program using `python news.py`.  In some versions of Windows you will need to use `winpty python news.py`.
  - The three reports should display with headings in your shell window.

## Database Requirements
`Newsdata.sql` is the only database required for use by this program.  Please see the Installation section for more on how to use the database.

## Known Bugs
At this time of this writing, there are no known bugs.

## License
The contents of this repository are covered under the [MIT License](https://github.com/downysoft/loganalysis/blob/master/LICENSE).

