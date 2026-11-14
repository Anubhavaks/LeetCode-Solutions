class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Edge case: empty list
        if not nums:
            return 0
            
        l = 0  # Points to the last unique element we've seen
        
        # r scans through the array looking for new unique elements
        for r in range(1, len(nums)):
            
            # If we find a number different from the last unique one
            if nums[r] != nums[l]:
                l += 1             # Move the writer forward
                nums[l] = nums[r]  # Overwrite the duplicate with the new unique number
        return l + 1