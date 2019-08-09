import scrapy


class KnowYourMemeSpider(scrapy.Spider):
    name = 'know_your_meme_spider'
    allowed_domains = ['https://knowyourmeme.com/']
    start_urls = ['https://knowyourmeme.com/memes/']

    def parse(self, response):
        pass