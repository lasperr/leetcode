def addTwoNumbers(l1, l2):
    # revert the list
    rev1, rev2 = l1[::-1], l2[::-1]
    # convert into str list
    str1, str2 = [str(item) for item in rev1], [str(item) for item in rev2]
    # convert into int
    a_str1, a_str2 = "".join(str1), "".join(str2)
    digit1, digit2 = int(a_str1), int(a_str2)
    # sum
    resInt = digit1 + digit2
    # convert int into list
    resList = [i for i in str(resInt)]
    return list(map(int, resList))
# Test Case
l1 = [2, 4, 3]
l2 = [5, 6, 4]
print(addTwoNumbers(l1, l2))