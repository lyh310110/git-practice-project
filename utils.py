"""
Utility Functions Module
Provides various helper functions
"""

import datetime
import json

def get_current_time():
    """Get current time"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def save_to_file(filename, data):
    """Save data to file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            if isinstance(data, dict):
                json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                f.write(str(data))
        return True
    except Exception as e:
        print(f"Failed to save file: {e}")
        return False

def load_from_file(filename):
    """Load data from file"""
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
    """Format number display"""
    return f"{number:,}"