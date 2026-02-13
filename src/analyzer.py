import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


#We do this to see if the vader lexicon file is already installed or no.
try:
    nltk.data.find("sentiment/vader_lexicon.zip")

except LookupError:
    nltk.download("vader_lexicon")


#we initialize the model for the sentiment analysis out of the function so python does not have to reload every time the dictionary of VADER
sia = SentimentIntensityAnalyzer()

#function to do the sentiment of the news
def get_sentiment(text):

    scores = sia.polarity_scores(text)
    return scores["compound"]



if __name__ == "__main__":
    print(get_sentiment("Bitcoin is good, great and the best investment!"))
    print(get_sentiment("Bitcoin is bad, terrible and the worst loss ever."))