# -*- encoding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from datetime import datetime
from Scrapper_v1.items import FlightsItem

class FlightSpider(Spider):

	name = "spiderman"

	def __init__(self, sal=None, des=None, fecha=None, *args, **kwargs):
		super(FlightSpider, self).__init__(*args, **kwargs)

		ciudades = { 'TIJ': 'Tijuana (TIJ)', 'CEN': 'Ciudad Obregón (CEN)'}

		salida = ciudades[sal]
		destino = ciudades[des]

		fecha = datetime.strptime(fecha, '%Y-%m-%d')
		fecha_formato = fecha.strftime("%b %d, %Y")

		self.allowed_domains = ["reservaciones.volaris.com"]
		self.start_urls = [	
			"https://reservaciones.volaris.com/Flight/DeepLinkSearch?s=true&culture=es-MX&r=false&c=false&other-departCity=%s&o1=%s&other-returnCity=%s&d1=%s&promocode-select=&P=&dateDeparture=May+22,+2014&dd1=%s&dateArrival=%s&cc=MXN&ADT=1&CHD=0&i=0&submit=" % (salida,sal,destino,des,fecha,fecha_formato)
			]
	
	def parse(self,response):

		sel = Selector(response)
		item = FlightsItem()

		try:
			item['salida'] = sel.select('//*[@id="sortedAvailability0"]/table/tbody/tr[2]/td[1]/span[1]/span[1]/text()').extract()[0]
			item['hora_salida'] = sel.select('//*[@id="sortedAvailability0"]/table/tbody/tr[2]/td[1]/span[1]/text()').extract()[0].strip()
			item['destino'] = sel.select('//*[@id="sortedAvailability0"]/table/tbody/tr[2]/td[1]/span[2]/span/text()').extract()[0]
			item['hora_destino'] = sel.select('//*[@id="sortedAvailability0"]/table/tbody/tr[2]/td[1]/span[2]/text()').extract()[0].strip()
			item['vuelo'] = sel.select('//*[@id="sortedAvailability0"]/table/tbody/tr[2]/td[1]/span[3]/text()').extract()[0].strip()
			item['asientos'] = sel.select('//div[@class="seat-number"]/text()').extract()[0]
			item['tarifa_regular'] = sel.select('//td[@class="fare-price-display"]/label/text()').extract()[0].strip()
			item['fecha'] = sel.select('//*[@id="roundTripSearch_DepartureDate"]/attribute::value').extract()

		except Exception, e:
			item['fecha'] = sel.select('//*[@id="roundTripSearch_DepartureDate"]/attribute::value').extract()
			item['error'] = 'No Disponible'

		# Vuelta
			#TODO

		return item

		