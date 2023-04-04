import re
from datetime import datetime
import openpyxl,os

pattern=re.compile(r'\[method\s*=\s*(\w+),\s*uri\s*=\s*([^,\s]*)')
timePattern = re.compile(r'\s*\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}')
start_time =datetime.strptime('2023-03-09 00:00:00','%Y-%m-%d %H:%M:%S')
end_time = datetime.strptime('2023-03-11 00:00:00','%Y-%m-%d %H:%M:%S')
results = []
logPath='D:/testLog'
fileList=os.listdir(logPath)


for file in fileList:
    with open(os.path.join(logPath,file), 'r',encoding='UTF-8') as f:
        logs=f.readlines()
        for log in logs:
            match_time = timePattern.search(log)
            if match_time:
                log_time = match_time.group()
                try:
                    logTime  = datetime.strptime(log_time, '%Y-%m-%d %H:%M:%S')
                except ValueError:
                    continue
                if start_time <= logTime <= end_time:
                    match_request = pattern.search(log)
                    if match_request:
                        result ={
                            'method' : match_request.group(1),
                            'uri' : match_request.group(2)
                        }
                        results.append(result)
                        print(results)

if results:
    print(results)  # 输出: [{'method': ', 'uri': ']# 将结果写入 Excel 文件
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Method', 'URI'])
    for result in results:
        ws.append([result['method'], result['uri']])
    try:
        wb.save('results.xlsx')
    except PermissionError:
        print(f'文件保存失败：没有写入权限')
else:
    print('没有匹配到结果')