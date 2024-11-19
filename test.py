"""Module for performing basic arithmetic operations."""
import datetime


def divide(a: float, b: float) -> float:
    """Divide first number by second number.

    Args:
        a (float): Numerator
        b (float): Denominator

    Returns:
        float: Result of division

    Raises:
        ZeroDivisionError: If denominator is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


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

def calculate_something_with_a_very_long_name(parameter1, parameter2, parameter3, parameter4, parameter5):    
    # This line is over 99 characters and has trailing whitespace    
    result = parameter1 * parameter2 + parameter3 * parameter4 + parameter5 * (parameter1 + parameter2 + parameter3)    
    return result

if __name__ == "__main__":
    try:
        print(divide(10, 2))
    except ZeroDivisionError as e:
        print(f"Error: {e}")
