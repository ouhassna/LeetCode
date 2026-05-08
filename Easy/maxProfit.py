class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy , sell = 0, 1
        maxP = 0
        while buy < len(prices):
            if prices[sell] < prices[buy]:
             profit = prices[sell] - prices[buy]
             maxP = max(maxP , profit)
            else:
                sell += 1
            buy += 1
        return MaxP

