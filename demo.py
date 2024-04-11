import PenroseArray as pa

#Slightly modified binary search to include the creation of penrose arrays
def binary_search(nums, target):
    penrose = pa.PenroseArray()
    #Just so the original array is not changed
    copy = nums
    #For naming the penrose substance file
    i = 0
    while len(copy) >= 1:
        penrose.array = copy
        penrose.penrose_binary_search("substance/binary_search"+str(i)+".substance")
        mid = len(copy)//2
        if copy[mid] == target:
            return nums.index(copy[mid])
        elif copy[mid] < target:
            copy = copy[mid+1:]
        else:
            copy = copy[:mid]
        i+=1
    
    return -1

#Generic array based stack for the demonstration
class Stack:
    def __init__(self):
        self.arr = []

    def pop(self):
        if len(self.arr) <= 0:
            raise ValueError("Cannot pop empty stack")
        return self.arr.pop(len(self.arr) - 1)
    
    def push(self, value):
        self.arr.append(value)
    
def main():
    default = [12,20,50,60]
    array = pa.PenroseArray(default)
    array.generate_substance("substance/array.substance")

    #Create a stack and push a series of numbers
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(50)
    stack.push(90)
    #Create some substance files for binary search
    x = binary_search(stack.arr,50)
    #Create a penrose array for the stack
    ps = pa.PenroseArray(stack.arr)
    #Create a substance
    #If you use the roger trio command line interface, you can create the 
    ps.penrose_stack("substance/stack0.substance")
    #Pop
    y = stack.pop()
    #Create another substance
    ps.array = stack.arr
    ps.penrose_stack("substance/stack1.substance")

main()