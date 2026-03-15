# Function to print fibonacci series
def print_fib(n):
    if n < 1:
        print("Invalid Number of terms")
        return

    # When number of terms is greater than 0
    prev1 = 1
    prev2 = 0

    print(prev2, end=" ")

    # If n is 1, then we do not need to
    # proceed further
    if n == 1:
        return

    print(prev1, end=" ")
    
    # Print 3rd number onwards using
    # the recursive formula
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
        print(curr, end=" ")

# Driver code
if __name__ == "__main__":
    n = 9
    print_fib(n)