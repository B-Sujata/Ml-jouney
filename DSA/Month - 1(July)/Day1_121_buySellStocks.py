class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        days = {}
        for day, price in prices:
            if price == mini:
                days["min_price_day"] = mini
                lowest_price_day = day
            if price == maxi:
                days["max_price_day"] = maxi
                highest_price_day = day

            if lowest_price_day<highest_price day:
                buy = lowest_price_day
                sell = highest_price_day
                profit = maxi-mini
                return profit
            elif:
                
        
            
                

            

            
        
        