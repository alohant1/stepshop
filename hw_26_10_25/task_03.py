"""
Напишите программу, в которой разбивается строка по нескольким разделителям.
"""
import re

pat = r'[tea]'
result = re.split(pat, 'though the idiocrasy to which extent it can be called thinking')
print(result)
