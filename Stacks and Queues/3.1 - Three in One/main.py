#implement 3 stacks in an array 
#Future work make it n stacks of m size
class Stacks:

    def __init__(self, sizeOfEachStack):
        #numbers of stacks
        arrayCapacity = 3 * sizeOfEachStack
        self.items = [0] * arrayCapacity
        self.start = [0, (arrayCapacity // 3), 2 * (arrayCapacity // 3)]
        self.end = [(arrayCapacity // 3), 2 * (arrayCapacity // 3), arrayCapacity]
        
    def push(self, stack, val):
        print(stack)
        print(val)
        print("Rest:")
        print(self.start[stack])
        print(self.items[self.start[stack]])
        self.items[self.start[stack]] = val
        print("Setting Vals")
        print(self.start[stack])
        print(self.items[self.start[stack]])
        self.start[stack] += 1
        print(self.start[stack])

    def pop(self, stack):
        
        top = self.start[stack] - 1
        item = self.items[top]
        self.items[top] = None
        self.start[stack] = top
        print("popped item:")
        print(item)

    def display(self):
        print(self.items)

a = Stacks(3)
a.push(0, 10)
a.display()
a.push(0, 12)
a.display()
a.push(1, 110)
a.display()
a.push(1, 112)
a.display()
a.push(1, 812)
a.display()

a.push(2, 12)
a.display()

a.push(2, 69)
a.display()
a.push(2, 69)
a.display()

a.pop(2)
a.display()