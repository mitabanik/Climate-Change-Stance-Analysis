# Climate-Change-Sentiment-Analysis

Twitter is one of the most popular social media platforms for sharing information on a variety of issues including politics, economics, science, and pop culture.
Climate change is an issue of relevant interest to many people from different spheres; however it has also become a very polarizing topic. In recent times a significant amount of opinions about climate change are formed in Twitter, using tweets is it possible to quantify the inherent biases present among people of opposite belief systems and further can one effectively distinguish climate change stances using NLP and ML techniques. Understanding the public’s stance on climate issues could be of interest to a variety of stakeholders such as policy makers, climate activists, private companies, and scientists. Therefore, accurately predicting the stance on climate change from tweets could help our leaders make better policy decisions and help combat the spread of misinformation and confusion among the public.

# Summary 
* data_raw - folder that contains the data that was extracted from twitter;
* data_utils.py and tt_scrapper - extract twitter messages; 
* Exploratory Data Analysis - exploratory analysis of data from Edward Qian (github username:edwardcqian);
* ML_models  - machine learning models used;
* Transformers - Pretrained Bidirectional Encoder Representations (BERT) model from Transformers.


# Goals
Create a stance classification algorithm to help distinguish the negative/neutral/positive climate change tweets. 

# Public pre-labelled  data
In order to train the models, we used the dataset about climate change sentiment create by Edward Qian (github username:edwardcqian) and available in https://github.com/edwardcqian/climate_change_sentiment. Removed tweets classified as ‘2’ (about 21% of original dataset) leaving us with 34667 tweets.

<img src="https://github.com/mitabanik/Climate-Change-Stance-Analysis/blob/main/img/camp.png" width="300" height="300">
Examples of our cleaned data:

* Positive stance: “teenvogue dear donald most of us do know that climate change is real a real threat”
* Negative stance: “randomsavage frmatthewlc crazy how two days ago people were going bezerk about global warming then a blizzard hits”
* Neutral stance: “myioxylouto i cant believe ed sheeran stopped global warming and ended pollution”

Positive             |  Negative
:-------------------------:|:-------------------------:
<img src="https://github.com/mitabanik/Climate-Change-Stance-Analysis/blob/main/img/camp1.png" width="350" height="250"> | <img src="https://github.com/mitabanik/Climate-Change-Stance-Analysis/blob/main/img/camp2.png" width="350" height="250">


# Training ML and DL models
Machine Learning models used:
* CountVectorizer, TfidfVectorizer and pretrained model Word2Vec for feature extraction.
* Logistic Regression, Multinomial Naive Bayes, XGBoost.

Deep Learning model used:
* Pretrained Bidirectional Encoder Representations (BERT) model from Transformers.

# Best results 
CountVectorizer Logistic  Regression 

* 76% Accuracy 
* 67% F1-score (macro)  

DistilBERT model

* 77% Accuracy 
* 67% F1-score (macro) 

DistilBert Model             |  CountVectorizer Logistic  Regression 
:-------------------------:|:-------------------------:
<img src="https://github.com/mitabanik/Climate-Change-Stance-Analysis/blob/main/img/camp4.png" width="350" height="250"> | <img src="https://github.com/mitabanik/Climate-Change-Stance-Analysis/blob/main/img/camp5.png" width="350" height="250">

1. Our analysis show that the accuracy provided by BERT is of the same order as the one of our model.
2. Classifying neutral stance is the most difficult; it is hard to distinguish b/w positive and neutral stance.

# Application of the models in historical data
We used our CountVect Logreg model on non-labeled Twitter data that we scraped using the snscrape package (100 tweets a day related to the word climate change). 
<img src="https://github.com/mitabanik/Climate-Change-Stance-Analysis/blob/main/img/camp6.png" width="800" height="300">
