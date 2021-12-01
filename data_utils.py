import re
import emoji
import nltk
import string
import snscrape.modules.twitter as sntwitter
import itertools
import pandas as pd
import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nltk.download('words')
words = set(nltk.corpus.words.words())

def search (word,since,until,near):
    return word+' '+'since:'+since+' '+'until:'+until+' '+'near:'+near

def get_tweets(query,tt_limits):
    print("Search for:" , (query))
    search=query
    scraped_tweets = sntwitter.TwitterSearchScraper(search).get_items()
    sliced_scraped_tweets = itertools.islice(scraped_tweets, tt_limits)
    df = pd.DataFrame(sliced_scraped_tweets)
    print(df.shape)
    return df

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'', text)

def clean_data(text):
    c_data= re.sub(r"(?:\|http?\://|https?\://|www)\S+", "", str(text)) 
    c_data = re.sub('[0-9]+', '', c_data)
    c_data=" ".join(c_data.split())
    c_data  = "".join([char for char in c_data if char not in string.punctuation])
    c_data=''.join(c for c in c_data if c not in emoji.UNICODE_EMOJI)
    c_data=c_data.replace("#", "").replace("_", " ")
    c_data=c_data.replace('“', '')
    c_data=c_data.replace('”','')
    c_data=c_data.replace('…','')
    c_data=deEmojify(c_data)
    
    return c_data

def count_hashtag(text):
    try:
        hashtags_count=len(text)
    except:
        hashtags_count=0
        
    return hashtags_count  

def hashtag_count_value(df):
    hashtags_name=[]
    for i in range(len(df)):
        try:
            for j in range(len(df['hashtags'][i])):
                hashtags_name.append(df['hashtags'][i][j])
        except:
            pass
    my_dict = {i:hashtags_name.count(i) for i in hashtags_name}
    return dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

def week_day(date):
    ##### monday =0, sunday=6
    year, month, day =year, month, day=str(date.date()).split('-')
    dow = datetime.date(int(year), int(month), int(day)).weekday()
    return dow

def get_VADER(text):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)['compound']