class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        curr = strs[0]
        for word in strs[1:]:
            i = 0
            temp = ""
            while i< len(word) and i<len(curr) and word[i]==curr[i]:
                temp+=curr[i]
                i+=1
            curr = temp
        return curr
        