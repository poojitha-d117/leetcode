class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pri=prices[0]
        max_profit=0
        for price in prices:
            if price<min_pri:
                min_pri=price
            profit=price-min_pri
            if profit>max_profit:
                max_profit=profit
        return max_profit