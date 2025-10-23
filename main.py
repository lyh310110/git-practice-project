#!/usr/bin/env python3
"""
Main program entry file
Demo Git workflow basic project
"""

from calculator import Calculator, calculate_expression
from utils import get_current_time, format_number, save_to_file, load_from_file
import config

def demo_calculator():
    """Demo calculator functions"""
    calc = Calculator()
    print(f"\nCalculator Demo:")
    print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
    print(f"Subtraction: 10 - 4 = {calc.subtract(10, 4)}")
    print(f"Multiplication: 6 x 7 = {calc.multiply(6, 7)}")
    print(f"Division: 15 / 3 = {calc.divide(15, 3)}")

def demo_utils():
    """Demo utility functions"""
    print(f"\nUtility Functions Demo:")
    print(f"Current Time: {get_current_time()}")
    print(f"Formatted Number: 1234567 -> {format_number(1234567)}")
    
    # Demo file operations
    test_data = {"project": config.PROJECT_NAME, "timestamp": get_current_time()}
    if save_to_file("test_data.json", test_data):
        print("Data saved successfully")
        loaded_data = load_from_file("test_data.json")
        print(f"Loaded data: {loaded_data}")

def show_config():
    """Show configuration info"""
    print(f"\nProject Configuration:")
    print(f"Project Name: {config.PROJECT_NAME}")
    print(f"Version: {config.VERSION}")
    print(f"Author: {config.AUTHOR}")
    print(f"Debug Mode: {'Enabled' if config.DEBUG else 'Disabled'}")

def main():
    print("=== Git Practice Project ===")
    print("Project started successfully!")
    print("This is a complete example project demonstrating Git workflow")
    
    # Demo all module functions
    demo_calculator()
    demo_utils()
    show_config()
    
    print(f"\nAll demos completed successfully!")

if __name__ == "__main__":
    main()