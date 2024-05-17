from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        data = {}
        n = len(nums) / 2
        data = defaultdict(int)
        for i in range(len(nums)):
            data[nums[i]] += 1
        data = [k for k,v in data.items() if v>n]
        print(data, n)
        if data is not None:
            return data[0]
        else:
            return 0


class BetterSolution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        data_dict = defaultdict(int)
        for i in nums:
            data_dict[i] += 1
        for k,v in data_dict.items():
            if v > n:
                return k
        return 0


nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))