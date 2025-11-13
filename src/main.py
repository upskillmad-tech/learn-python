def main():
    print("Hello from learn-python!")


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    main()
    print(f"adding 2 and 3 is {add(2, 3)}")
    print(f"subtracting 5 from 3 is {subtract(5, 3)}")
    print(f"multiplying 4 and 2 is {multiply(4, 2)}")
    print(f"dividing 8 by 2 is {divide(8, 2)}")
