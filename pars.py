import requests
from bs4 import BeautifulSoup


json_data = {
    "rub": "valyuty/usd-rub",
    "gas": "birzhevyye-tovary/gaz-cena",
    "oil": "birzhevyye-tovary/neft-cena",
    "gold": "birzhevyye-tovary/zoloto-cena"
}

# Цены на нефть, газ, золото, доллар
def get_price(object_info):
    global json_data
    r = requests.get(f"https://www.finanz.ru/{json_data[object_info]}").text

    soup = BeautifulSoup(r, 'lxml')
    main_table = soup.find('div', {"class":"pricebox"}).find('div', {"class":"content"}).find('table')
    price = main_table.find('th').text
    return price



def req_and_soup(url):
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'lxml')
    return soup

# Газ
# https://1prime.ru/gas/
def pars_gaz():
    soup = req_and_soup('https://1prime.ru/gas/')

    card = []
    news = soup.find_all('article', {'class': 'rubric-list__article rubric-list__article_default'})
    for new in news:
        title_and_link = new.find('h2', {'class': 'rubric-list__article-title'})
        title = title_and_link.text
        link = 'https://1prime.ru' + title_and_link.find('a').get('href')
        card.append(f'{title},: {link}')
    print(card)
    return card[:3]



# https://1prime.ru/oil/
# нефть
def pars_prime():
    soup = req_and_soup('https://1prime.ru/oil/')

    card = []
    news = soup.find_all('article', {'class': 'rubric-list__article rubric-list__article_default'})
    for new in news:
        title_and_link = new.find('h2', {'class': 'rubric-list__article-title'}).find('a')
        title = title_and_link.text
        link = 'https://1prime.ru' + title_and_link.get('href')
        card.append(f'{title},: {link}')
    print(card)
    return card[:3]


# https://russian.rt.com/tag/dollar
# Доллар
def pars_dollar():
    soup = req_and_soup('https://russian.rt.com/tag/dollar')

    card = []
    news = soup.find_all('div', {'class': 'card card_all-new'})
    for new in news:
        title_and_link = new.find('div', {'class': 'card__heading card__heading_all-new'}).find('a')
        title = title_and_link.text.strip()
        link = 'https://russian.rt.com' + title_and_link.get('href')
        card.append(f'{title},: {link}')
    print(card)
    return card[:3]

# https://gold.1prime.ru/
# Золото
def pars_zoloto():
    soup = req_and_soup('https://gold.1prime.ru/')

    card = []
    news = soup.find_all('article', {'class': 'news-feed__article'})
    for new in news:
        title_and_link = new.find('a', {'class': 'news-feed__article-title'})
        title = title_and_link.text
        link = 'https://gold.1prime.ru/' + title_and_link.get('href')
        card.append(f'{title},: {link}')
    print(card)
    return card[:3]

# https://ru.tradingview.com/ideas/gold/
# Золото аналитика
def analytics_a(url):
    soup = req_and_soup(url)


    card = []
    news = soup.find_all('div', {'class': 'tv-feed__item'})
    for new in news:
        try:
            title_and_link = new.find('div', {'class': 'tv-widget-idea js-userlink-popup-anchor'}).find('div', {'class': 'tv-widget-idea__title-row'}).find('a')
            title = title_and_link.text
            link = 'https://ru.tradingview.com' + title_and_link.get('href')
            card.append(f'{title},: {link}')
        except Exception as e:
            print(e)
    print(card)
    return card[:3]



# Сравнение курса доллара

def comparison():
    soup = req_and_soup('https://www.banki.ru/products/currency/cash/usd/moskva/')
    d = []

    sale_purchase = soup.find_all('td', {'class': 'currency-table__rate currency-table__bordered-col'})
    for sale_and_purchase in sale_purchase:
        purchase_and_link_bank = sale_and_purchase.find('a', {'class': 'currency-table__link'})
        link_purchase = 'https://www.banki.ru' + purchase_and_link_bank.get('href')
        purchase = purchase_and_link_bank.find('div', {'class': 'currency-table__large-text'}).text
        d.append(f'{purchase},: {link_purchase}')
    return d

