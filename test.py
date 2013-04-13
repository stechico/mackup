import ConfigParser
import json
from pprint import pprint

# config = ConfigParser.SafeConfigParser()
# config.read('sample.ini')

json_data = open('sample.json')
data = json.load(json_data)
json_data.close()
pprint(data)
