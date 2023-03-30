import re

# pattern = re.compile(r'(?<=method = ).*?(?=,)')
# pattern = re.compile(r'method = (\w+) uri (\w+)')
# pattern=re.compile(r'(?<=method = )(\w+), uri = (\S+)')
pattern=re.compile(r'\[method\s*=\s*(\w+),\s*uri\s*=\s*(\S+)')
print('2023-03-10 00:00:00.002 - delete basic data cache [method = GET, uri = /module-configs/personnel/villager-schema,')
s=pattern.search('2023-03-10 00:00:00.002 - delete basic data cache [method = GET, uri = /module-configs/personnel/villager-schema,')

# if s:
print(s.group(1))
print(s.group(2))
# else:
#     print('没有匹配到结果')
# print('')

