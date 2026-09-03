def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

input_string = "Cognifyz"
output = reverse_string(input_string)
print("Reverse string :", output)