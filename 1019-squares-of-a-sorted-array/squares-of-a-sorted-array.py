class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        for num in nums:
            nums[i]=num*num
            i=i+1
        nums.sort()
        return nums
        