class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum=0
        n=x
        if x<0 :
            return False
        else:
            while(x!=0):
                y=x%10
                sum=sum*10 + y
                x=x//10
        if(n==sum):
            return True
        else:
            return False
        