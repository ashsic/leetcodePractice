class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        minIdx = 0
        profit = 0

        for i, price in enumerate(prices):
            if price < minPrice:
                minPrice = price
                minIdx = i
            profit = (price - minPrice) if (price - minPrice) > profit else profit
        
        return profit
        