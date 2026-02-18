from src.scraper import get_crypto_news
from src.analyzer import get_sentiment
from src.database import init_db,save_news
import datetime

def main():
    init_db() #the first thing we do is to initialize the db.
    
    df_news = get_crypto_news()
    print(f"Downloaded {len(df_news)} news.")

    list_news = df_news.to_dict(orient="records") #we convert the dataframe in a list of dict because we need this format in the database

    save_news(news_list=list_news)
    time = datetime.datetime.now()
    print(f"Finished! The database has been updated at {time.strftime('%H:%M:%S')}")



if __name__ == "__main__":
    main()