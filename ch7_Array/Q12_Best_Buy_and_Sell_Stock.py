''' 주식 사고팔기 가장 좋은 시점
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
* 1 <= prices.length <= 105
* 0 <= prices[i] <= 104
'''
# --- 한번 훑는것으로 결정을 내려야함. -> loop 하나로 저점, 이익 동시에 tracking
from typing import List
import sys

def max_profit(prices:List[int]) -> int:
    max_profit = 0
    min_price = sys.maxsize
    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(price - min_price, max_profit)
    return max_profit


# O(n^2) 시간초과풀이
def maxProfit(prices: list) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i + 1, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price