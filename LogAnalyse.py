import re,os
from datetime import datetime
import openpyxl
from collections import defaultdict, Counter


logPath='D:/testLog'
fileList=os.listdir(logPath)
# 定义正则表达式
time_regex = re.compile(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}')

# 读取日志文件
for file in fileList:
    with open(os.path.join(logPath,file), 'r',encoding='utf-8') as f:
        logs = f.readlines()

# 定义时间段
start_time =datetime.strptime('2023-03-09 00:00:00','%Y-%m-%d %H:%M:%S')
end_time = datetime.strptime('2023-03-11 00:00:00','%Y-%m-%d %H:%M:%S')

# 定义字典，用于存储分类后的日志记录
logs_dict = defaultdict(int)

# 遍历日志文件中的每一行记录
for log in logs:
    # 使用正则表达式匹配时间
    time_match = time_regex.search(log)
    if time_match:
        date_str = time_match.group()
        # 将字符串类型的时间转换成 datetime.datetime 类型的对象
        date_obj = datetime.strptime(date_str,  '%Y-%m-%d %H:%M:%S')
        # 判断时间是否在指定的时间段内
        if start_time <= date_obj <= end_time:
            # 使用正则表达式匹配请求类型和 URL
            match_result = re.search(r'\[method\s*=\s*(\w+),\s*uri\s*=\s*([^,\s]*)', log)
            if match_result:
                # 获取请求类型和 URL
                method = match_result.group(1)
                url = match_result.group(2)
                # 将 URL 中的数字替换为 ID
                url_new = re.sub(r'/(\d+)', '/id', url)
                # 将请求类型和 URL 作为键，增加请求次数
                logs_dict[(method, url_new)] += 1
                # print(url_new)
                print(logs_dict)

# 将结果输出到 Excel 文件中
wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'Logs'

ws.append(['method','url','count'])
for (method,url),count in logs_dict.items():
    ws.append([method, url, count])

# 保存 Excel 文件
try:
    wb.save('results.xlsx')
except PermissionError:
        print(f'文件保存失败：没有写入权限')
else:
    print('没有匹配到结果')