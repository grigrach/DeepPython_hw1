import requests
from bs4 import BeautifulSoup

# Определяем ключевые слова
KEYWORDS = ['дизайн', 'фото', 'python', 'web','sql']

# Получаем страницу с самыми свежими статьями
response = requests.get('https://habr.com/ru/articles/')
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# Ищем все статьи на странице
articles = soup.find_all('article', class_='tm-articles-list__item')
#print(articles)

for article in articles:
    # Получаем заголовок статьи
    title_element = article.find('a', class_='tm-title__link')
    #print(title_element)
    title = title_element.text.strip()
    #print(title)

    # Получаем ссылку на статью
    href = title_element['href']
    #print(href)
    link = 'https://habr.com' + href
    #print(link)

    # Получаем дату публикации
    date_element = article.find('time')
    date = date_element['title']
    #print(date)

    # Проверяем наличие ключевых слов в заголовке или превью
    content = f"{title}".lower()
    #print(content)
    if any(keyword.lower() in content for keyword in KEYWORDS):
        print(f"{date} – {title} – {link}")