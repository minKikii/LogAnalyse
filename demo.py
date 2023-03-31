import re
import datetime
# pattern = re.compile(r'(?<=method = ).*?(?=,)')
# pattern = re.compile(r'method = (\w+) uri (\w+)')
# pattern=re.compile(r'(?<=method = )(\w+), uri = (\S+)')
# pattern=re.compile(r'\[method\s*=\s*(\w+),\s*uri\s*=\s*(\S+)')
# pattern = re.compile(r'^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}\.\d{3})\s+\[(.*?)\]\s+(\S+)\s+(.*?)$')
# # print('2023-03-10 00:00:00.002 - delete basic data cache [method = GET, uri = /module-configs/personnel/villager-schema,')
# s=pattern.search('2023-03-10 00:00:00.002 [scheduling-1] INFO c.a.q.s.handler.ClientIndexStatisticHandler - delete basic data cache 2023-03-10 00:00:00.014 [scheduling-1] INFO org.ehcache.core.EhcacheManager - C[method = GET, uri = /module-configs/personnel/point-card, Azale method')

# if s:
# print(s.group(5))

timePatten = re.compile(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\d{3}')
with open('D:/testLog.txt', 'r',encoding='UTF-8') as f:
    logs = f.readlines()
    for log in logs:
        time_match=timePatten.search(log)
        if time_match:
            log_time = time_match.group()
            logTime  = datetime.strptime(log_time, '%Y-%m-%d %H:%M:%S.%f')
            print(logTime)

