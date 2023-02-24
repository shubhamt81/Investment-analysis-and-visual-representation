import scrapy
from ..items import TryzItem


class TryalSpider(scrapy.Spider):
    name = "tryal"
    allowed_domains = ["www.etmoney.com"]
    start_urls = ['https://www.etmoney.com/mutual-funds/equity/large-cap/32',
                  'https://www.etmoney.com/mutual-funds/equity/mid-cap/35',
                  'https://www.etmoney.com/mutual-funds/equity/small-cap/36',
                  'https://www.etmoney.com/mutual-funds/equity/large-cap-index/99',
                  'https://www.etmoney.com/mutual-funds/equity/mid-cap-index/100',
                  'https://www.etmoney.com/mutual-funds/equity/small-cap-index/101'
                  ]

    


    def parse(self, response):
        dic={'Aditya':'Aditya Birla','Axis':'Axis','Baroda':'Baroda','Canara':'Canara','DSP':'DSP'
          ,'Edelweiss':'Edelweiss','Franklin':'Franklin India','HDFC':'HDFC','ICICI':'ICICI'
          ,'Invesco':'Invesco India','Kotak':'Kotak','Mirae':'Mirae','Motilal':'Motilal Oswal',
          'Navi':'Navi','Nippon':'Nippon India','PGIM':'PGIM India','Quant':'Quant','Sundaram':'Sundaram'
          ,'Tata':'Tata','UTI':'UTI','SBI':'SBI','IDFC':'IDFC','HSBC':'HSBC'
          }
        item=TryzItem()
        for fund in response.xpath('//*[@id="fundListing"]/div[@class="mfFund-block media"]'):  
            v_fund=fund.xpath('.//div[2]/div/div[1]/div[1]/div[1]/a/text()').get()
            item['fund_name']=v_fund
            v_link=response.request.url.split('/')
            item['type']=v_link[5]
            item['company_name']=dic.get(str((v_fund.split(' '))[0]))
            item['link']="https://www.etmoney.com"+fund.xpath('.//div[2]/div/div[1]/div[1]/div[1]/a/@href').get()
            v_val=fund.xpath('.//div[2]/div/div[1]/div[2]/div[1]/p[2]/text()').get()
            v_roi=str(fund.xpath('.//div[2]/div/div[1]/div[2]/div[2]/div[2]/p/strong[2]/text()').get())[54:60]
            if(v_roi==""):
                item['roi']=float(0)
            else:
                item['roi']=float(v_roi[:-1])
            if(v_val==""):
                item['val']=float(0)
            else:
                v_val=v_val.replace(',','')
                item['val']=float((v_val.split(' ')[0])[1:])
            print(v_val,item['val'])
            print(v_roi,item['roi'])
            print(item)
            yield item
        
        

