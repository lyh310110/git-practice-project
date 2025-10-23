"""
工具函数模块
提供各种辅助功能
"""

import datetime
import json

def get_current_time():
    """获取当前时间"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_to_file(filename, data):
    """保存数据到文件"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            if isinstance(data, dict):
                json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                f.write(str(data))
        return True
    except Exception as e:
        print(f"保存文件失败: {e}")
        return False

def load_from_file(filename):
    """从文件加载数据"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                return content
    except FileNotFoundError:
        return None

def format_number(number):
    """格式化数字显示"""
    return f"{number:,}"