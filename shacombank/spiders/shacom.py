import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from shacombank.items import Article


class ShacomSpider(scrapy.Spider):
    name = 'shacom'
    start_urls = ['https://www.shacombank.com.hk/tch/about/news/news.jsp']

    def parse(self, response):
        yield response.follow(response.url, self.parse_article, dont_filter=True)

        next_page = response.xpath('.//a[@class="right_arrow"]/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_article(self, response):
        articles = response.xpath('//tbody/tr')
        for article in articles:
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            link = article.xpath('./td[2]/a/@href').get()
            title = article.xpath('./td[2]/a/text()').get()
            date = article.xpath('./td[1]/text()').get().strip()
            date = datetime.strptime(date, '%d/%m/%Y')
            date = date.strftime('%Y/%m/%d')

            item.add_value('title', title)
            item.add_value('date', date)
            item.add_value('link', response.urljoin(link))

            yield item.load_item()
