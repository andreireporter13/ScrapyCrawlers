#
#
#
#
import scrapy
from urllib.parse import unquote
from scrapy_playwright.page import PageMethod
#
from amazon_spider_test.items import AmazonSpiderTestItem
#


class AmazonTestSpider(scrapy.Spider):
    name = "amazon_test"
    allowed_domains = ["www.amazon.com"]

    def start_requests(self):

        for page in range(1,3):
            yield scrapy.Request(url=f"https://www.amazon.com/s?k=Blouses+%26+Button-Down+Shirts&i=fashion-womens-clothing&rh=n%3A2368365011&page={page}&c=ts&ts_id=2368365011&ref=sr_pg_{page}", 
                                callback=self.parse,
                                meta=dict(
                                playwright = True,
                                playwright_page_methods = [
                                    PageMethod('wait_for_selector', 
                                               'h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-4')
                                        ]
                                    ),)
            
    def parse(self, response):
        
        urls = response.css('a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal::attr(href)').extract()

        for link_to in range(10):
            uri = urls[link_to]

            # make request with product link
            yield scrapy.Request(url=f"https://www.amazon.com{unquote(uri)}",
                                callback=self.parse_product,
                                meta=dict(
                                playwright = True,
                                playwright_page_methods = [
                                    PageMethod('wait_for_selector', 'span#productTitle')
                                        ]
                                    ),
                                )
            
    def parse_product(self, response):

        item = AmazonSpiderTestItem()
        item['url'] = response.url
        item['title'] = response.css('span#productTitle::text').extract_first().strip()
        item['price'] = response.css('span.a-offscreen::text').extract_first().split()[0].replace('$', '')
        item['img_product'] = response.css('img.imgSwatch::attr(src)').extract_first()    

        yield item