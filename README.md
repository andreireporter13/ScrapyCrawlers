# About my experience with Python3: Scrapy, Playwright, Selenium, Requests, BS4, requests-html etc.

Sites that are larger and more complex pose a greater challenge, but this is not an issue. If they cannot be accessed
using simple HTTPS requests with Scrapy, we can configure Playwright within the project. Additionally, there are alternative
options such as Splash and Selenium. For more intricate and robust websites, we may choose to build a project exclusively using 
Selenium, as demonstrated in the project below:

[Selenium app for SEO Analysis](https://github.com/andreireporter13/SEO-1st-page-Google-data-scrape)
This project has been configured with a web driver using Selenium. I have implemented more complex logic 
here, including anti-bot detection and proxy configuration.
[Browser Config for Selenium](https://github.com/andreireporter13/SEO-1st-page-Google-data-scrape/blob/SEO-1st-page-Google-data-scrape/browser_settings/browser_settings_file.py)

And video presentation with Selenium Headless app:

[![SEO app with Selenium Headless](https://i.ytimg.com/vi/44cThvaa3Jw/hqdefault.jpg)](https://www.youtube.com/watch?v=44cThvaa3Jw&t=687s "SEO APP + Selenium Headless")

The extensive Scrapy project I created for peviitor.ro can be found at:
[Scrapy full automated project](https://github.com/peviitor-ro/Scrapy_peviitor_jobs)
In this project, I configured Scrapy for crawling, processing items, and updating API data on peviitor.ro.
Scrapy is the best choice for large-scale scraping projects due to its ease of use. Even if someone
else works on your project, they will easily understand the configuration.

Scrapy project video presentation:

[![Scrapy video presentation](https://i.ytimg.com/vi/i_fkt29UuPs/hqdefault.jpg)](https://www.youtube.com/watch?v=i_fkt29UuPs&t=4s "Scrapy Project")

My another project is for Peviitor.ro: a Job Search Engine. You can find the custom build for scraping at:
[Peviitor Project - Custom build for Scraping](https://github.com/peviitor-ro/Scrapers_start_with_digi)
This section provides insights into my custom solution for scraping and is designed for new contributors.
It's straightforward to create a new template for scraping within this project. Users will find it easy to create new scrapers:

>  You can create new files for scrapers from ->
>  ... your terminal. For example:
>  python3 __create_scraper.py "name_scraper" "link" "type_scraper"
>  Its really useful when you have a lot of scrapers.
>
>  You can create your own scraper:
>  ... static
>  ... dynamic_json_get
>  ... dynamic_json_post
>  ... dynamic_render
>  ... custom

[File for create scraping template](https://github.com/peviitor-ro/Scrapers_start_with_digi/blob/main/new_sites/__create_scraper.py)
[Folder with __utils files for automate scraping process](https://github.com/peviitor-ro/Scrapers_start_with_digi/tree/main/new_sites/__utils)

Custom scraping project video presentation:

[![Custom solution for scraping - video presentation](https://i.ytimg.com/vi/icoCA8it9zw/hqdefault.jpg)](https://www.youtube.com/watch?v=icoCA8it9zw&t=351s "Custom Scraping Project")

In this project, I opted not to use Selenium due to the limitation of GitHub Actions, which provides only 4GB of RAM for each virtual machine.
Instead, I employed requests_html, a lightweight browser emulator that proved sufficient for our requirements.
 
I implemented the Singleton Pattern in this project to streamline the workflow for scrapers. The feedback from the 5 students who have used
it is very positive. They only need to create an instance, and the results are conveniently available within that instance. 
There is no need to invoke additional magic methods.

### Little example from Scrapy

#### Note about Scraping:
In the web scraping process, the first step involves searching for a REST API or SOAP service on the site.
If these are not available, the next step is to parse the HTML. In the case of dynamic pages rendered with JavaScript,
we explore the possibility of finding an XML file associated with the site. However, it's crucial to compare the .xml file
with the site's category; if they match, we proceed with scraping. Note that the XML file may not be instantly updated with 
changes in the site's category.

If none of these methods proves effective, we resort to using Playwright or Selenium to interact directly with the web page

![Scrapy](./project_photo/photo_presentation.png)

#### Pipeplines
![Pipelines](./project_photo/pipelines.png)

#### First tests in "scrapy shell"
![Scrapy Shell](./project_photo/scrapy_shell.png)

I have extensively worked with Scrapy, a Python web scraping framework, to extract and analyze 
data from various websites. Leveraging its flexible architecture and powerful features, I have 
successfully developed efficient web scraping solutions for diverse projects.
