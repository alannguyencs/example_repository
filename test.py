"""Module for performing basic arithmetic operations."""
import datetime


def divide(numerator: float, denominator: float) -> float:
    """Divide first number by second number.

    Args:
        numerator (float): Numerator
        denominator (float): Denominator

    Returns:
        float: Result of division

    Raises:
        ZeroDivisionError: If denominator is zero
    """
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return numerator / denominator


def date_to_string(year: int, month: int, day: int):
    """Convert date to formatted string.

    Args:
        year (int): Year value
        month (int): Month value (1-12)
        day (int): Day value

    Returns:
        str: Formatted date string (e.g., 'Monday January, 1 2024')
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    day_name = days[datetime.date(year, month, day).weekday()]
    month_name = months[month - 1]  # Subtract 1 since months list is 0-indexed

    return f"{day_name} {month_name}, {day} {year}"


def calculate_something(param1, param2, param3, param4, param5):
    """Calculate result using the given parameters.

    Args:
        param1: First parameter
        param2: Second parameter
        param3: Third parameter
        param4: Fourth parameter
        param5: Fifth parameter

    Returns:
        Result of calculation
    """
    result = (
        param1 * param2
        + param3 * param4
        + param5 * (param1 + param2 + param3)
    )
    return result


# add some comments
if __name__ == "__main__":
    try:
        print(divide(10, 2))
    except ZeroDivisionError as e:
        print(f"Error: {e}")
