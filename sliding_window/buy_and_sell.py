#!/usr/bin/env python
def maxProfit(self, prices: List[int]) -> int:
    answer = 0
    prev_price = prices[0] + 1
    for k, v in enumerate(prices):
        if v < prev_price:
            prev_price = v
        if v - prev_price > answer:
            answer = v - prev_price


    return answer


if __name__ == "__main__":
    main()
