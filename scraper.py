import scrapy

class newSpider(scrapy.spider):
    name = "CreepyCrawler"
    start_urls = ['https://ite.edu.sg']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }


# To recurse next page
            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback = self.parse
                )