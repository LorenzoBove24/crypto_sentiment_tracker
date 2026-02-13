import pandas as pd
import feedparser

RSS_URL = "https://cointelegraph.com/rss"

def get_crypto_news():
    feed = feedparser.parse(RSS_URL)
    news_list = []

    for entry in feed.entries:

        dic_new = {
            "title" : entry.title,
            "date" : entry.published,
            "link" : entry.link
        }
        news_list.append(dic_new)
    
    df = pd.DataFrame(news_list)
    return df



if __name__ == "__main__":
    df = get_crypto_news()
    print(df.head())
    print(df.head())