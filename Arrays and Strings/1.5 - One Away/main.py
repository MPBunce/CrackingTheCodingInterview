def isOneAway(stringOne, stringTwo):
    
    letterTable = {}

    for n in range( len(stringOne) ):
        letterTable[stringOne[n]] = 1 + letterTable.get(stringOne[n], 0)


    for n in range( len(stringTwo) ):

        letterTable[stringTwo[n]] = -1 + letterTable.get(stringTwo[n], 0)

    count = 0

    for val in letterTable:

        if letterTable[val] < 0:
            count += 1


    if count == 1:
        return True

    return False

s1 = "pales"
s2 = "pales"

value = isOneAway(s1, s2)

print(value)

