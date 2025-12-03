"""
Created Oct 2025

@author: V_Morgan

Natural Language Processing:
    
Web Scraping and Analysis -html pages for Stock information and sentiment
"""
import time
from nltk import sent_tokenize
from nltk import word_tokenize
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from nltk.probability import FreqDist
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as vis
from nltk.corpus import stopwords
from wordcloud import WordCloud
#import nltk
#nltk.download('vader_lexicon')

#custom stopwords for user addition
custom_stopwords = []
class HTML_web_scraper:          
    def accessData(self, html_url, company): 
        try:
            #Implementation of headers to attempt to bypass anti-scraper protection
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Accept-Language': 'en-US,en;q=0.9', 'Accept-Encoding': 'gzip, deflate','Connection': 'keep-alive'}
            req = Request(html_url, headers=headers)
            html_xters = urlopen(req).read()
            html_Data = html_xters.decode("utf-8", "ignore") 
            print('Character Length = ', len(html_Data))
            print('\n DISPLAY SOME TEXT: \n', html_Data[:100])
                    
            cleaner_Data = BeautifulSoup(html_Data, features="lxml").get_text()
            cleaner_Data = ' '.join(cleaner_Data.split())  
    
            print('\n Cleaner Text: ', cleaner_Data[:200])
            self.cleaner_Data = cleaner_Data
            
        except Exception as e:
            #Allowing user to enter text if scraper is unable to access website automatically.
            print(f"Unable to access the URL provided for {company}.")
            pasteText = input(f"Paste some text from the {company} article here to have it analyzed:")
            self.cleaner_Data = pasteText
        
        
    def Sentence_tokenizer(self):    
        sentences = sent_tokenize(self.cleaner_Data)
        sentences = [w.replace('\n','').lower() for w in sentences]
        print('\n Number of Sentences = ', len(sentences))
        print('\n Some Sentences: \n', sentences[:10])
        
    def Word_tokenizer(self):    
        all_words = word_tokenize(self.cleaner_Data)
        print('\n Number of Words = ', len(all_words))
        print('\n Some Words: \n', all_words[:10])
        self.all_words = all_words
        
    def getRid_meaningless_xters(self):
        global custom_stopwords
        words_minus_punct = []
    
        # Remove punctuation / non-alphabetic tokens
        for wd in self.all_words:
            if wd.isalpha():
                words_minus_punct.append(wd.lower())
    
        # Ask the user for additional words to ignore
        while True:
            addition = input("Add a word you'd like to be ignored or enter q to stop: ").strip().lower()
            if addition == 'q':
                break
            elif addition != "":
                custom_stopwords.append(addition)
    
        # Combine default stopwords + user-provided ones
        conjuctions = stopwords.words("english")
        all_stopwords = set(conjuctions + custom_stopwords)
    
        # Filter words
        meaningful_words = [wd for wd in words_minus_punct if wd not in all_stopwords]
    
        print("\nSample of meaningful words:", meaningful_words[:20])
        self.meaningful_words = meaningful_words

    
    def Word_Distr_visualizer(self):  
        word_freq = FreqDist(self.meaningful_words)
        print('\n', word_freq.most_common(20))
        
        #plot word frequency
        word_freq.plot(20)
        vis.title("Top 20 Most Common Words")
        vis.xlabel("Words")
        vis.ylabel("Frequency")
        vis.show()
        
    def decode_message(self):
        decision_keywords = WordCloud().generate(str(self.meaningful_words))
        vis.figure(figsize = (14,14))
        vis.axis("off")
        vis.imshow(decision_keywords)    
        vis.show()
        
    def sentiment_analysis(self, company):
        print(f"\nAnalyzing sentiment for {company}...")
        sia = SentimentIntensityAnalyzer()

        #Adding finance words to our sentiment lexicon for more accutate sentiment predictions.
        finance_lexicon = {
            "losses": -3.0,
            "plunge": -3.0,
            "crash": -3.5,
            "bearish": -2.5,
            "recession": -3.0,
            "underperform": -2.5,
            "volatility": -2.0,
            "selloff": -3.0,
            "downgrade": -2.5,
            "slump": -3.0,
            "risk": -2.0,
            "uncertain": -2.0,
            "profit": 3.0,
            "gain": 2.5,
            "growth": 3.0,
            "bullish": 2.5,
            "surge": 3.5,
            "upgrade": 2.5,
            "strong": 2.0,
            "record": 2.5,
            "rebound": 3.0,
            "opportunity": 2.0,
            "expansion": 2.5
        }
        sia.lexicon.update(finance_lexicon)
        
        sentences = sent_tokenize(self.cleaner_Data)
        compound_scores = [sia.polarity_scores(s)['compound'] for s in sentences]
        avg_score = sum(compound_scores) / len(compound_scores)
        
        if avg_score >= 0.41:
            sentiment = "Positive"
        elif avg_score <= 0.2:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        
        print(f"Overall Sentiment for {company}: {sentiment} (score={avg_score:.3f})")
        self.sentiment = sentiment

        
        
        
        
        
        
#----------------------------Drive above code----------------------------------
handle = HTML_web_scraper()
handle2 = HTML_web_scraper()

# HTML pages
print('\n SCRAPING HTML PAGES')

while True:
    company1 = input("Enter the first company for comparison: ")
    company2 = input("Enter the second company for comparison: ")

    html_url1 = input(f"Enter an article for {company1}.")
    html_url2 = input(f"Enter an article for {company2}.")
    
    handle.accessData(html_url1, company1)
    handle2.accessData(html_url2, company2)
    
    #Tokenize Sentences
    print('\n UNCLEAN TOKENIZED SENTENCES FOR', html_url1, ":")
    handle.Sentence_tokenizer()
    
    print('\n UNCLEAN TOKENIZED SENTENCES FOR', html_url2, ":")
    handle2.Sentence_tokenizer()
    
    #Tokenize Words
    print('\n UNCLEAN TOKENIZED WORDS FOR', html_url1, ":")
    handle.Word_tokenizer()
    
    print('\n UNCLEAN TOKENIZED WORDS FOR', html_url2, ":")
    handle2.Word_tokenizer()
    
    
    #Get Rid of Meaningless Words and Visualize
    print('\n MEANINGFUL WORDS FOR', html_url1, ":")
    handle.getRid_meaningless_xters()
    
    print('\n MEANINGFUL WORDS FOR', html_url2, ":")
    handle2.getRid_meaningless_xters()
    
    #Frequency of Words and Visualization
    print('\n FREQUENCY: MOST COMMON WORDS AND VISUALIZATION FOR ', company1, ":")
    handle.Word_Distr_visualizer()
    
    print('\n FREQUENCY: MOST COMMON WORDS AND VISUALIZATION FOR', company2, ":")
    handle2.Word_Distr_visualizer()
    
    
    #Visualize and Decode Messages
    print('\n VISUAL DECODING FOR QUALITATIVE SENTIMENT OF', company1, ":")
    handle.decode_message()
    
    print('\n VISUAL DECODING FOR QUALITATIVE SENTIMENT OF', company2, ":")
    handle2.decode_message()
    
    #Analyze and Provide Sentiment
    print('\n Sentiment analysis for', company1, ":")
    handle.sentiment_analysis(company1)
    
    print('\n Sentiment analysis for', company2, ":")
    handle2.sentiment_analysis(company2)
    
    n = input("\n Press Enter-key to continue or enter 'q' to Quit: ")
    if n.strip().lower() == 'q':
        print("Please be safe in the environment...")
        break