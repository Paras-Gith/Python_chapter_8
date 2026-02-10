# Iterables = An object/collection that can return its elements one at a time, allowing it to be iterated
# over in a loop

# n = [1, 2, 3, 4, 5]

# for number in n:
#     print(number)

# n = (1, 2, 3, 4, 5)   #tuple

# fruits = {"apple", "ornage", "banana", "coconut"}   #set

# name = "team rtc"    #string


my_dictionary = {"A":1,"b":2,"c":3}


# for key in (my_dictionary):
#     print(key, end=" ")

for key,value in my_dictionary.items():
    print(f"{key} = {value}") 