class MinStack:

    def __init__(self):
        self.items=[]
        

    def push(self, value: int) -> None:
        if not self.items:
            self.items.append((value,value))
        else:
            curr=self.items[-1][1]
            minim=min(value,curr)
            self.items.append((value,minim))

        

    def pop(self) -> None:
        if len(self.items)==0:
            return "cannot pop,stack is empty"
        x=self.items.pop()
        return x
        

    def top(self) -> int:
        if len(self.items)==0:
            return "stack is empty"
        return self.items[-1][0]
        

    def getMin(self) -> int:
        return self.items[-1][1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()