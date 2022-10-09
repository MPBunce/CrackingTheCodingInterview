class AnimalShelter(object):

    def __init__(self):
        self.dogs = []
        self.cats = []
        self.place_in_line = 0

    def enqueue(self, name, type):
        if type == "DOG":
            self.place_in_line += 1
            self.dogs.append([name , self.place_in_line])

        elif type == "CAT":
            self.place_in_line += 1           
            self.cats.append([name , self.place_in_line])

        else:
            print("Only dogs and cats my guy")


    def dequeueOldest(self):
        oldDog = self.dogs[0][1]
        oldCat = self.cats[0][1]

        if oldCat < oldDog:
            self.cats.pop(0)
        else:
            self.dogs.pop(0)

    def dequeueDog(self):
        self.dogs.pop(0)

    def dequeueCat(self):
        self.cats.pop(0)

    def display(self):
        print("Dogs:")
        print(self.dogs)

        print("Cats:")
        print(self.cats)

#Main Driver Code
myShelter = AnimalShelter()
myShelter.enqueue("spot", "CAT")
myShelter.enqueue("mittens", "CAT")
myShelter.enqueue("Fluffers", "CAT")
myShelter.enqueue("Duke", "DOG")
myShelter.enqueue("Buddy", "DOG")
myShelter.enqueue("Barker", "DOG")
myShelter.display()
myShelter.dequeueCat()
myShelter.dequeueDog()
myShelter.display()
myShelter.dequeueOldest()
myShelter.display()