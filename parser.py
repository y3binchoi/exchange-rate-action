from datetime import datetime
import csv
import requests
from bs4 import BeautifulSoup as bs

# 오늘 날짜 구하기
# today = datetime.today().strftime("%Y%m%d")
today = datetime.today()
# today = int(today)
print(today)

# parsing
page = requests.get("https://obank.kbstar.com/quics?page=C101423")
soup = bs(page.text, "html.parser")

# #inqueryTable > table:nth-child(2) > tbody > tr:nth-child(1)
elements = soup.select('#inqueryTable > table:nth-child(2) > tbody > tr')

# 0통화코드 | 1통화이름 | 2매매기준율 | 3송금보낼때 | 4송금받을때 | 5현찰살때 | 6현찰팔때 | 7USD환산율 | 8환율변동추이바로보기
for index, element in enumerate(elements, 1):
    rows = element.select('td')  # 리스트

    currency_code = rows[0].text
    trading_base_rate = rows[2].text
    telegraphic_transfer_buying_rate = rows[3].text
    telegraphic_transfer_selling_rate = rows[4].text
    buying_rate = rows[5].text
    selling_rate = rows[6].text

    print("{}번째 통화: ".format(index))
    print("기준일시", today)
    print("통화코드", currency_code)
    print("매매기준율", trading_base_rate)
    print("송금보내실때", telegraphic_transfer_buying_rate)
    print("송금받으실때", telegraphic_transfer_selling_rate)
    print("현찰사실때", buying_rate)
    print("현찰파실때", selling_rate)

    with open('result.csv', 'a', encoding='utf-8', newline='') as f:
        tw = csv.writer(f)
        # tw.writerow(['기준일시', '통화코드', '매매기준율', '송금보내실때', '송금받으실때', '현찰사실때', '현찰파실때'])
        tw.writerow([today, currency_code, trading_base_rate, telegraphic_transfer_buying_rate,
                     telegraphic_transfer_selling_rate, buying_rate, selling_rate])
