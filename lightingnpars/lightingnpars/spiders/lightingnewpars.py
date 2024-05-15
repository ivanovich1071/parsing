import scrapy


class LightingnewparsSpider(scrapy.Spider):
    name = "lightingnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        ligtins = response.css('div.PUK0i')
        for ligtin in ligtins:

            yield {

                'name':ligtin.css('div.LZRug span::text').get(),
                # Создаём словарик цен, используем поиск по диву, а внутри дива — по тегу span
                'price': ligtin.css('div.RJsqR span::text').get(),
                # Создаём словарик ссылок, используем поиск по тегу "a", а внутри тега — по атрибуту
                # Атрибуты — это настройки тегов
                'url': ligtin.css('a').attrib['href']
            }

