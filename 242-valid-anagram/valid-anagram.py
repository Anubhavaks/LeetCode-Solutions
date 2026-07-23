class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashlist=[0]*27
        hashlist2=[0]*27
        i=0
        for ch in s:
            ascii_val=ord(ch)
            index=ascii_val-97
            hashlist[index]+=1
        for ch in t:
            ascii_val=ord(ch)
            index=ascii_val-97
            hashlist2[index]+=1
        while(i<27):
            if(hashlist[i]==hashlist2[i]):
                i=i+1
            else:
                return False
                break
        return True
        
        