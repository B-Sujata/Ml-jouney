# This below is the approach I came up with first and it worked and passed many of the cases but there are two problems here, one is it's time complexity and other is, the memory, because of storing every possible difference, it's memory limit exceeded so it couldn't be submitted on leetcode

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         all_profit = []
#         if prices==sorted(prices, reverse=True):
#             return 0
#         else:
#             for i in range(len(prices)):
#                 for j in range(i+1, len(prices)):
#                     profit = prices[j]-prices[i]
#                     all_profit.append(profit)
#             ans = max(all_profit)
#             return ans
        
## Then my friend, I came up with this solution....But this time the time limit exceeded because of the number of comparisons

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
        
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 profit = prices[j]-prices[i]
#                 if profit>max_profit:
#                     max_profit = profit
#         return max_profit
            
                
### Then I finally discovered a right O(n) solution for this problem

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price=prices[0]
        
        for i in range(1,len(prices)):
            if prices[i]<min_price:
                min_price = prices[i]
            if prices[i]-min_price>max_profit:
                max_profit =prices[i]-min_price
        return max_profit
                    
            
            

        
    
# ##Approach

# We need to find the maximum profit that can be earned by buying a stock on one day and selling it on a later day.

# Instead of checking every possible buy-sell pair (which takes O(n²) time), we traverse the array only once.

# While traversing:

# Keep track of the minimum price seen so far.

# For each current price, calculate the profit if we sold the stock today:

# profit = current_price - minimum_price
# If this profit is greater than the maximum profit found so far, update max_profit.
# If the current price is lower than the minimum price, update minimum_price.


# This way, we always know the cheapest buying price before the current day, allowing us to compute the best possible profit in a single pass


### Algorithm
# Initialize:
# min_price as the first element of the array.
# max_profit as 0.
# Traverse the array from left to right.
# For each price:
# If the current price is smaller than min_price, update min_price.

# Calculate:

# current_profit = current_price - min_price
# If current_profit is greater than max_profit, update max_profit.
# After traversing the entire array, return max_profit.
            

# Time Complexity - O(n)
# Space Complexity - O(1)

            
        
# Similar question withn some variation came in my infosys test yesterday
