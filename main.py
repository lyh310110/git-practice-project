#!/usr/bin/env python3
"""
主程序入口文件
演示 Git 工作流程的基础项目
"""

from calculator import Calculator, calculate_expression

def main():
    print("=== Git 实践项目 ===")
    print("项目启动成功！")
    print("这是一个演示 Git 工作流程的示例项目")
    
    # 演示计算器功能
    calc = Calculator()
    print(f"\n计算器演示:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")

if __name__ == "__main__":
    main()