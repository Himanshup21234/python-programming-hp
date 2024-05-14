from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = list(set(nums))
        print(nums)
        return len(nums)


class FinalSolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        cnt = 0
        while idx <= len(nums)-2:
            if nums[idx] != nums[idx+1]:
                cnt += 1
            else:
                nums.remove(nums[idx+1])
                idx -= 1
            idx += 1
        print(nums, cnt)
        return cnt + 1

class FinalSolution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        for idx in range(1,len(nums)):
            if nums[idx-1] != nums[idx]:
                nums[cnt] = nums[idx]
                cnt += 1
        print(nums, cnt)
        return cnt + 1


nums = [1,1,2,3,4,5,5,5,6,7,7,8,8,8,9,9]
sol = FinalSolution2()
sol.removeDuplicates(nums)
