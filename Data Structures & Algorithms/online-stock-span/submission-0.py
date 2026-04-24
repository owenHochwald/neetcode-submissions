class StockSpanner:
    # monotonic stack problem
        # if curr >= last item, we can reuse that thing + 1
        # if curr < last item, we have to completly restart our stack
            # maybe its not the last item, but the min among them?


    def __init__(self):
        self.stocks = []        

    def next(self, price: int) -> int:
        count = 1

        # if this one is larger than the previous before it, we have to overwrite all of those values!
        while self.stocks and price >= self.stocks[-1][0]:
            s_price, s_con = self.stocks.pop()

            count += s_con

        self.stocks.append([price, count])


        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)