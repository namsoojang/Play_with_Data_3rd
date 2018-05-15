import requests
from bs4 import BeautifulSoup

print("## 검색어를 입력하시오. ")
keyword = input()

PAGES = 5

for page in range(1, PAGES + 1):
    print("page : ", page, "----------------------------------------------------")
    url = "https://www.diningcode.com/list.php?page=" + str(page) + "&query=" + keyword
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    restaurant_names = soup.findAll("div", {"class": "dc-restaurant-name"})
    for restarant in restaurant_names:
        print("\t", restarant.text.strip())
