#import glob,json,ast,io,os
from subprocess import call
import time
from calendar import monthrange
from time import strptime
from pymongo import Connection
from datetime import date

connection = Connection('localhost', 27017)
db = connection['flights']  

mayo = monthrange(2014, 5)
junio = monthrange(2014, 6)
julio = monthrange(2014, 7)
agosto = monthrange(2014, 8)
septiembre = monthrange(2014, 9)
octubre = monthrange(2014, 10)
noviembre = monthrange(2014, 11)
diciembre = monthrange(2014, 12)

meses = [
	# {'May' : mayo[1]},
	# {'Jun' : junio[1]},
	# {'Jul' : julio[1]},
	{'Aug' : agosto[1]}
	# {'Sep' : septiembre[1]},
	# {'Oct' : octubre[1]},
	# {'Nov' : noviembre[1]},
	# {'Dec' : diciembre[1]},
	]

# def createMonth(month):
# 	data = []
# 	files = sorted(glob.glob("*.json"))
# 	for filename in files:
# 		with open(filename) as fp:
# 			doc = json.load(fp)
# 			doc = ast.literal_eval(json.dumps(doc))
# 			data.append(doc)
# 			os.remove(filename)

# 	with io.open('data_%s.txt' % month, 'w+', encoding='utf-8') as f:
# 		f.write(unicode(json.dumps(data, ensure_ascii=False)))

#loop months
for j in range(len(meses)):

	collection = db[str(meses[j].keys()[0]) + str(date.today().year)]

	if collection.name in db.collection_names():
		collection.drop()  

	mes = strptime(meses[j].keys()[0], '%b').tm_mon

	#meses[j].itervalues().next()+1
	for i in range(1,4):
		call(["python","runner.py","TIJ","CEN","2014-%s-%s" % (mes,i)])
		time.sleep(2)
	#createMonth(meses[j].keys()[0])	

