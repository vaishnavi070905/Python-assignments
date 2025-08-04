from math import *

def main():
    num = float(input("Enter a number: "))

    if num < 0:
        print("Square root and natural logarithm are not defined for negative numbers.")
    elif num == 0:
        print("Square root of 0 is: 0.0")
        print("Natural logarithm is not defined for 0.")
        print(f"Sine of {num} radians is: {sin(num)}")
    else:
        square_root = sqrt(num)
        logarithm = log(num)
        sine = sin(num)

        print("Square root : ",square_root)
        print("Logarithm: ",logarithm)
        print("Sine: ",sine)

main()
