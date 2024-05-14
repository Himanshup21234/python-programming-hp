from typing import List


class Solution1:
    """
    Two integer arrays nums1 and nums2 - sorted in non-decreasing order
    Two integers m and n - representing the number of elements in nums1 and nums2
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m = m-1
        n = n-1
        p = 0
        i = j = 0
        final = []
        nums1 = nums1[:m+1]
        nums2 = nums2[:n+1]
        if n < 0 or m < 0:
            final = nums1 + nums2
        else:
            if nums1[m] <= nums2[0]:
                final = nums1 + nums2
            elif nums1[0] >= nums2[n]:
                final = nums2 + nums1
            else:
                while i <= m and j <= n:
                    if nums1[i] <= nums2[j]:
                        final.append(nums1[i])
                        i += 1
                    else:
                        final.append(nums2[j])
                        j += 1
                while j <= n:
                    final.append(nums2[j])
                    j += 1
                while i <= m:
                    final.append(nums2[j])
                    j += 1
        print(final)

class FinalSolution:
    """
    Two integer arrays nums1 and nums2 - sorted in non-decreasing order
    Two integers m and n - representing the number of elements in nums1 and nums2
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        final_idx = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[final_idx] = nums1[m-1]
                m -= 1
            else:
                nums1[final_idx] = nums2[n-1]
                n -= 1
            final_idx -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
            final_idx = 0
        print(nums1)


nums1 = [0]
m = 0
nums2 = [1]
n = 1
sol = FinalSolution()
sol.merge(nums1,m ,nums2, n)

nums1 = [0,0]
m = 0
nums2 = [1,2]
n = 2
sol = FinalSolution()
sol.merge(nums1,m ,nums2, n)

nums1 = [1,2,3,5,6,7,8,0,0,0]
m = 7
nums2 = [5,5,7]
n = 3
sol = FinalSolution()
sol.merge(nums1,m ,nums2, n)

nums1 = [3,3,0,0,0,0,0,0,0]
m = 2
nums2 = [1,2,3,5,6,7,8]
n = 7
sol = FinalSolution()
sol.merge(nums1,m ,nums2, n)


nums1 = [1,2,3,0,0,0,0,0]
m = 3
nums2 = [2,5,6,7,8]
n = 5
sol = FinalSolution()
sol.merge(nums1,m ,nums2, n)


nums1 = [1]
m = 1
nums2 = []
n = 0
sol = FinalSolution()
sol.merge(nums1,m ,nums2, n)