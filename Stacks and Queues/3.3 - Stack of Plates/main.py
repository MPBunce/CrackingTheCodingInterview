class DinnerPlates(object):
    
    def __init__(self, capacity):
        self.stacks = []
        if capacity < 1:
            print("Must have a capacity greater than 1")
        else:
            self.capacity = capacity

    def push(self, item):
        if self.stacks == []:
            self.stacks.append([item])

        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def pop(self, index):
        if self.stack == []:
            raise NameError("Cant pop an empty stack")
        else: 
            popped_data = self.stack[-1][-1]

            if len(self.stacks[-1]) == 1:
                del self.stakcs[-1]
            else:
                del self.stacks[-1][-1]

        print("popped value:")
        print(popped_data)

    def display(self):
        for n in self.stacks:
            print(n)

    def popAt(self, index):
        if self.stakcs == []:
            raise NameError("Cant pop an empty stack")
        elif index-1 > len(self.stacks):
            raise NameError("Out or range")
        else: 
            popped_data = self.stacks[index-1][-1]

        

plates = DinnerPlates(3)
plates.push(1)
plates.push(3)
plates.push(4)
plates.push(8)
plates.push(12)
plates.push(19)

plates.display()