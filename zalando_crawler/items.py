# -*- coding: utf-8 -*-
import scrapy


class ZalandoItem(scrapy.Item):

    title = scrapy.Field()
    price = scrapy.Field()
    remote_id = scrapy.Field()
    main_image = scrapy.Field()
    category = scrapy.Field()
    availability = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()
    extra_images = scrapy.Field()
    color = scrapy.Field()
    product_condition = scrapy.Field()
    variations = scrapy.Field()
    currency = scrapy.Field()

