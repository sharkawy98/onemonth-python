#######
# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".
#######

for i in range(1,101):    
    is_module_3 = True if i % 3 == 0 else False
    is_module_5 = True if i % 5 == 0 else False

    if is_module_3 and is_module_5:
        print("FizzBuzz")
    elif is_module_3:
        print("Fizz")
    elif is_module_5:
        print("Buzz")
    else:
        print(i)
