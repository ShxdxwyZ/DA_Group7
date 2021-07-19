import scrapy
class NewSpider(scrapy.Spider):
    name = "CreepyCrawler"
    start_urls = ['http://54.169.8.122/Python/172.18.58.238/snow/index.html']
    def parse(self,response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield{'Image Link': x.xpath(newsel).extract_first(),}
