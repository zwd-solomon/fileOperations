
import json
import csv

infilename = 'meal_info.json' 
oufile = 'meal_info.csv'

# mapping json file to csv
def json_to_csv():
	with open(infilename,'r') as fp:
		jsonls = json.load(fp)
		with open(outfile,'w+') as fpOut:
			header_ = ['meal_id','category','cuisine']
			OWriter = csv.DictWriter(fpOut, header_)
			OWriter.writeheader()
			for element in jsonls:
				OWriter.writerow(element)

with open(file2, 'w+') as fp2:

	filewriter = csv.writer(fp2)
	## csv header ??? 	fieldnames = ['meal_id','category','cuisine']
	for element in jsonls:
		filewriter.writerow(element.values())

with open(filename) as fp_: 
	fieldnames = ['meal_id','category','cuisine']
	reader_ = csv.DictReader(fp_, fieldnames)
