class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        result = int(''.join([str(num) for num in digits]))
        result=result+1
        digits=list(map(int, str(result)))
        return digits
        