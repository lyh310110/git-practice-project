"""
计算器模块
提供基本的数学运算功能
"""

class Calculator:
    """简单的计算器类"""
    
    def add(self, a, b):
        """加法运算"""
        return a + b
    
    def subtract(self, a, b):
        """减法运算"""
        return a - b
    
    def multiply(self, a, b):
        """乘法运算"""
        return a * b
    
    def divide(self, a, b):
        """除法运算"""
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

def calculate_expression(expression):
    """计算字符串表达式（简单版本）"""
    try:
        return eval(expression)
    except Exception as e:
        return f"计算错误: {e}"