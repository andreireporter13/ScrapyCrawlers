#
#
#
#
#
import scrapy
from amazon_spider_test.items import AmazonSpiderTestItem
#
from playwright.async_api import async_playwright
#
from bs4 import BeautifulSoup


class AboutyouSpider(scrapy.Spider):
    name = "aboutyou"
    allowed_domains = ["www.aboutyou.ro"]
    start_urls = ["https://www.aboutyou.ro/c/femei/haine/moda-pentru-femei-insarcinate-158750"]

    @classmethod
    async def parse(cls, response):
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            context = await browser.new_context()
            page = await context.new_page()

            await page.goto(response.url)
            await page.wait_for_load_state("domcontentloaded")

            # wait for selector to load
            await page.wait_for_selector('li.sc-oelsaz-0.YkKBp', state='visible')

            prev_links = set()
            links_site = list()
            second_list = list()
            count = 0
            while True:
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
                await page.wait_for_timeout(5000)

                # can_scroll = await page.evaluate('''() => {
                #     const scrollTop = window.pageYOffset;
                #     const scrollHeight = document.body.scrollHeight;
                #     const clientHeight = document.documentElement.clientHeight;
                #     return scrollHeight > scrollTop + clientHeight;
                # }''')

                count += 1
                if count == 20:
                    break

                print(count)


                current_links = await page.evaluate('''() => {
                    const links = document.querySelectorAll('a.sc-16ol3xi-0.sc-163x4qs-0.KQunc.jHpeFA.sc-nlxe42-5.llVvtR');
                    return Array.from(links).map(link => link.getAttribute('href'));
                }''')

                for linkos in current_links:
                    if linkos not in second_list:
                        second_list.append(linkos)

                links_site.extend(current_links)

                # print("Current Links:", current_links, len(current_links))

                # if set(current_links).issubset(prev_links):
                #     break

                # prev_links = current_links

            #print(links_site)
            print(len(links_site), len(second_list), second_list)

        await browser.close()

        
        