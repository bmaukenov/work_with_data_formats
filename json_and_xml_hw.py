import json
import collections
from pprint import pprint 
import xml.etree.ElementTree as ET


def json_most_common(file_name):
	with open(file_name) as json_file:
		json_data = json.load(json_file)


	items = json_data["rss"]["channel"]["items"]

	json_result = collections.Counter()

	for item in items:
		descr_list = item["description"].split()
		for word in descr_list:
			if len(word) > 6:
				json_result[word] += 1



	pprint(json_result.most_common(10))
	print("\n")




def xml_most_common(file_name):

	tree = ET.parse(file_name)
	root = tree.getroot()
	items = root.findall("channel/item")

	xml_result = collections.Counter()

	for item in items:
		descr_list = item.find("description").text.split()
		for word in descr_list:
			if len(word) > 6:
				xml_result[word] += 1



	pprint(xml_result.most_common(10))
	print("\n")

	

json_most_common("newsafr.json")
xml_most_common("newsafr.xml")

