# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
'''
pipeline  用于处理数据  清理  存储
'''

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymysql



class titlePipeline:

    def __init__(self):
        self.limit = 10
    # process_item 必须实现的方法
    def process_item(self, item, spider):
        if item['title']:
            if len(item['title']) > self.limit:
                item['title'] = item['title'][0:self.limit].strip() + "......"
                return item
        else:
            return DropItem("Missing Title")

class SqlPipeline:
    def __init__(self,db_user,db_passwd,db_name,db_host):
        self.db_user = db_user
        self.db_passwd = db_passwd
        self.db_name = db_name
        self.db_host = db_host
        self.conn = None
        self.cursor = None

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            db_user=crawler.settings.get('DB_USER'),
            db_passwd=crawler.settings.get('DB_PASSWD'),
            db_name=crawler.settings.get('DB_NAME'),
            db_host = crawler.settings.get('DB_HOST')
        )

    # 默认方法
    def open_spider(self,spider):
        self.conn = pymysql.connect(host=self.db_host, user=self.db_user, password=self.db_passwd,database=self.db_name, charset='utf8')

        if self.conn:
            print("创建链接成功")
            self.cursor = self.conn.cursor()

    def close_spider(self,spider):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    def process_item(self, item, spider):
        title = item['title']
        date = item['date']
        read = item['read']
        rows = self.cursor.execute(
            "insert into note(`title`,`date`,`read`) values (%s,%s,%s);",[title,date,read])  # 指定要执行的sql语句 创建数据库的语句没有返回值
        print(rows)

        return item



