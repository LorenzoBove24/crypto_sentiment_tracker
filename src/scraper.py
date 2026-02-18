import pandas as pd
import feedparser
from analyzer import get_sentiment


#URL of the RSS from the website cointelegraph
RSS_URL = "https://cointelegraph.com/rss"

#function to get the title, date and link of the last news published on the website and create a dataframe
def get_crypto_news():
    feed = feedparser.parse(RSS_URL)
    news_list = []

    for entry in feed.entries:

        score = get_sentiment(entry.title)

        dic_new = {
            "title" : entry.title,
            "published" : entry.published,
            "link" : entry.link,
            "sentiment" : score
        }
        news_list.append(dic_new)
    
    df = pd.DataFrame(news_list)
    return df


#TESTING

if __name__ == "__main__":
    df = get_crypto_news()
    print(df.head())
    print(df.head())