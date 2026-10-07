import requests
import bs4



url = 'https://habr.com/ru/articles/'
response = requests.get(url)

with open('index.html', 'w',encoding='utf-8') as file:
    file.write(response.text)
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
soup = bs4.BeautifulSoup(response.text, features='lxml')

articles = soup.select('article.tm-articles-list__item')

for article in articles:
    # Заголовок
    title = article.select_one('a.tm-title__link').text.strip()
    #cсылка
    link = 'https://habr.com'+ article.select_one('a')['href']

    # Дата
    date = article.select_one('time')['title']

    # Preview-текст: заголовок + анонс + хабы + теги — всё, что видно на листинге
    text = article.get_text(separator=' ', strip=True).lower()

    # Проверяем совпадение по ключевым словам
    if any(keyword in text for keyword in KEYWORDS):
        print(f'{date} – {title} – {link}')
