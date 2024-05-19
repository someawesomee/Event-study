import pandas as pd
import requests
from bs4 import BeautifulSoup

from list_of_urls import urls

# Создание пустого списка для хранения датафреймов
dfs = []

# Цикл для обработки каждого URL
for url in urls:
    print(url)
    # Загрузка HTML-документа
    response = requests.get(url)
    html_content = response.content

    # Парсинг HTML с помощью BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Поиск таблицы с классом "oj-table"
    tables = soup.find_all("table", {"class": "oj-table"})

    # Извлечение данных из всех таблиц
    for table in tables:
        data = []
        for row in table.find_all("tr"):
            row_data = [cell.text.strip() for cell in row.find_all("td")]
            if row_data:
                data.append(row_data)

        # Создание датафрейма Pandas
        df = pd.DataFrame(data)
        print(df)
        # Добавление датафрейма в список
        dfs.append(df)

# Объединение датафреймов в один
df_final = pd.concat(dfs, ignore_index=True)

# Вывод датафрейма
print(df_final)


df_final.to_excel("eu_sunctions.xlsx")
