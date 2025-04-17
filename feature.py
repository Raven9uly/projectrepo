# feature.py

def add_numbers(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: The sum of a and b
    """
    return a + b

# Example usage
if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum is: {result}")