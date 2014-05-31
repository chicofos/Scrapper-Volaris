import sys
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from Scrapper_v1.spiders.flight_spider import FlightSpider
from scrapy.utils.project import get_project_settings

#Arguments
print 'Argument List:', str(sys.argv)

spider = FlightSpider(sal=str(sys.argv[1:][0]),des=str(sys.argv[2:][0]),fecha=str(sys.argv[3:][0]))
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
reactor.run() 
# the script will block here until the spider_closed signal was sent
