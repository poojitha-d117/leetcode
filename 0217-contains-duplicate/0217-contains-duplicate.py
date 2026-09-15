class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            if len(nums)!=len(set(nums)):
                return True
            else:
                return False