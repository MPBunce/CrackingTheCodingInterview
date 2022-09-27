def isUnique(string):

    hashset = set()
    
    for n in string:
        if n in hashset:

            #if letter is already in set return False, there are duplicates
            return False
        
        hashset.add(n)

    #else True   
    return True

#Testing
theString = "hut"
value = isUnique(theString)
print("\n")
print(value)
print("\n")

#Do this without making another data type

def isUniqueTwo(string):

    hashset = set()
    
    for i in range(len(string)):
        for j in range( i+1, len(string) ):
            if( string[i] == string[j] ):
                return False

    #else True   
    return True

theString = "hut"
value = isUniqueTwo(theString)
print("Two\n")
print(value)
print("\n")