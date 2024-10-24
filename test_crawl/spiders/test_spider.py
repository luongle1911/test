from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            r'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/huyen-cu-chi-286',
            r'https://masothue.com/tra-cuu-ma-so-thue-theo-tinh/huyen-hoc-mon-535'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")