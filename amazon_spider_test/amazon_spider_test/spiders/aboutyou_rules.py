#
#
#
#
#
import scrapy
#
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AboutyouRulesSpider(CrawlSpider):
    name = "aboutyou_rules"
    allowed_domains = ["www.aboutyou.ro"]
    start_urls = ["https://www.aboutyou.ro/c/femei/haine/moda-pentru-femei-insarcinate-158750"]

    rules = (
        Rule(LinkExtractor(allow=('/p/(noppies|mamalicious|nike|only-maternity|love2wait)/',)),
                callback='parse_product'),
        )
    
    def parse_product(self, response):
        print(response.url)
    
    # https://asmap-bucket-production-smaps-eu-west-1.s3-eu-west-1.amazonaws.com/ro/sitemap.xml.gz
    """
    Pentru AboutYou am gasit XML ---> De unde pot fi scoase toate link-urile cu produse foarte usor. 
    ihaaaaa...!!!
    """
