import scrapy
from scrapy.http.request import Request


class NewSpider(scrapy.Spider):
    name = "CreepyCrawler"
    start_urls = ['https://ite.edu.sg']

    def start_requests(self):
        headers = {'User Agent: Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'}
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
