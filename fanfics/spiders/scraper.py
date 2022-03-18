import scrapy
from ..items import FanficsItem


class FanficsCrawler(scrapy.Spider):
    name = 'fanfics'
    start_urls = [
        'https://archiveofourown.org/tags/Video%20Blogging%20RPF/works?page=1'
    ]

    def parse(self, response):
        items = FanficsItem()

        for fanfic in response.css('[role~=article]'):
            title = '.heading a::text'
            author = '[rel~=author]::text'
            date = '.datetime::text'
            fandoms = 'h5 a.tag::text'
            characters = '.characters a.tag::text'
            parings = '.relationships a.tag::text'
            warnings = '.warnings a.tag::text'
            freeforms = '.freeforms a.tag::text'
            description = 'p:not(.datetime)::text'
            language = 'dd.language::text'
            number_of_words = 'dd.words::text'
            hits = 'dd.hits::text'

            items['title'] = fanfic.css(title)[0].get()
            items['author'] = fanfic.css(author).get()
            items['date'] = fanfic.css(date).get()
            items['fandoms'] = fanfic.css(fandoms).getall()
            items['characters'] = fanfic.css(characters).getall()
            items['parings'] = fanfic.css(parings).getall()
            items['warnings'] = fanfic.css(warnings).getall()
            items['freeforms'] = fanfic.css(freeforms).getall()
            items['description'] = fanfic.css(description).get()
            items['language'] = fanfic.css(language).get()
            items['number_of_words'] = fanfic.css(number_of_words).get()
            items['hits'] = fanfic.css(hits).get()

            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


