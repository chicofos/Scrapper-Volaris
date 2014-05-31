from scrapy.item import Item, Field

class FlightsItem(Item):
	salida = Field()
	hora_salida = Field()
	destino = Field()
	hora_destino = Field()
	vuelo = Field()
	asientos = Field()
	tarifa_regular = Field()
	error = Field()
	fecha = Field()
