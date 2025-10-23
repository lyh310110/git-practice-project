"""
Utility Functions Module
Provides various helper functions
"""

import datetime

def get_current_time():
    """Get current time"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def format_number(number):
    """Format number display"""
    return f"{number:,}"

def calculate_area(radius):
    """Calculate circle area"""
    return 3.14159 * radius * radius

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32