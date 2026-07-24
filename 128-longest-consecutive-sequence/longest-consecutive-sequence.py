class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        longest = 0
        
        for num in my_set:
            if (num - 1) not in my_set:
                x = num
                count = 1
                
                # Expand the sequence as far as possible
                while (x + 1) in my_set:
                    count += 1
                    x += 1
                    
                # OUTSIDE the while loop: Update longest
                longest = max(longest, count)
                
        return longest