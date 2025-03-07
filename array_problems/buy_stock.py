class Solution:
  def time_to_buy_stocks(self):
    min_price = float('inf')
    max_profit = 0
    days = [7,1,5,3,6,2,10,8,15]
    buy_day = 0
    sell_day = 0

    for day, price in enumerate(days):
      if price < min_price:
        min_price = price
        buy_day = day
      
      if max_profit < price - min_price:
        max_profit = price - min_price
        sell_day = day
      
    print(f"Buy-Day: {buy_day}\nSell-Day: {sell_day}\nMaximum profit: {max_profit}")

""" 
(REVIEW)
Basically find the minimum price on a buy day, then see if the next days have 
a lower price to find a new buy day, then find the profit margin. If profit
margin is greater than before, it is the new maximum profit.
At the end it will find the max profit and return it
"""

if __name__ == '__main__':
  solution = Solution()
  solution.time_to_buy_stocks()