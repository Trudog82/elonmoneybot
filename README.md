# elonmoneybot


Inspiration

The recent surge in Elon Musk's influence has caused his Twitter to be a gold mine for people looking to find the next stock surge. With tweets that helped Dogecoin reach higher prices, and giving a random stock a 1000% increase, it is clear there is money to be made in Elon Musk's tweets.
What it does

The bot scrapes Twitter for Elon Musk, Joe Biden, Kamala Harris, Jeff Bezos, and Bill Gates's latest tweets and analyzes the contents to determine if there is something to be invested in. Next, it will buy the stock or currency in our trading portfolios on alpaca and crypto parrot.
How we built it

The bot is made completely in Python, utilizing multiple different packages for each step. The Twitter scraper is made using Twint, a python package that gives us access to live-tweeting. The next step utilizes TextBlob, which allows us to conduct sentiment analysis on the content of the tweets. During this step, we also used dictionaries of stock and currency symbols and names in order to determine if there are any investments that can be related to the tweet. Finally, using a paper trading API, Alpaca-API, we are able to buy stocks, and by automating a browser to crypto parrot we buy cryptocurrencies.
Challenges we ran into

Due to the large number of connections we were making to twitter, our ISP eventually limited our ability to connect to Twitter through Twint. To resolved this, we resorted to connecting our system to a VPN. Another issue that arose was that the polarity that was calculated during the sentiment analysis seemed to be a little off each time for certain words that we know for sure had negative connotations. After a bit of tweaking with the numbers, we found ones that were suitable enough to detect if the tweet was in fact negative. As well, initially, we planned on using an API for the cryptocurrency exchange, however, after multiple attempts at making it work, it was clear the API was not designed very well for the US. This caused us to change directions, into using selenium to automate the browser and basically create our own API.
Accomplishments that we're proud of

The bot works very well and is smooth with finding tweets, locating the tickers, and then buying the asset. This bot was more than we thought we could accomplish and displays all our hard work.
What we learned

Our python knowledge has grown tremendously, and now we are more familiar with Twitter, sentiment analysis, and browser automation. All these skills can be put to use in different projects, and now we will be more prepared for it.
What's next for ElonMoneyBot

The sentiment analysis can always be improved upon, and the next big step would be connecting live trading accounts to actually buy the currencies.
