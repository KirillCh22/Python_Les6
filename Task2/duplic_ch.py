
def duplicate_chars(string: str):

    result = [string[0]]
    duplicate_val = string[0]
    count = 0

    if string == "":
        return ""

    else:
        for i in range(len(string)):
            if string[i] == duplicate_val:
                count += 1
            else:
                result.append(string[i])
                duplicate_val = string[i]




    return ''.join(result)