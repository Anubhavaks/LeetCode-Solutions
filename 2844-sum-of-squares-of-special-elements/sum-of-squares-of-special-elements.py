class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        sum=0
        for i in range(n):
            l=i+1
            if n%l==0 :
                sum+=(nums[i]*nums[i])
        return sum
        