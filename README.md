# Scrapy PEP - Асинхронный парсер документов PEP на базе фреймворка Scrapy.

Проект асинхронного парсинга документации Python
Выполняется парсинг данных со страницы с общей информацией о PEP (https://peps.python.org/), переход по ссылкам и сбор данных о каждом PEP. Парсер подготавливает данные и сохраняет их в два файла формата csv в папку results.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=013220)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=013220)](https://scrapy.org/)

## Оглавление
1. [Описание](#описание)
2. [Стек технологий](##стек-технологий)
3. [Как запустить проект](##как-запустить-проект)
4. [Автор проекта](##автор-проекта)


## Описание проекта:

Парсер, собирающий информацию с сайта https://www.python.org/
- версии языка и авторов версий;
- статусы всех стандартов PEP.

Вся собранная информация сохраняется в файлы с расширением **csv**:
- Информация о стандарте: номер, статус, автор-(ы);
- Колличество каждого статуса на сайте + общая сумма.

## Стек технологий
- Python, Scrapy

## Как запустить проект

Клонировать проект из репозитория
```
git@github.com:vikolga/scrapy_parser_pep.git
```

Создать, активировать виртуальное окружение и в него установить зависимости:

```
python -m venv .env
```

```
source .env/Scripts/activate
```

```
pip install -r requirements.txt
```

Запустить парсер из командной строки:

```
scrapy crawl pep
```

Результатом работы парсера будет создание двух файлов:

```
pep_ДатаВремя.csv
```
- содержит список всех PEP (number, name, status);

```
status_summary_ДатаВремя.csv
```
- содержит сводку по статусам PEP: сколько найдено документов в каждом статусе (Status, Quantity). В последней строке этого файла в колонке Total выводится общее количество всех документов.



## Автор проекта
_[Ольга Викторова](https://github.com/vikolga/)_, python-developer
