class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open=0
        close=0
        for char in s:
            if char=='(':
                close+=1
            else:
                if close>0:
                    close-=1
                else:
                    open+=1
        return open+close


        