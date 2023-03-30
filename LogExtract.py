import re
import datetime
from datetime import datetime,timedelta
import openpyxl


pattern=re.compile(r'\[method\s*=\s*(\w+),\s*uri\s*=\s*([^,\s]*)')
# pattern = re.compile(r'method = \'GET,\',uri = (.+)')

start_time =datetime(2022, 1, 1, 0, 0, 1)
end_time = datetime(2024, 1, 1, 0, 0, 3)

results = []
with open('D:/testLog.txt', 'r',encoding='UTF-8') as f:
    for line in f:
        log_time = datetime.strptime(line[0:19], '%Y-%m-%d %H:%M:%S')
        if start_time <= log_time <= end_time:
            match = pattern.search(line)
            while match:
                result ={
                    'method' : match.group(1),
                    'uri' : match.group(2)
                }
                results.append(result)
                if results:
                    print(results)  # 输出: [{'method': 'GET', 'uri': '/module-configs/personnel'}]

                    # 将结果写入 Excel 文件
                    wb = openpyxl.Workbook()
                    ws = wb.active
                    ws.append(['Method', 'URI'])
                    for result in results:
                        ws.append([result['method'], result['uri']])
                    wb.save('results.xlsx')
                else:
                    print('没有匹配到结果')