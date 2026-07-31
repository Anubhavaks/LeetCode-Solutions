class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        
        while left <= right:
            mid = (left + right) // 2
            
            ops = sum((balls - 1) // mid for balls in nums)
            
            if ops <= maxOperations:
                right = mid - 1
            else:
                left = mid + 1
                
        return left