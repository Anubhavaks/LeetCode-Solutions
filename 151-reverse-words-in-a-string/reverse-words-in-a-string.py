class Solution:
    def reverseWords(self, s: str) -> str:
        i=0
        p_list=s.split()
        left=0
        right=len(p_list)-1
        while(left<right):
            p_list[left],p_list[right]=p_list[right],p_list[left]
            left+=1
            right-=1
        s=" ".join(p_list)
        return s
        



        