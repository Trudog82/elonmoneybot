from selenium import webdriver
#driver = webdriver.Chrome()
account_total_USD = 10000

#login 



def crypto_bot(TCKER, account_total_USD, account_total_BTC):
    driver = webdriver.Chrome()
        
    #login
    driver.get("https://cryptoparrot.com/login")
    
    user = driver.find_element_by_name("email")
    password = driver.find_element_by_name("password")
    
    user.clear()
    password.clear()
    
    email = "cyrusb01@tamu.edu"
    passWord = "elonmoneybot"
    
    user.send_keys(email)
    password.send_keys(passWord)
    driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/div/div/div[1]/div/form/button").click()
    
    
    #clicks new trade 
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[4]/button").click()
    
    
    percent_invest = .1
    amount_USD = str((account_total_USD * percent_invest))
    
    #Finding the price of Bitcoin
    bitPrice_html = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/p[2]/span[2]")
    bitPrice = bitPrice_html.get_attribute("innerHTML")
    bitPrice = bitPrice.replace(".00", '')
    bitPrice = float(bitPrice)
    
    amount_BTC = str(account_total_BTC * percent_invest / bitPrice)
    
    buy_box = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div/div/div[3]/div[1]/div[1]/div/div[1]/div/input")
    
    if(TCKER == "BTC"):
        #driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div/div/div[3]/div[3]/div[1]/div/label").click()
        buy_box.send_keys(amount_USD) #USD
        account_total_USD -= float(amount_USD)
        
        #Opens the textbox
        text_box = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div/div/div[3]/div[4]/div[1]/div[1]/textarea")
        text_box.clear()
        text_box.send_keys("Suck it ")
        
        #clicks the buy 
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div/div/div[3]/div[4]/div[3]/div[2]/button").click()
        
        
    else:
        #clicks the ticker menu
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[2]/p[1]").click()
        #driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div/div/div[3]/div[3]/div[1]/div/label").click()
        
        if(TCKER == "ETH"):
            
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[2]").click()
            buy_box.send_keys(amount_USD) #USD
            account_total_USD -= float(amount_USD)
            
            
        elif(TCKER == "LTC"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[3]").click()
            buy_box.send_keys(amount_USD) #USD
            account_total_USD -= float(amount_USD)
            
        elif(TCKER == "XRP"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[5]").click()
            buy_box.send_keys(amount_USD) #USD
            account_total_USD -= float(amount_USD)
            
        elif(TCKER == "RVN"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[6]").click()
            buy_box.send_keys(amount_BTC) #BTC
            account_total_BTC -= float(amount_BTC) * bitPrice
            
        elif(TCKER == "THR"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[7]").click()
            buy_box.send_keys(amount_BTC) #BTC
            account_total_BTC -= float(amount_BTC) * bitPrice
            
        elif(TCKER == "BAT"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[8]").click()
            buy_box.send_keys(amount_BTC) #BTC
            account_total_BTC -= float(amount_BTC) * bitPrice
            
        elif(TCKER == "EOS"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[9]").click()
            buy_box.send_keys(amount_USD) #USD
            account_total_USD -= float(amount_USD)
            
        elif(TCKER == "DSH"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[10]").click()
            buy_box.send_keys(amount_USD) #USD
            account_total_USD -= float(amount_USD)
            
        elif(TCKER == "XMR"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[11]").click()
            buy_box.send_keys(amount_USD) #USD
            account_total_USD -= float(amount_USD)
            
        elif(TCKER == "NEO"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[12]").click()
            buy_box.send_keys(amount_USD) #USD
            account_total_USD -= float(amount_USD)
            
        elif(TCKER == "OMG"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[13]").click()
            buy_box.send_keys(amount_USD) #USD
            account_total_USD -= float(amount_USD)
            
        elif(TCKER == "TUBE"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[14]").click()
            buy_box.send_keys(amount_USD) #USD
            account_total_USD -= float(amount_USD)
            
        elif(TCKER == "DGB"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[15]").click()
            buy_box.send_keys(amount_USD) #USD
            account_total_USD -= float(amount_USD)
            
        elif(TCKER == "DOGE"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[16]").click()
            buy_box.send_keys(amount_BTC) #BTC
            account_total_BTC -= float(amount_BTC) * bitPrice
            
        elif(TCKER == "STEEM"):
            driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[3]/form/div/div[17]").click()
            buy_box.send_keys(amount_BTC) #BTC
            account_total_BTC -= float(amount_BTC) * bitPrice
        
        #Opens the textbox
        text_box = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div/div/div[3]/div[4]/div[1]/div[1]/textarea")
        text_box.clear()
        text_box.send_keys("Suck it ")
        
        #clicks the buy 
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[2]/div[1]/div[2]/form/div/div/div[3]/div[4]/div[3]/div[2]/button").click()
    
    driver.close()

#crypto_bot("OMG", 50000, 50000)