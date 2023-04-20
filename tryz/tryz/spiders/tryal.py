import scrapy
from ..items import TryzItem


class TryalSpider(scrapy.Spider):
    name = "tryal"
    allowed_domains = ["www.etmoney.com"]
    start_urls = [
        'https://www.etmoney.com/mutual-funds/nippon-india-large-cap-fund-direct-growth/15759',
        'https://www.etmoney.com/mutual-funds/icici-prudential-bluechip-fund-direct-growth/15408',
        'https://www.etmoney.com/mutual-funds/canara-robeco-bluechip-equity-fund-direct-growth/15332',
        'https://www.etmoney.com/mutual-funds/sbi-bluechip-direct-plan-growth/15765',
        'https://www.etmoney.com/mutual-funds/hdfc-top-100-fund-direct-plan-growth/15731',
        'https://www.etmoney.com/mutual-funds/edelweiss-large-cap-fund-direct-growth/16911',
        'https://www.etmoney.com/mutual-funds/kotak-bluechip-fund-direct-growth/15904',
        'https://www.etmoney.com/mutual-funds/baroda-bnp-paribas-large-cap-fund-direct-growth/15286',
        'https://www.etmoney.com/mutual-funds/tata-large-cap-direct-plan-growth/16292',
        'https://www.etmoney.com/mutual-funds/mirae-asset-large-cap-fund-direct-growth/16138',
        'https://www.etmoney.com/mutual-funds/aditya-birla-sun-life-frontline-equity-direct-fund-growth/15398',
        'https://www.etmoney.com/mutual-funds/uti-mastershare-direct-growth/15356',
        'https://www.etmoney.com/mutual-funds/invesco-india-largecap-fund-direct-growth/16275',
        'https://www.etmoney.com/mutual-funds/bandhan-large-cap-fund-direct-growth/16262',
        'https://www.etmoney.com/mutual-funds/pgim-india-large-cap-fund-direct-plan-growth/15141',
        'https://www.etmoney.com/mutual-funds/hsbc-large-cap-fund-direct-growth/15856',
        'https://www.etmoney.com/mutual-funds/franklin-india-bluechip-direct-fund-growth/15549',
        'https://www.etmoney.com/mutual-funds/dsp-top-100-equity-direct-plan-growth/16019',
        'https://www.etmoney.com/mutual-funds/axis-bluechip-fund-direct-plan-growth/15249',
        'https://www.etmoney.com/mutual-funds/quant-large-cap-fund-direct-growth/42811',
        'https://www.etmoney.com/mutual-funds/sundaram-large-cap-fund-direct-growth/41572',
        'https://www.etmoney.com/mutual-funds/quant-mid-cap-fund-direct-growth/16934',
        'https://www.etmoney.com/mutual-funds/pgim-india-midcap-opportunities-fund-direct-growth/21891',
        'https://www.etmoney.com/mutual-funds/motilal-oswal-midcap-fund-direct-growth/23602',
        'https://www.etmoney.com/mutual-funds/sbi-magnum-mid-cap-direct-plan-growth/15802',
        'https://www.etmoney.com/mutual-funds/edelweiss-mid-cap-direct-plan-growth/16149',
        'https://www.etmoney.com/mutual-funds/kotak-emerging-equity-fund-direct-growth/16693',
        'https://www.etmoney.com/mutual-funds/bandhan-large-cap-fund-direct-growth/16262',
        'https://www.etmoney.com/mutual-funds/quant-liquid-direct-fund-growth/16587',
        'https://www.etmoney.com/mutual-funds/aditya-birla-sun-life-liquid-fund-direct-growth/15367',
        'https://www.etmoney.com/mutual-funds/edelweiss-liquid-direct-growth/16139',
        'https://www.etmoney.com/mutual-funds/pgim-india-liquid-fund-direct-plan-growth/15172',
        'https://www.etmoney.com/mutual-funds/franklin-india-liquid-fund-direct-growth/16411',
        'https://www.etmoney.com/mutual-funds/axis-liquid-direct-fund-growth/15315',
        'https://www.etmoney.com/mutual-funds/icici-prudential-liquid-fund-direct-plan-growth/15528',
        'https://www.etmoney.com/mutual-funds/sbi-liquid-fund-direct-plan-growth/15869',
        'https://www.etmoney.com/mutual-funds/kotak-liquid-direct-growth/15932',
        'https://www.etmoney.com/mutual-funds/hdfc-liquid-direct-plan-growth/15734',
        'https://www.etmoney.com/mutual-funds/motilal-oswal-liquid-fund-direct-growth/38994',
        'https://www.etmoney.com/mutual-funds/icici-prudential-all-seasons-bond-fund-direct-plan-growth/16679',
        'https://www.etmoney.com/mutual-funds/sbi-dynamic-bond-direct-plan-growth/15766',
        'https://www.etmoney.com/mutual-funds/kotak-dynamic-bond-fund-direct-growth/15909',
        'https://www.etmoney.com/mutual-funds/hdfc-dynamic-debt-fund-direct-plan-growth/15628',
        'https://www.etmoney.com/mutual-funds/nippon-india-dynamic-bond-fund-direct-growth/15627',
        'https://www.etmoney.com/mutual-funds/canara-robeco-dynamic-bond-fund-direct-growth/16140',
        'https://www.etmoney.com/mutual-funds/icici-prudential-multi-asset-fund-direct-growth/15512',
        'https://www.etmoney.com/mutual-funds/sbi-multi-asset-allocation-fund-direct-growth/17213',
        'https://www.etmoney.com/mutual-funds/axis-triple-advantage-direct-plan-growth/15260',
        'https://www.etmoney.com/mutual-funds/aditya-birla-sun-life-multi-asset-allocation-fund-direct-growth/43475',
        'https://www.etmoney.com/mutual-funds/tata-multi-asset-opportunities-fund-direct-growth/41158',
        'https://www.etmoney.com/mutual-funds/nippon-india-multi-asset-fund-direct-growth/41542'
        

        
        
        
    ]
    def clean_roi(v_roi):
        if(v_roi==""):
            roi=float(0)
        else:
            if((48<=ord(v_roi[0])<=57) or v_roi[0]=='-'):
                roi=float(v_roi[:-1])
            else:
                roi=float(0)
        return roi
    
    
    def parse(self, response):
        dic={'Aditya':'Aditya Birla','Axis':'Axis','Baroda':'Baroda','Bandhan':'Bandhan','Canara':'Canara','DSP':'DSP'
          ,'Edelweiss':'Edelweiss','Franklin':'Franklin India','HDFC':'HDFC','ICICI':'ICICI'
          ,'Invesco':'Invesco India','Kotak':'Kotak','Mirae':'Mirae','Motilal':'Motilal Oswal',
          'Navi':'Navi','Nippon':'Nippon India','PGIM':'PGIM India','Quant':'Quant','Sundaram':'Sundaram'
          ,'Tata':'Tata','UTI':'UTI','SBI':'SBI','IDFC':'IDFC','HSBC':'HSBC'
          }
        item=TryzItem()
        item['fund_name']=response.xpath('/html/body/div[1]/div[9]/div[1]/div[1]/div/div/div[2]/div[1]/h1/text()').get()
        v_val=response.xpath('/html/body/div[1]/div[10]/div/div[1]/div[4]/div/div/div/table/tbody/tr[5]/td[2]/span[2]/text()').get()
        v_roi=str(response.xpath('/html/body/div[1]/div[9]/div[2]/div/div/div/div/div/div/div[2]/p[3]/span[1]/text()').get())
        v_link=str(response)
        v_link=v_link[5:]
        v_link=v_link[:-1]
        
        item['link']=v_link
        v_fund=item['fund_name']
        v_link=response.request.url.split('/')
        item['type']=v_link[3]
        item['company_name']=dic.get(str((v_fund.split(' '))[0]))
        item['roi']=TryalSpider.clean_roi(v_roi)
        item['roi_1m']=TryalSpider.clean_roi(str(response.xpath('/html/body/div[1]/div[10]/div/div[2]/section[2]/div/div/div/div[1]/div/table/tbody/tr[1]/td[2]/span/text()').get()))
        item['roi_3m']=TryalSpider.clean_roi(str(response.xpath('/html/body/div[1]/div[10]/div/div[2]/section[2]/div/div/div/div[1]/div/table/tbody/tr[2]/td[2]/span/text()').get()))
        item['roi_6m']=TryalSpider.clean_roi(str(response.xpath('/html/body/div[1]/div[10]/div/div[2]/section[2]/div/div/div/div[1]/div/table/tbody/tr[3]/td[2]/span/text()').get()))
        item['roi_1y']=TryalSpider.clean_roi(str(response.xpath('/html/body/div[1]/div[10]/div/div[2]/section[2]/div/div/div/div[1]/div/table/tbody/tr[4]/td[2]/span/text()').get()))
        item['roi_3y']=TryalSpider.clean_roi(str(response.xpath('/html/body/div[1]/div[10]/div/div[2]/section[2]/div/div/div/div[1]/div/table/tbody/tr[5]/td[2]/span/text()').get()))
        item['roi_5y']=TryalSpider.clean_roi(str(response.xpath('/html/body/div[1]/div[10]/div/div[2]/section[2]/div/div/div/div[1]/div/table/tbody/tr[6]/td[2]/span/text()').get()))
        item['roi_10y']=TryalSpider.clean_roi(str(response.xpath('/html/body/div[1]/div[10]/div/div[2]/section[2]/div/div/div/div[1]/div/table/tbody/tr[7]/td[2]/span/text()').get()))
        item['age']=response.xpath('/html/body/div[1]/div[10]/div/div[1]/div[4]/div/div/div/table/tbody/tr[7]/td[2]/text()').get()
        item['risk']=response.xpath('/html/body/div[1]/div[10]/div/div[3]/div[1]/div/div/p/span/text()').get()
        item['lockdown_duration']=response.xpath('/html/body/div[1]/div[10]/div/div[1]/div[4]/div/div/div/table/tbody/tr[6]/td[2]/text()').get()
        item['cat']=response.xpath('/html/body/div[1]/div[9]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[1]/a[1]/span/text()').get()
        item['sub_cat']=response.xpath('/html/body/div[1]/div[9]/div[1]/div[1]/div/div/div[2]/div[1]/div/div[1]/a[2]/span/text()').get()
        if(v_val==""):
            item['val']=float(0)
        else:
            v_val=v_val.replace(',','')
            item['val']=float((v_val.split(' ')[0])[1:])
        print(item)
        yield item
        
    
    

