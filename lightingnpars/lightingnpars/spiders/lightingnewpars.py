import scrapy


class LightingnewparsSpider(scrapy.Spider):
    name = "lightingnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        ligtins = response.css('div.Yksws')
        for ligtin in ligtins:
            # Извлечение цены
            price_element = ligtin.css('span[data-testid="price"]')
            content_price = price_element.css('::attr(content)').get()
            text_price = price_element.css('::text').get().strip()
            final_price = content_price if content_price else text_price

            yield {
                'name': ligtin.css('img.c9h0M::attr(alt)').get(),
                'price': final_price,
                'url': ligtin.css('a').attrib['href']
            }

