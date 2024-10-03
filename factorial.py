'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
'''
def is_factorial_number(n):
    if n < 0:
        return False  # Factorials are not defined for negative numbers
    
    factorial = 1
    i = 1
    
    # Compute the factorial iteratively until it exceeds n
    while factorial < n:
        i += 1
        factorial *= i
    
    # Check if the computed factorial is equal to n
    return factorial == n

# Input: Read an integer from the user
n = int(input("Enter an integer:\n"))

# Check if n is a factorial number and print the result
if is_factorial_number(n):
    print("Yes")
else:
    print("No")
