# importing libraries that are needed
import scrapy
from scrapy.http.request import Request
import requests as req
global stat  # realise "stat" as a global variable


class NewSpider(scrapy.Spider):
    name = "CreepyCrawler"
#    url = 'http://ite.edu.sg'
    url = 'http://54.169.8.122/Python/172.18.58.238/snow/index.html'  # page URL for doing GET request
    start_urls = ['http://54.169.8.122/Python/172.18.58.238/snow/index.html']
    print("Chosen URL: ", url, "\n")
    r = req.get(url)
    # for statement to print out the meaning of the few important status codes
    for y in str(r.status_code):
        if r.status_code == 200:
            stat = "OK"
        elif r.status_code == 404:
            stat = "Not Found"
        elif r.status_code == 500:
            stat = "Internal Server Error"
        elif r.status_code == 502:
            stat = "Service Unavailable"
        else:
            continue  # a continue is needed as there are more service codes than there are stated here

    print("Performing GET request....\nStatus code: ", r.status_code, stat, "\n\n")  # display status code
    # Obtaining current header
    h = req.head(url)
    print("Current header:\n=======================================================")
    for x in h.headers:
        print("\t", x, ":", h.headers[x])
    print("=======================================================\n\n")

# spoofing current header to a mobile header
    def start_requests(self):
        headers = {'User-Agent': "Mobile"}
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
        page_selector = '.next a ::attr(href)'  # to recurse to next page
        next_page = response.css(page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
