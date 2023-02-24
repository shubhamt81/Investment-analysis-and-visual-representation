# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class TryzPipeline:
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'bgnobpenpyjuevrh0fpe-mysql.services.clever-cloud.com',
            user = 'u2enmuofuxxuyrkq',
            password = '1rZVoL6BvM04OSZ7VfIH',
            database = 'bgnobpenpyjuevrh0fpe'
        )

        ## Create cursor, used to execute commands
        self.cur = self.conn.cursor()
        

    
    def process_item(self, item, spider):
        self.cur.execute(" insert into name(Company_name,name_of_plan,link) values(%s,%s,%s);"
        ,(item['company_name'],str(item['fund_name']),str(item['link'])))
        self.conn.commit()
        self.cur.execute("SET FOREIGN_KEY_CHECKS = 0;")
        self.conn.commit()
        self.cur.execute(
            "insert into returns(Company_name,name_of_plan,cap_size,type_of_investment,ROI,risk,min_investment) values(%s,%s,%s,%s,%s,%s,%s);"
        ,(str(item['company_name']),str(item['fund_name']),float(item['val']),str(item['type']),float(item['roi']),'HIGH',float(0))
        )
        self.conn.commit()
        self.cur.execute("SET FOREIGN_KEY_CHECKS = 1;")
        self.conn.commit()
        

    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()
