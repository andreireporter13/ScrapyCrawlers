#
#
#
#
#
import scrapy
import re
import math


def make_headers(page: str, bm_sz: str, _abck: str, akavpau: str) -> tuple[str, dict]:
    '''
    ... Make custom requests for H&M company.
    '''

    url = f"https://www2.hm.com/ro_ro/barbati/colectie-noua/view-all/_jcr_content/main/productlisting.display.json?sort=stock&image-size=small&image=model&offset={page}&page-size=36"

    headers = {  
        'authority': 'www2.hm.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.5',
        'cookie': 'preshoppingUser=false; akainst=EU2; agCookie=b23f3184-e42e-4106-989d-dd759366898a; hm-romania-favourites=""; HMCORP_locale=ro_RO; HMCOUNTRY_name=Romania; HMCORP_locale_autoassigned=false; bm_sz={bm_sz}; AKA_A2=A;_abck={_abck}; akamref=ro_ro; akavpau_www2_ro_ro={akavpau};',
        'referer': f'https://www2.hm.com/ro_ro/barbati/colectie-noua/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size={page}',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        }

    return url, headers


class HmSpiderSpider(scrapy.Spider):
    name = "hm_spider"
    allowed_domains = ["www2.hm.com"]
    start_urls = ["https://www2.hm.com/ro_ro/barbati/colectie-noua/view-all.html"]

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0],
                             callback=self.parse_headers, method='GET')

    def parse_headers(self, response):
        str_headers = str(response.headers)

        # scrape all items from page
        items = str(response.css('h2.load-more-heading::attr(data-total)').extract_first())

        bm_sz = re.search(r'bm_sz=([^;]+)', str_headers).group(1)
        _abck = re.search(r'_abck=([^;]+)', str_headers).group(1)
        akavpau = re.search(r'akavpau_www2_ro_ro=([^;]+)', str_headers).group(1)

        # make headers + url and request
        offset = 0
        for i in range(0, math.ceil(int(items) / 36)):
            headers_url = make_headers(page=offset, bm_sz=bm_sz, _abck=_abck, akavpau=akavpau)

            yield scrapy.Request(
                    url=headers_url[0],
                    method='GET',
                    headers=headers_url[1],
                    callback=self.parse
                )
            offset += 36
        
    def parse(self, response):

        lst_links = list()
        for link in response.json()['products']:
            lst_links.append(f"https://www2.hm.com{link['link']}")

        print(lst_links, len(lst_links))