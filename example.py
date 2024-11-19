"""Module for basic arithmetic operations."""


def add_numbers(num1: float, num2: float) -> float:
    """Add two numbers together.

    Args:
        num1 (float): First number to add
        num2 (float): Second number to add

    Returns:
        float: Sum of the two numbers
    """
    return num1 + num2


if __name__ == "__main__":
    print(add_numbers(1, 2))
