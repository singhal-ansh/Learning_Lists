# Problem statement...
""" Your goal is to create a program that will take two positive integers as inputs from the user. Then the user must
choose one of the following operations for the program to execute:

composite: this will print a list of all composite (non-prime) numbers within the range of the inputs (inputs inclusive)
even: this will print a list of all even no.s within the range of inputs (inputs inclusive)
odd: this will print a list of all odd no.s wihin the range of inputs (inputs inclusive)
remove: this will remove all multiples of any number of user's choice from the range (inputs inclusive)

Note: The program should keep asking for operations until the user wants it to stop. However, it should only ask for
inputs once. """

# Solution Begins here.

# Instructions for the user...
print('In this program, you will define a range of positive no.s of your choice and then ')
print('choose from the following operations: ')

print('')  # A very important print statement that will ensure that the running program looks clean

print('''
composite: this will print a list of all composite (non-prime) numbers in your range
even: this will print a list of all even no.s in your range')
odd: this will print a list of all odd no.s in your range')
remove: this will remove all multiples of any number of your choice from the range')
end: this will end the program''')

print('')
print('')

# Taking inputs for the range
start = int(input('Enter the number with which the range will start (example: 1) : '))
end = int(input('Enter the number with which the range will end (example: 100) : '))
print('')

# storing multiple lists in variables... These will come into play later
non_prime = []
even = []
odd = []
non_multiples = []

# Getting rid of ridiculous input scenarios.
if start > end or start == end or start < 0 or end < 0:
    print('Invalid input. Please re-run the program.')
else:
    while True:  # Executing while loop to ensure program keeps asking for operation.
        operation = input('Choose operation (example: even) : ')  # asking operation from user
        print('')

        # Operation for non-prime numbers...
        if operation == "composite":
            for i in range(start, end + 1):
                if i == 1:
                    non_prime.append(i)  # Including case for '1'
                for x in range(2, i):
                    if i % x == 0:
                        non_prime.append(i)  # This statement will add desired numbers to the list
                        break
            print(f'The list of composite/non-prime numbers in your range are: ')
            print('')
            print(non_prime)
            print('')

        # Operation for even numbers...
        elif operation == 'even':
            for i in range(start, end + 1):
                if i % 2 == 0:
                    even.append(i)
            print(f'The list of even numbers in your range are: ')
            print('')
            print(even)
            print('')

        # Operation for even numbers...
        elif operation == 'odd':
            for i in range(start, end + 1):
                if i % 2 != 0:
                    odd.append(i)
            print(f'The list of odd numbers in your range are: ')
            print('')
            print(odd)
            print('')

        # Operation to remove multiples...
        elif operation == 'remove':
            num = int(input('Enter a number to remove its multiples from your range: '))
            for i in range(start, end + 1):
                if i % num == 0:  # lines 74-77 ensure that multiples of the entered number don't make it to the list
                    pass
                else:
                    non_multiples.append(i)
            print(f'The list of numbers in your range excluding the multiples of {num} are: ')
            print('')
            print(non_multiples)
            print('')
            non_multiples = []
            # This will reset the original list to avoid problems if user decides to execute this operation multiple
            # times

        # This will allow the user to stop the otherwise never-ending program.
        elif operation == 'end':
            break

        # This will ensure that the program only runs when the user types one of the listed operations.
        else:
            print('Invalid input. Please choose from the operations mentioned above.')
            print('')
