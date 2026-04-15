class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        rSet = set()
        for num in nums:
            if num in rSet:
                return True
            else:
                rSet.add(num)
        return False
        