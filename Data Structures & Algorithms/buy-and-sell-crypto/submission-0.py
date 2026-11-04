class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_diff = 0
        for i, price in enumerate(prices):
            min_price = min(min_price, price)
            max_diff = max(max_diff, price-min_price)
        return max_diff

