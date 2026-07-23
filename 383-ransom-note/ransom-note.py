class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashlist=[0]*27
        for ch in magazine:
            ascii_val=ord(ch)
            index=ascii_val-97
            hashlist[index]+=1
        for ch in ransomNote:
            ascii_val=ord(ch)
            index=ascii_val-97
            if(hashlist[index]==0):
                return False
                break
            hashlist[index]-=1
        return True
        
        