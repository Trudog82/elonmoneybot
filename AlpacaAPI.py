import alpaca_trade_api as tradeapi


API_Key = "PKNQH6XMU6WJIW2J5M3W"
API_Secret_Key = "xkCgJ2QWMHbgaDRx2R6UlsX6mcbbdvbplNewXAKo"
api = tradeapi.REST(API_Key, API_Secret_Key, base_url='https://paper-api.alpaca.markets')


        
def Alpaca_func(TCKER, quantity):
    clock = api.get_clock()
    api.submit_order(
        symbol= TCKER,
        side='buy',
        type='market',
        qty= quantity,
        time_in_force='gtc',
    )
    
    if clock.is_open:
        api.submit_order(
            symbol= TCKER,
            side='sell',
            type='trailing_stop',
            qty= quantity,
            trail_percent = 3.5,
            time_in_force='gtc',
        )
        
#Alpaca_func("SPY", 1)