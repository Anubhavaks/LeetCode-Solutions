class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k=len(needle)
        if (len(haystack)<k):
            return -1
        ans=[]
        for i in range(k):
            ans.append(haystack[i])
        left=0
        right=k
        if needle==("".join(ans)):
            return 0
        while right<len(haystack):
            ans.append(haystack[right])
            ans.pop(0)
            if needle==("".join(ans)):
                return left+1
            left+=1
            right+=1
        return -1

        