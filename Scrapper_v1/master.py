import time
from subprocess import call
from calendar import monthrange
from time import strptime
from pymongo import Connection
from datetime import date

connection = Connection('localhost', 27017)
db = connection['flights']  

jan = monthrange(2014, 1)
february = monthrange(2014, 2)
march = monthrange(2014, 3)
april = monthrange(2014, 4)
may = monthrange(2014, 5)
june = monthrange(2014, 6)
july = monthrange(2014, 7)
august = monthrange(2014, 8)
september = monthrange(2014, 9)
october = monthrange(2014, 10)
november = monthrange(2014, 11)
december = monthrange(2014, 12)

meses = [
	# {'Jan' : jan[1]},
	# {'Feb' : february[1]},
	# {'Mar' : march[1]},
	# {'Apr' : april[1]},
	# {'May' : may[1]},
	# {'Jun' : june[1]},
	# {'Jul' : july[1]},
	{'Aug' : august[1]},
	{'Sep' : september[1]},
	{'Oct' : october[1]},
	{'Nov' : november[1]},
	{'Dec' : dicember[1]},
	]

#loop months
for j in range(len(meses)):

	collection = db[str(meses[j].keys()[0]) + str(date.today().year)]

	if collection.name in db.collection_names():
		collection.drop()  

	mes = strptime(meses[j].keys()[0], '%b').tm_mon

	#meses[j].itervalues().next()+1
	for i in range(1,meses[j].itervalues().next()+1):
		call(["python","runner.py","TIJ","CEN","2014-%s-%s" % (mes,i)])
		time.sleep(2)
	#createMonth(meses[j].keys()[0])	

