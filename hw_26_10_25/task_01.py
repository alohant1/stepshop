"""
Напишите программу, в которой возвращаются домены из списка e-mail адресов
"""
import re

found = re.findall(r'@([a-zA-Z0-9.-]+)', 'what@idk.com, @idk.etc, @etc.com, @inbox.ru, @gmail.com')
print(found)
