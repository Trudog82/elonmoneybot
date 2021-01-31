import nest_asyncio
import csv
import os
import twint
import time
from datetime import datetime, timedelta
nest_asyncio.apply()

from sentiment_analysis import *

tweet = ""
while(True):
    date = datetime.now()
    dateNew = date - timedelta(seconds = 50)
    
    year = dateNew.year
    month = dateNew.month
    day = dateNew.day
    hour = dateNew.hour
    minute = dateNew.minute
    sec = dateNew.second
    dateFormat = str(year) + "-" + str(month) + "-" + str(day)
    timeFormat = str(hour) + ":" + str(minute) + ":" + str(sec)
    
    # Configure
    c = twint.Config()
    c.Since = dateFormat + " " + timeFormat
    try:
        os.remove("test.txt")
    except:
        print("")
    c.Output = "test.txt"
    csvnames = open('file(1).csv')
    
    for user in csv.reader(csvnames):
   
        c.Username = "elonmoneybot" 
   
    
    # Run
        twint.run.Search(c)
        pastTweet = tweet
        
        try:
            with open('test.txt') as txt:
                csvReader = csv.reader(txt, delimiter='`')
                row1 = next(csvReader)
                i = 0
                words = row1[0].split(' ')
                for word in words:
                    if (i > 4):
                        if (i == 5):
                            tweet = word
                        else:
                            tweet = tweet + " " + word
                        i = i + 1 
                    i = i + 1
            txt.close()
            
            if(pastTweet != tweet):
                print("\n")
                print("Tweet from @" + "elonmoneybot")
                print("-----------------------------")
                print(tweet)
                with open("fullTweet.txt", "w") as text_file:
                    text_file.write(tweet)
                sentimentAnalysis()
                os.remove("fullTweet.txt")
                print("\n\n")
                time.sleep(4)
 
            os.remove("test.txt")
            
        except:
            print("No new tweets from @" + "elonmoneybot")

