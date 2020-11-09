import requests
from bs4 import BeautifulSoup

url = 'https://yugioh.fandom.com/es/wiki/'

url2 = 'Categor%C3%ADa:Carta'

while True:
    req = requests.get(url+url2)

    soup = BeautifulSoup(req.text,'html.parser')

    div_category_page__members = soup.find('div',class_='category-page__members')

    __members_for_char = div_category_page__members.find_all('li',class_='category-page__member')
    with open('cards_path.txt','a') as f:
        for link in __members_for_char:
            link_href = link.a['href']
            f.write(link_href + '\n')

    div_category_page__pagination = soup.find('div',class_='category-page__pagination')

    __pagination_next = div_category_page__pagination.find('a',class_='category-page__pagination-next')

    if __pagination_next is not None:

        link_by_str = str(__pagination_next['href'])
        index_path = link_by_str.index('Categor')
        url2 = link_by_str[index_path:]
    else:
        print('finalizado')
        break




