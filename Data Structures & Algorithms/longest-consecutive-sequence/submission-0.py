class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setS = set(nums)

        longS = 0 
        
        for num in setS:
            if (num - 1) not in setS:
                currLen = 1
                while (num + currLen) in setS:
                    currLen += 1
                longS = max(longS, currLen)
        
        return longS