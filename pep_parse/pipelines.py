# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import datetime as dt
import csv
from collections import Counter

from pep_parse.settings import BASE_DIR, DATE_FORMAT


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.sum_status = Counter()

    def process_item(self, item, spider):
        self.sum_status[item['status']] += 1
        return item

    def close_spider(self, spider):
        FIELDS = ['Статус', 'Количество']
        TOTAL = ['Total', sum(self.sum_status.values())]
        timestamp = dt.datetime.now().strftime(DATE_FORMAT)
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_name = f'status_summary_{timestamp}.csv'
        file_path = results_dir / file_name
        result = self.sum_status.most_common()
        with open(file_path, mode='w',
                  newline='', encoding='utf-8') as csvfile:
            status_file = csv.writer(csvfile, doublequote=False,
                                     delimiter=',', quoting=csv.QUOTE_MINIMAL)
            status_file.writerow(FIELDS)
            status_file.writerows(result)
            status_file.writerow(TOTAL)
