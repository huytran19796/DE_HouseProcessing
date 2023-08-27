import json

class ZillowPipeline:
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ","+ "\n"
        self.file.write(line)
        return item
 
    def open_spider(self, spider):
        self.file = open('/opt/airflow/data_stage_1/california_houses.json', 'w')
        header='['
        self.file.write(header)
 
    def close_spider(self, spider):
        footer='{' + '}]'
        self.file.write(footer)
        self.file.close()