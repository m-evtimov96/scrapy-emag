import scrapy


class GpuSpider(scrapy.Spider):
    name = 'gpu_spider'
    allowed_domains = ['emag.bg/video-karti/c']
    start_urls = ['http://emag.bg/video-karti/c']

    def parse(self, response):
        products = response.css('div.card-v2')

        for product in products:
            item = {
                'name': product.css('a.card-v2-title.semibold.mrg-btm-xxs.js-product-url::text').get().replace(',',' '),
                'price': product.css('p.product-new-price::text').get(),
                'image': product.css('img::attr(src)').get(),
            }
            yield item


