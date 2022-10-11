def isPalindrome(stringOne):

    stringOne = stringOne.replace(" ", "")
    stringOne = stringOne.lower()

    letterTable = {}

    for n in range( len(stringOne) ):
        letterTable[stringOne[n]] = 1 + letterTable.get(stringOne[n], 0)

    odd_count = 0

    for k, v in letterTable.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 and odd_count != 0:
            return False

    return True




string_One = "Tact Coa"
print("\n")
print(string_One)
value = isPalindrome(string_One)
print("Is Palindrome?")
print(value)
print("\n")