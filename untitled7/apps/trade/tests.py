import requests
import json
s=requests.get('https://p.3.cn/prices/mgets?type=1&skuIds=5918213')
a=s.text.split('[')[1].split(']')[0]
s=json.loads(a)
print(s)
s = requests.get('http://127.0.0.1:8000/a/')
print(s.text)