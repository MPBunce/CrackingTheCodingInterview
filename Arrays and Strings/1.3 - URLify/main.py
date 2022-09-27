def url_ify(string):
    
    result = []

    for i in range(len(string)):
        if string[i] == " ":
            result.append("%20")
            i += 1
        else:
            result.append(string[i])

    result = "".join(result)

    return result


string = "this is a test string"
value = ""
value = url_ify(string)

print("\nString before:")
print(string)
print("String after:")
print(value)
print("\n")

#replace(',', ' ')