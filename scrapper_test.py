
import unittest

class TestScrapper(unittest.TestCase):
    def test_requests(self):
        print("Spoofing current header....\n")
        headers = {'User-Agent': "Mobile"}
        for url in self.start_urls:
            yield Request(url, headers=headers)
        url2 = 'http://httpbin.org/headers'
        print("Using site 'http://httpbin.org/headers' to obtain spoofed header....\n")
        spoofed = req.get(url2, headers=headers)
        print("Spoofed Header: (via external site http://httpbin.org/headers)\n======================================="
              "================\n", spoofed.text,
              "=======================================================\n\n")

    def test_parse(self):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

if __name__ == '__main__':
    unittest.main