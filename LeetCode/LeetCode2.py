from typing import List


class Solution:
    """
    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        nums = [1 for n in nums if n != val ]
        return sum(nums)

class FinalSolution:
    """
    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for n in range(len(nums)):
            if nums[n] != val:
                nums[index] = nums[n]
                index += 1
        print(nums, index)
        return index


nums1 = [1,2,2,3,3,4,5,6]
m = 3
sol = FinalSolution()
sol.removeElement(nums1,m)