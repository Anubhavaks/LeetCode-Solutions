class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        set={'a','e','i','o','u'}
        count=0
        for i in range(k):
            if s[i] in set:
                count+=1
        ans=count
        for i in range(k,len(s)):
            if s[i] in set:
                count+=1
            if s[i-k] in set:
                count-=1
            ans=max(ans,count) 
        return ans      