from ast import And
import scrapy



class RedditPostsSpider(scrapy.Spider):
    name = 'redditposts'
    start_urls = ['https://old.reddit.com/r/scrapy/']


    def parse(self, response):
        for item in response.css('div.thing'):
            yield {
                'title': item.css('a.title.may-blank::text').get(),
                'date': item.css('p.tagline time::attr(datetime)').get(),
                }
                
        next_page = response.css('span.next-button a::attr(href)').get()
        
        if (next_page is not None):
            yield response.follow(next_page, callback=self.parse)
            