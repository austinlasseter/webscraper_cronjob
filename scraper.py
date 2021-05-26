import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

# define scraper
def lovely_soup(url):
    # https://recycledrobot.co.uk/words/?web-scraping
    r = requests.get(url, headers = {'User-agent': 'Agent_Smith'})
    return BeautifulSoup(r.text, 'lxml')

# write a function to clean up the date
def parse_that_date(row):
    x = row.split(' ')[1:]
    y = ' '.join(x)
    z = '2020 '+ y
    return z[:20]

# primary function
def scrape_that_page():
    # scrape the page
    url = 'https://old.reddit.com/r/AskReddit/'
    soup = lovely_soup(url)

    # gather the titles
    titles = soup.findAll('p', {'class': 'title'})
    titleslist=[]
    for title in titles:
        titleslist.append(title.text)

    # gather the dates
    dates = soup.findAll('time', {'class':"live-timestamp"})
    dateslist=[]
    for date in dates:
        output = str(date).split('title="')[1].split('">')[0]
        dateslist.append(output)

    # convert the two lists into a pandas dataframe
    df_dict={'date':dateslist, 'post':titleslist}
    working_df = pd.DataFrame(df_dict)
    pd.set_option('display.max_colwidth', 200)
    working_df['date'] = working_df['date'].str.strip()

    # apply the date parsing function and sort the dataframe
    working_df['cleandate']=working_df['date'].apply(parse_that_date)
    # print(parse_that_date(working_df.iloc[1,0]))
    # print(working_df[['date', 'cleandate']].head())
    working_df['UTC_date'] = pd.to_datetime(working_df['cleandate'])
    working_df.sort_values('UTC_date', inplace=True, ascending=False)
    final_df = working_df.drop(['date', 'cleandate'], axis=1)[['UTC_date', 'post']]

    # write html to file
    html = final_df.to_html(index=False)
    text_file = open("static/redditposts.html", "w")
    text_file.write(html)
    text_file.close()





# deploy the function
if __name__ == "__main__":
    scrape_that_page()

# reference:
# https://recycledrobot.co.uk/words/?web-scraping
