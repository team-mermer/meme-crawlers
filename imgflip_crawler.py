import scrapy


class ImgflipSpider(scrapy.Spider):
    name = 'imgflip_spider'
    allowed_domains = ['https://imgflip.com/']
    start_urls = ['https://imgflip.com/memetemplates']

    def parse(self, response):
        pass