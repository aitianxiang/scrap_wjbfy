# -*- coding:utf-8 -*-

import requests
from lxml import etree

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh;'  
                  ' Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Host':'www.fmprc.gov.cn',
    'Origin':'www.fmprc.gov.cn',
    'Referer':'http://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/default_1.shtml',
}

cookies = {
    'Cookie': 'user_trace_token=20180308130349-957aad79-033b-484d-8c6c-b3f1b02d9bc6;'
              'LGUID=20180308130350-17042781-228e-11e8-a0b2-525400f775ce; '
              'index_location_city=%E5%8C%97%E4%BA%AC; SEARCH_ID=e9c2777c27164f3fb3cd731328f62cc5; '
              'TG-TRACK-CODE=search_code; JSESSIONID=ABAAABAAADEAAFIF2EB6C34556E9A0844EAF7FDF02F852B; '
              'PRE_UTM=; PRE_HOST=; '
              'PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_java%3Fcity%3D%25E6%25B7%25B1%25E5%259C%25B3%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; '
              'PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2F3413383.html; _gat=1; _'
              'gid=GA1.2.807135798.1504227456; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520485431; '
              'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1520489339; _ga=GA1.2.803046708.1520485431; '
              'LGSID=20180308130350-170425a7-228e-11e8-a0b2-525400f775ce; '
              'LGRID=20180308130350-17042781-228e-11e8-a0b2-525400f775ce',
}
#fo = open("wjbfy.txt","w")
fo_2015 = open("wjbfy_2015.txt","w")
fo_2016 = open("wjbfy_2016.txt","w")
fo_2017 = open("wjbfy_2017.txt","w")
fo_2013 = open("wjbfy_2013.txt","w")
fo_2014 = open("wjbfy_2014.txt","w")
fo_2018 = open("wjbfy_2018.txt","w")

url_head = "http://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/default.shtml"
url_head_2 = "http://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/"
response = requests.get(url=url_head, headers=headers, cookies=cookies)
response.encoding = 'utf-8'
tree = etree.HTML(response.text)
neirong = tree.xpath('//*[@class="rebox_news"]/ul/li/a/@href')
for n in neirong:
    url_detail =  url_head_2+n.replace('./','')
    response2 = requests.get(url=url_detail, headers=headers, cookies=cookies)
    response2.encoding = 'utf-8'
    tree = etree.HTML(response2.text)
    title = tree.xpath('//*[@id="News_Body_Title"]/text()')
    content = tree.xpath('//*[@id="News_Body_Txt_A"]')
    print title[0][:4].encode("utf-8")
    if title[0][:4].encode("utf-8").replace(" ","")=="2018":
        fo_2018.write(title[0].encode("utf-8"))
        for c in content:
            fo_2018.write(c.xpath('string(.)').encode('utf-8').strip())
    elif title[0][:4].encode("utf-8").replace(" ","")=="2017":
        fo_2017.write(title[0].encode("utf-8"))
        for c in content:
            fo_2017.write(c.xpath('string(.)').encode('utf-8').strip())
    elif title[0][:4].encode("utf-8").replace(" ","")=="2016":
        fo_2016.write(title[0].encode("utf-8"))
        for c in content:
            fo_2016.write(c.xpath('string(.)').encode('utf-8').strip())
    elif title[0][:4].encode("utf-8").replace(" ","")=="2015":
        fo_2015.write(title[0].encode("utf-8"))
        for c in content:
            fo_2015.write(c.xpath('string(.)').encode('utf-8').strip())
    elif title[0][:4].encode("utf-8").replace(" ","")=="2014":
        fo_2014.write(title[0].encode("utf-8"))
        for c in content:
            fo_2014.write(c.xpath('string(.)').encode('utf-8').strip())
    elif title[0][:4].encode("utf-8").replace(" ","")=="2013":
        fo_2013.write(title[0].encode("utf-8"))
        for c in content:
            fo_2013.write(c.xpath('string(.)').encode('utf-8').strip())

for i in range(66):
    url_3= "http://www.fmprc.gov.cn/web/fyrbt_673021/jzhsl_673025/default_"+str(i)+".shtml"
    res3 = requests.get(url=url_3, headers=headers, cookies=cookies)
    res3.encoding = 'utf-8'
    tree3= etree.HTML(res3.text)
    neirong = tree3.xpath('//*[@class="rebox_news"]/ul/li/a/@href')
    for n in neirong:
        url_detail = url_head_2 + n.replace('./', '')
        response2 = requests.get(url=url_detail, headers=headers, cookies=cookies)
        response2.encoding = 'utf-8'
        tree = etree.HTML(response2.text)
        title = tree.xpath('//*[@id="News_Body_Title"]/text()')
        content = tree.xpath('//*[@id="News_Body_Txt_A"]')
        print title[0][:4].encode("utf-8")
        if title[0][:4].encode("utf-8").replace(" ", "") == "2018":
            fo_2018.write(title[0].encode("utf-8"))
            for c in content:
                fo_2018.write(c.xpath('string(.)').encode('utf-8').strip())
        elif title[0][:4].encode("utf-8").replace(" ", "") == "2017":
            fo_2017.write(title[0].encode("utf-8"))
            for c in content:
                fo_2017.write(c.xpath('string(.)').encode('utf-8').strip())
        elif title[0][:4].encode("utf-8").replace(" ", "") == "2016":
            fo_2016.write(title[0].encode("utf-8"))
            for c in content:
                fo_2016.write(c.xpath('string(.)').encode('utf-8').strip())
        elif title[0][:4].encode("utf-8").replace(" ", "") == "2015":
            fo_2015.write(title[0].encode("utf-8"))
            for c in content:
                fo_2015.write(c.xpath('string(.)').encode('utf-8').strip())
        elif title[0][:4].encode("utf-8").replace(" ", "") == "2014":
            fo_2014.write(title[0].encode("utf-8"))
            for c in content:
                fo_2014.write(c.xpath('string(.)').encode('utf-8').strip())
        elif title[0][:4].encode("utf-8").replace(" ", "") == "2013":
            fo_2013.write(title[0].encode("utf-8"))
            for c in content:
                fo_2013.write(c.xpath('string(.)').encode('utf-8').strip())
fo_2013.close()
fo_2014.close()
fo_2015.close()
fo_2016.close()
fo_2017.close()
fo_2018.close()




