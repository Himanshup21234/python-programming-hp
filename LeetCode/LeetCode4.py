from typing import List

class NaiveFinalSolution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        first_index = second_index = second_val = first_val = None
        while i < len(nums)-1:
            first_val = nums[i]
            first_index = i
            diff_target = target - first_val
            # if diff_target >= 0:
            for idx in range(len(nums)):
                if nums[idx] == diff_target and idx != first_index:
                        second_val = nums[idx]
                        second_index = idx
                        break
            if second_index is not None:
                break
            i += 1

        print(first_val, first_index, second_val, second_index)
        return [first_index, second_index]

class BruteForceSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found

class BetterFinalSolution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            diff_target = target - nums[i]
            if diff_target in hashMap:
                return [hashMap[diff_target], i]
            hashMap[nums[i]] = i
        return []

nums = [2,7,11,15]
target = 18
sol = BetterFinalSolution()
print(sol.twoSum(nums, target))

nums = [3,3]
target = 6
sol = BetterFinalSolution()
print(sol.twoSum(nums, target))

nums = [0,4,3,0]
target = 0
sol = BruteForceSolution()
print(sol.twoSum(nums, target))

nums = [-1,-2,-3,-4,-5]
target = -8
sol = BruteForceSolution()
print(sol.twoSum(nums, target))