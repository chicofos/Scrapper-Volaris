import calendar, json
from datetime import date
from time import gmtime, strftime
from pymongo import MongoClient

class MongoPipeline(object):

	#create Json file
    # def __init__(self):
    # 	temp = strftime("data_%Y%m%d%H%M%S.json", gmtime())
    #     self.file = open(temp, 'wb')

    def process_item(self, item, spider):
    	#save json file
        # line = json.dumps(dict(item))
        # self.file.write(line)

        #Connect and save item in mongodb
    	db = MongoClient().flights
    	col = calendar.month_abbr[int(str(item['fecha'])[8:-5])] + str(date.today().year)
    	collection = db[col]
     	collection.insert(dict(item))
        return item