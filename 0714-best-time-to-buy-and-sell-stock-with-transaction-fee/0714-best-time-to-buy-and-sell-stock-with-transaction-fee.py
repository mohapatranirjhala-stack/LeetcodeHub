class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
            
        # 'hold' tracks the maximum profit if we currently own a stock.
        # We start by "buying" the stock on day 0, which costs prices[0].
        hold = -prices[0]
        
        # 'free' tracks the maximum profit if we do not own a stock.
        # We start with 0 profit on day 0.
        free = 0
        
        for price in prices[1:]:
            # To get the optimal 'hold' state for today:
            # - We keep our previous stock (hold), or
            # - We buy today's stock using yesterday's free cash (free - price)
            hold = max(hold, free - price)
            
            # To get the optimal 'free' state for today:
            # - We remain stock-free (free), or
            # - We sell our stock at today's price and pay the fee (hold + price - fee)
            free = max(free, hold + price - fee)
            
        return free