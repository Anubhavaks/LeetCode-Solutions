class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        f={}
        i=1
        temp=0
        for num in nums :
            f[num]=f.get(num,0)+1
        while temp<=100:
            temp=k*i
            if temp in f:
                i+=1
            else:
                return temp
            

        