def isPalindrome(x):
    arr = [i for i in str(x)]
    if arr == arr[::-1]:
        return True
    return False

# Test Case     
x = 121
print(isPalindrome(x))