import re
import openpyxl
import datetime
import time

# 打开日志文件并读取内容
with open('D:/testLog.txt', 'r',encoding='UTF-8') as f:
    logs = f.readlines()
    f.close()

# 设置时间段
start_time = '2023-03-01 00:00:00'
end_time = '2023-03-10 23:00:00'

# 定义一个字典，用于存储请求类型和URL以及它们的请求次数
req_dict = {}

# 遍历日志文件中的每一行记录
for line in logs:
    # 使用正则表达式提取出记录中的请求时间、请求类型和URL
    # pattern = r'^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'
    # match = re.search(pattern, line)
    t=time.strptime(line[0:19], '%Y-%m-%d %H:%M:%S')
    if match:
        # req_time = match.group(1)
        method, uri = match.group(2).split()
        req_status = match.group(3)
        req_size = match.group(4)

        # 如果请求时间在指定的时间段内，将请求类型和URL存储到字典中
        if start_time <= t <= end_time:
            key = (method, uri)
            if key in req_dict:
                req_dict[key] += 1
            else:
                req_dict[key] = 1

# 创建Excel表格并写入数据x
wb = openpyxl.Workbook()
ws = wb.active
ws.title = '请求汇总'

# 写入表头
ws.cell(1, 1, '请求类型')
ws.cell(1, 2, 'URL')
# ws.cell(1, 3, '请求次数')

# 遍历字典中的数据，写入Excel表格
row = 2
for key, value in req_dict.items():
    ws.cell(row, 1, key[0])
    ws.cell(row, 2, key[1])
    # ws.cell(row, 3, value)
    row += 1

# 保存Excel表格
wb.save('req_summary.xlsx')