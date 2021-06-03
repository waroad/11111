import bs4
import requests

headers = {
    'User-Agent': 'Not Crawling X'
}
response = requests.get('https://kin.naver.com/', headers=headers).text
soup = bs4.BeautifulSoup(response, 'html.parser')
trends = soup.select('#rankingChart > ul > li')

with open('kin_trend.csv', 'w') as file:
    file.write("순위, 이름\n")
    for trend in trends:
        file.write(f'{int(trend.select_one("span.no").text)}위, {trend.select_one("a.ranking_title").text}\n')
