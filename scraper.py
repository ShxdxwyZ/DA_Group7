# importing libraries that are needed
import scrapy
from scrapy.http.request import Request
import requests as req

global stat  # realise "stat" as a global variable


class NewSpider(scrapy.Spider):
    name = "CreepyCrawler"
    url = 'https://brickset.com/sets/year-2004'  # page URL for doing GET request
    start_urls = ['https://brickset.com/sets/year-2004']
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
            stat = "Bad Gateway"
        else:
            continue  # a continue is needed as there are more service codes than there are stated here

    print("Performing GET request....\nStatus code: ", r.status_code, stat, "\n\n")  # display status code
    # Obtaining current header
    h = req.head(url)
    # printing current header
    print("Current header:\n=======================================================")
    for x in h.headers:
        print("\t", x, ":", h.headers[x])
    print("=======================================================\n\n")

# spoofing current header to a mobile header
    def start_requests(self):
        headers = {'User-Agent': "Mobile"}
        for url in self.start_urls:
            yield Request(url, headers=headers)
        url2 = 'http://httpbin.org/headers'  # External site to retrieve our spoofed header
        spoofed = req.get(url2, headers=headers)
        print("Spoofed Header: (via external site http://httpbin.org/headers)\n======================================="
              "================\n", spoofed.text,
              "=======================================================\n\n")
        # large print to make output in terminal to be more pleasing to the eye

# parse function used to retrieve/export the type of files we want
    def parse(self, response, **kwargs):
        css_selector = 'img'  # using variable css_selector. we will not be using xpath for this project
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),  # extracting 'img' files
            }
        # start of 'next page function'
        page_selector = '.next a ::attr(href)'  # to recurse to next page
        next_page = response.css(page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
