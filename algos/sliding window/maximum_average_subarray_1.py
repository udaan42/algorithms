class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum  = 0
        avg = float('-inf')
        for i,num in enumerate(nums):
            sum += num
            if i >= k-1:
                avg = max(avg,sum/k)
                sum -= nums[i-(k-1)]

        return avg


        