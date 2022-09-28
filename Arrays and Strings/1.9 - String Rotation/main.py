def stringRotation(s, goal):

    if(len(s) != len(goal)):

        return False

    for i in range(len(s)):
        s = s[1:]+s[0] #Rotate the string by 1 element
        
        if(s==goal): #Compare the string with goal.
            return True
    return False



one = "waterbottle"
two = "tlewaterbot"

print("Are they rotated?\n")
value = stringRotation(one, two)
print(value)