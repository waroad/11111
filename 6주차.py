import bs4
import requests

headers = {
    'User-Agent': 'Not_Crawling X)'
}

response = requests.get('https://kin.naver.com/',headers=headers).text
soup=bs4.BeautifulSoup(response, 'html.parser')

ranks = soup.select('#rankingChart > ul > li')

with open('kin_trend.csv','w') as f:
    for rank in ranks:
        num = rank.select_one('span.no').text
        title = rank.select_one('a.ranking_title').text
        f.write(f'{num},{title}\n')