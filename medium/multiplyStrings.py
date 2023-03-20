def multiply(num1, num2):
    a_num1, a_num2 = "".join(num1), "".join(num2)
    product = int(a_num1) * int(a_num2)
    return str(product)
# Test Case
num1 = "123"
num2 = "456"
print(multiply(num1, num2))