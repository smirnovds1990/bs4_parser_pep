# bs4_parser_pep

Это парсер с разными режимами работы:
- Режим whats-new:
собирает данные в формате ('Ссылка на статью', 'Заголовок', 'Редактор, Автор') на страницы с описанием обновлений в python в зависимости от версии.
- Режим latest-versions:
собирает данные в формате ('Ссылка на документацию', 'Версия', 'Статус') на страницы с документацией python в зависимости от версии.
- Режим download:
скачивает архив с документацией последней версии python  в формате pdf-A4.
- Режим pep: 
собирает информацию о статусах PEP, подсчитывает их общее количество, а также сравнивает статусы в общей таблице на основной странице сайта https://peps.python.org/pep-0000/# со статусами на страницах конкретных PEP и выводит информацию в случае несовпадения статусов.

## Технологии
- Python
##### Основные сторонние библиотеки
- beautifulsoup4
- requests_cache
- tqdm
- requests
- lxml
- prettytable

### Установка
Склонировать репозиторий
```
git clone https://github.com/smirnovds1990/bs4_parser_pep
```

Установка виртуального окружения и зависимостей:
```
python -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
```

Запуск парсера:
перейти в папку с кодом, запустить парсер с указанием нужного режима.
```
cd src
python main.py whats-new|latest-versions|download|pep
```
также опционально можно указать дополнительные аргументы
- '-c' или '--clear-cache' для очистки кеша перед запуском
- '-o' или '--output' для вывода, плюс 'pretty' или 'file' формата вывода

Примеры команд
```
python main.py latest-versions --output file
python main.py pep --output pretty
python main.py whats-new --clear-cache
```

###### Автор проекта
[smirnovds](https://github.com/smirnovds1990)