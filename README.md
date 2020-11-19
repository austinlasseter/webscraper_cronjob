# webscraper cronjob

I installed a cronjob on a digital ocean droplet that runs the script `scraper.py` every 10 minutes as follows:
```
* /10 * * * * cd /root/myproject/webscraper_cronjob && /root/myproject/myprojectenv/bin/python /root/myproject/webscraper_cronjob/scraper.py
```
Confirm this by checking the logs:
```
grep CRON /var/log/syslog
```

The script scrapes reddit for recent posts and saves them to the table `reddit_posts.html`.
On the same droplet I installed a Flask app which displays the results of the scraped posts.
When the Flask app is running, the results can be seen here: http://134.209.70.210:5000/
