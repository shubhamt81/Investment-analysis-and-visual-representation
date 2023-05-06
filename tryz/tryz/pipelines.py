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
            "insert into returns(Company_name,name_of_plan,cap_size,type_of_investment,ROI,risk,min_investment,ROI_1M,ROI_3M,ROI_6M,ROI_1Y,ROI_3Y,ROI_5Y,ROI_10Y,cat,sub_cat,vro_rating,lumpsum_min,sip_min,aum,nav,CAT_AVG_10Y,CAT_AVG_5Y,CAT_AVG_3Y,CAT_AVG_1Y,CAT_AVG_6M,CAT_AVG_3M,CAT_AVG_1M    ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        ,(str(item['company_name']),str(item['fund_name']),float(item['val']),str(item['type']),float(item['roi']),item['risk'],float(0),str(item['roi_1m']),str(item['roi_3m']),str(item['roi_6m']),str(item['roi_1y']),str(item['roi_3y']),str(item['roi_5y']),str(item['roi_10y']),str(item['cat']),str(item['sub_cat']),str(item['vro']),str(item['lumpsum_min']),str(item['sip_min']),str(item['aum']),str(item['nav']),str(item['cat_avg_10y']),str(item['cat_avg_5y']),str(item['cat_avg_3y']),str(item['cat_avg_1y']),str(item['cat_avg_6m']),str(item['cat_avg_3m']),str(item['cat_avg_1m']))
        )
        self.conn.commit()
        self.cur.execute("SET FOREIGN_KEY_CHECKS = 1;")
        self.conn.commit()
        self.cur.execute(" insert into duration(Company_name,Name_of_plan,time_for_maturity,age,lockdown) values(%s,%s,%s,%s,%s);"
        ,(item['company_name'],str(item['fund_name']),str(0),str(item['age']),str(item['lockdown_duration'])))
        self.conn.commit()
        

    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.conn.close()
