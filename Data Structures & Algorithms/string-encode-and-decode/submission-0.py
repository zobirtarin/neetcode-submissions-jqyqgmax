class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "_" + s 
        return output
        

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "_":
                j += 1
            lengthS = int(s[i:j])
            word = s[j + 1 : j + 1 + lengthS]
            output.append(word)
            i = j + 1 + lengthS
            
        return output

