# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. 
# You can only hold at most one share of the stock at any time. However,
# you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
def buysell(prices):
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] >prices[i-1]:
            max_profit+= prices[i] - prices[i-1]
    return max_profit
# Time: O(n) — Looping through the array
# Space: O(1) — No additional space used
# Example usage:    
prices = [7,1,5,3,6,4]
print(buysell(prices))  # Output: 7
prices = [1,2,3,4,5]    
print(buysell(prices))  # Output: 4