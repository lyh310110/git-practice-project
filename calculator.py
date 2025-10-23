"""
Calculator Module
Provides basic math operations
"""

class Calculator:
    """Simple calculator class"""
    
    def add(self, a, b):
        """Addition operation"""
        return a + b
    
    def subtract(self, a, b):
        """Subtraction operation"""
        return a - b
    
    def multiply(self, a, b):
        """Multiplication operation"""
        return a * b
    
    def divide(self, a, b):
        """Division operation"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def calculate_expression(expression):
    """Calculate string expression (simple version)"""
    try:
        return eval(expression)
    except Exception as e:
        return f"Calculation error: {e}"