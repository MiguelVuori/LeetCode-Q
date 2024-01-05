class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        sell = 0

        for i in range(len(prices)):
            sell = i + 1
            if  sell - i > 0 and prices[i] - prices[buy] > max_profit:
                max_profit = prices[i] - prices[buy]
            if prices[i] < prices[buy]:
                buy = i
        return max_profit

            