import nltk#import libraries
from textblob import TextBlob
from newspaper import Article
nltk.download('punkt')
url = 'https://www.geeksforgeeks.org/how-to-play-a-spotify-audio-with-python/'
article = Article(url)
article.download()
article.parse()
article.nlp()
text= article. summary
print (text)
blob= TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print (sentiment)