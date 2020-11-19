# webscraper cronjob

I installed a cronjob on a digital ocean droplet that runs the script `scraper.py` every 10 minutes as follows:
```
* /10 * * * * cd /root/myproject/webscraper_cronjob && /root/myproject/myprojectenv/bin/python /root/myproject/webscraper_cronjob/scraper.py
```
To confirm that the cronjob is actually running, the webpage displays the most recent log entry from `syslog`, equivalent to the command:
```
grep CRON /var/log/syslog
```

The python script `scraper.py` scrapes AskReddit for recent posts and saves them to the table `reddit_posts.html`. On the same droplet I installed a Flask app which displays the results of the scraped posts. The results can be seen here: http://134.209.70.210:5000/

The flask app is kept running in the background after I close terminal thanks to `screen`.
