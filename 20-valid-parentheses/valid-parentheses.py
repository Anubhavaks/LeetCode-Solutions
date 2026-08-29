class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brac={")": "(", "}": "{", "]": "["}
        for char in s:
            if char in brac:
                top=stack.pop() if stack else '#'
                if brac[char]!=top :
                    return False
            else:
                stack.append(char)
        return True if len(stack)==0 else False
        