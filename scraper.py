import scrapy
from scrapy.http.request import Request


class NewSpider(scrapy.Spider):
    name = "CreepyCrawler"
    start_urls = ['https://ite.edu.sg']

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'}
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }


# To recurse next page
            page_selector = '.next a ::attr(href)'
            next_page = response.css(page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
