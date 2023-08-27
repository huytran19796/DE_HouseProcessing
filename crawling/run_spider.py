from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from zillow.spiders.zillow_house import ZillowHouseSpider
from zillow.utils import setting_for_airflow

ZillowHouseSpider.custom_settings= setting_for_airflow
process = CrawlerProcess(get_project_settings())
process.crawl(ZillowHouseSpider)
process.start()