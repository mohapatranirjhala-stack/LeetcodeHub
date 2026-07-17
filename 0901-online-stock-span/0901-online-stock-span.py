class StockSpanner(object):

    def __init__(self):
        # The stack stores pairs of: (price, span)
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        
        # Collapse all previous elements with a price <= the current price
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
            
        # Push the current price and its accumulated span onto the stack
        self.stack.append((price, span))
        
        return span