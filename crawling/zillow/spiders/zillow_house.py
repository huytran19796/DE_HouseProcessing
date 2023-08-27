from zillow.utils import URL, cookies_parser, parse_new_url
from zillow.items import ZillowItem
import scrapy
from scrapy.loader import ItemLoader
import json

class ZillowHouseSpider(scrapy.Spider):
    name = "zillow_house"
    allowed_domains = ["www.zillow.com"]
    
    def start_requests(self):
        yield scrapy.Request(
            url=URL,
            callback=self.parse,
            cookies=cookies_parser(),
            meta={
                'current_page': 1
            }
        )

    def parse(self, response):
        current_page = response.meta['current_page']
        json_resp = json.loads(response.body)
        houses = json_resp.get("cat1").get("searchResults").get("listResults")
        for house in houses:
            loader = ItemLoader(item=ZillowItem())
            loader.add_value('id', house.get('id'))
            loader.add_value('address', house.get('address'))
            loader.add_value('area', house.get('area'))
            loader.add_value('beds', house.get('beds'))
            loader.add_value('baths', house.get('baths'))
            loader.add_value('detail_url', house.get('detailUrl'))
            loader.add_value('image_urls', house.get('imgSrc'))
            loader.add_value('price', house.get('price'))
            loader.add_value('status_text', house.get('statusText'))
            loader.add_value('status_type', house.get('statusType'))
            loader.add_value('latitude', house.get('latLong').get("latitude"))
            loader.add_value('longitude', house.get('latLong').get("longitude"))
            loader.add_value('broker_name', house.get('brokerName'))
            loader.add_value('broker_phone', "")
            yield loader.load_item()
        
        total_pages = json_resp.get('cat1').get('searchList').get('totalPages')
        if current_page <= total_pages:
            current_page += 1
            yield scrapy.Request(
                url=parse_new_url(URL, current_page),
                callback=self.parse,
                cookies=cookies_parser(),
                meta={
                    'current_page': current_page
                }
            )