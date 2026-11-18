fib_range = int(input("What number would you like to try Fibonnaci series on? "))

if fib_range <= 0:
    print("Sorry, number out of range")
else:
    first_number = 0
    second_number = 1
    for i in range(fib_range):
        print(first_number)
        next_number = first_number + second_number

        first_number = second_number
        second_number = next_number
