class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sales=float('inf')
        max_sales=0
        for prof in prices:
            if prof < min_sales:
                min_sales=prof
            elif prof-min_sales>max_sales:
                max_sales=prof-min_sales
        return max_sales