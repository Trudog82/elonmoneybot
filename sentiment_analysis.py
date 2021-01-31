from textblob import TextBlob
from AlpacaAPI import *
from Crypto_sel import *

def sentimentAnalysis():
    pos_count = 0
    pos_correct = 0

    neg_count = 0
    neg_correct = 0

    total_count = 0

    tickerName = ""
    
    stockBool = False
    cryptoBoolean = False

    with open("fullTweet.txt", "r") as fulltweets:
        for line in fulltweets:
            full_tweet = line
            for word in line.split():
                if(word == "don't" or word == 'dont'):
                    neg_correct += 1
                    
                if(word[0] == "?" or word[0] == "#"):
                    word = word[1:]
                
                analysis = TextBlob(word)

                if analysis.sentiment.polarity <= 0:
                    if analysis.sentiment.polarity <= -0.0001:
                        neg_correct += 1
                    #neg_count += 1
                total_count += 1
                
                #stock names and tickers 
                big_stocks_dictionary = {}
                big_stocks_file = open("tickersBigTXT.txt")
                for line_ in big_stocks_file:
                    value, key = line_.lower().split()
                    big_stocks_dictionary[key] = value

               #find if its in the dictionary 
                if word.lower() in  big_stocks_dictionary.keys():
                   tickerName = big_stocks_dictionary[word]
                   stockBool = True
                   print("1")
                elif word.lower() in big_stocks_dictionary.values():
                    tickerName = word
                    stockBool = True
                    print("2")
                else:
                    
                    # all traded tickers
                    fileHandler = open("tickersTXT.txt", "r")
                    listOfLines = fileHandler.readlines()
                    for line_ in listOfLines:
                        if(line_.strip().lower() == word.lower()):
                            tickerName = word
                            stockBool = True
                            print("3")
                            break
                    
                #Crypto Dictonary 
                crypto_dictionary = {}
                crypto_file = open("tickersCryptoTXT.txt")
                for line_ in crypto_file:
                    value, key = line_.lower().split()
                    crypto_dictionary[key] = value

               #find if its in the dictionary 
                if word.lower() in crypto_dictionary.keys():
                   tickerName = crypto_dictionary[word]
                   cryptoBoolean = True
                elif word.lower() in crypto_dictionary.values():
                   tickerName = word
                   cryptoBoolean = True
                
                
    #pos_acc = pos_correct/total_count*100.0
    neg_acc = neg_correct/total_count*100.0

    #print("Positivity of tweet = {}% via {} samples".format(pos_acc, pos_count))
    print("Negativity of tweet = {}% ".format(neg_acc))

    print()

    if(neg_acc < 30):
        print("neg")
        if(cryptoBoolean == True):
            crypto_bot(tickerName.upper(), 50000, 50000, full_tweet)
        elif(stockBool == True):
            print("use alpaca", tickerName)
            Alpaca_func(tickerName.upper(), 1)

    
    stockBool = False
    cryptoBoolean = False
    time.sleep(30)
    
    stockBool = False
    cryptoBoolean = False

    # print("WE NEED TO INVEST IN", tempStock) #send the name of stock/crypto to API function to buy
