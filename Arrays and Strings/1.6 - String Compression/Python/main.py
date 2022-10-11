def stringComp(stringOne):
    
    letterTable = {}
    compressedString = []

    for n in range( len(stringOne) ):
        letterTable[stringOne[n]] = 1 + letterTable.get(stringOne[n], 0)
    
    for k, v in letterTable.items():
        compressedString.append(k)
        compressedString.append(v)

    compressedString = "".join(map(str, compressedString))

    return compressedString


string = "aabbbbbbccd"

value = stringComp(string)

print(value)
