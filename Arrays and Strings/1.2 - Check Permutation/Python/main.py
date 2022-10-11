def isAnagram(stringOne, stringTwo):
    
    letterTable = {}

    for n in range( len(stringOne) ):
        letterTable[stringOne[n]] = 1 + letterTable.get(stringOne[n], 0)
        letterTable[stringTwo[n]] = -1 + letterTable.get(stringTwo[n], 0)

    for val in letterTable:
        if letterTable[val] > 0:
            return False

    return True

#d[key] = d.get(key, value)


one = "apple"
two = "pplse"

value = isAnagram(one, two)

print("Is permutation?: ")
print(value)