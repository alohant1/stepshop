"""
Напишите программу, в которой извлекаются слова, начинающиеся на гласную букву.
"""

import re

matched = re.findall(r'\s[eayuio]+[a-zA-Z0-9.-]+\b', ' astronomically, biblically, cronically, directly, erraticly, ortopedically')
print(matched)
