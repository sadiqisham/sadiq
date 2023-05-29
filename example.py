def reverse_str(string):
    reversed_str=""
    for char in string:
        reversed_str= char+reversed_str
    return reversed_str

input_str="Hello ALL"
reverse_it=reverse_str(input_str)
print(reverse_it)