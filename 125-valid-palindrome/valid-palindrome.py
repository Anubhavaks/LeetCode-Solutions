class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        str=''.join(char.lower() for char in s if char.isalnum())
        r=len(str)-1
        while(l<=r):
            if str[l]==str[r]:
                l+=1
                r-=1
            else:
                return False
        return True
