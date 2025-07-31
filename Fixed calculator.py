def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y  # Fixed logic bug

def add(x, y):
    return x + y

def main():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("Sum:", add(a, b))
        print("Difference:", subtract(a, b))
        print("Product:", multiply(a, b))
        print("Quotient:", divide(a, b))

    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    main()
