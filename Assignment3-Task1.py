def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        
def main():
    n = int(input("Enter a number: "))
    b = factorial(n)
    print("Factorial of", n, "is:", b)

main()
