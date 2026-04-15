class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sortS = "".join(sorted(s))
        sortT = "".join(sorted(t))

        for s in range(len(sortS)):
            if sortS[s] != sortT[s]:
                return False

        return True 

        