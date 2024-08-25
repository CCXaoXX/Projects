import requests
keyword = "python"
try:
    kv = {'wd':keyword}
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(r.text[1000:2000])
except:
    print("爬取失败")
    

