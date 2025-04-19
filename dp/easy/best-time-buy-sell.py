# You are given an array prices where prices[i] is the price of a given stock on the ith day.
def besttimetobuyandsell(prices):
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit
# Example usage:
prices = [7,1,5,3,6,4]
print(besttimetobuyandsell(prices))  # Output: 5

# Time: O(n) — Looping through the array
# Space: O(1) — No additional space used