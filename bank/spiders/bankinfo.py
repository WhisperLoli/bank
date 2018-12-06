# -*- coding: utf-8 -*-
import scrapy
from bank.items import BankItem
import re

class BankinfoSpider(scrapy.Spider):
    name = 'bankinfo'
    allowed_domains = ['lianhanghao.com']
    start_urls = ['http://lianhanghao.com/index.php/Index/index/p/1.html']

    def parse(self, response):
        trs = response.xpath("/html/body/div[3]/div[3]/table/tbody/tr")
        for tr in trs:
            item = BankItem()
            item["bank_number"] = tr.xpath("./td[1]/text()").extract_first()
            item["bank_name"] = tr.xpath("./td[2]/text()").extract_first()
            item["bank_telephone"] = re.sub("\s+|\|","",tr.xpath("./td[3]/text()").extract_first())
            item["bank_address"] = tr.xpath("./td[4]/text()").extract_first()
            yield (item)

        next = response.xpath("/html/body/div[3]/div[3]/table/tfoot/tr/td/div/div/span[@class='current']/following-sibling::a[1]/@href").extract_first()
        if next:
            yield (scrapy.Request("http://lianhanghao.com" + next, self.parse))