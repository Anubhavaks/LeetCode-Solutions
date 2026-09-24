class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for index,num in enumerate(nums):
            sum=0
            while num>0:
                rem=num%10
                sum+=rem
                num=int(num//10)
            if sum==index:
                return index
        return -1
        

