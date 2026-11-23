#optimal solution using Hashset O(n)
#other solutions are using Brute Force [O(n2) Comparing every element against AND Sorting O(1)]
#Remember: The fastest solution uses more memory (space complexity)
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


#Solution if interviewer asks to solve without using extra memory 
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
"""