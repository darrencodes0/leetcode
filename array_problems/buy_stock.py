def time_to_buy_stocks(self):
    min_price = float('inf')
    max_profit = 0
    days = [7,5,3,6,2,10,8]

    for price in days:
      if price < min_price:
        min_price = price
      
      if max_profit < price - min_price:
        max_profit = price - min_price
      
    return f"Maximum profit: {max_profit}"
  
  """ 
  (REVIEW)
  Basically find the minimum price on a buy day, then see if the next days have 
  a lower price to find a new buy day, then find the profit margin. If profit
  margin is greater than before, it is the new maximum profit.
  At the end it will find the max profit and return it
  """
