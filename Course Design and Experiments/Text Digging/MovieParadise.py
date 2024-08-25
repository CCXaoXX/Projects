# MovieParadise

import requests
import bs4
import pandas as pd
from tqdm import *


def get_data(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except requests.HTTPError as e:
        print(e)
        print("HTTPError")
    except requests.RequestException as e:
        print(e)
    except:
        print("Unknown Error")


def parse_data(html):
    bsobj = bs4.BeautifulSoup(html, 'html.parser')
    info = []
    tbList = bsobj.find_all('table', attrs={'class': 'tbspan'})
    for item in tbList:
        movie = []
        link = item.b.find_all('a')[1]
        name = link["title"]
        url = 'https://www.dy2018.com' + link["href"]
        movie.append(name)
        movie.append(url)
        try:
            temp = bs4.BeautifulSoup(get_data(url), 'html.parser')
            tbody = temp.find_all('tbody')
            for i in tbody:
                download = i.a.text
                movie.append(download)
            info.append(movie)
            print(movie)
        except Exception as e:
            print(e)
    return info


def save_data(data):
    filename = 'E:/片片.csv'
    dataframe = pd.DataFrame(data)
    dataframe.to_csv(filename, mode='a', index=False, sep=',', header=False)


def main():
    for page in tqdm(range(1, 100)):
        print('正在爬取：第' + str(page) + '页')
        if page == 1:
            index = 'index'
        else:
            index = 'index_' + str(page)
        url = 'https://www.dy2018.com/html/bikan/' + index + '.html'
        html = get_data(url)
        movies = parse_data(html)
        save_data(movies)
        print('第' + str(page) + '页完成！')


if __name__ == '__main__':
    print('爬虫启动完成！')
    main()
    print('爬虫执行完成！')
