import os
import csv
import configparser as cp

#get files in a folder
file_list = [f for f in os.listdir('G:\CSV_Surgery\csvFiles') if os.path.isfile(os.path.join('G:\CSV_Surgery\csvFiles', f))]
#print file_list
#iterate through the file list
dict1 = {}
for file in file_list:
	if file == 'column.ini':
		config = cp.ConfigParser()
		config.read('G:\CSV_Surgery\csvFiles\\'+file)
		sections = config.sections()
		for section in sections:
			options = config.options(section)
			for option in options:
				dict1[option] = config.get(section,option)
		#print sections
		continue	
	else:
		with open('G:\CSV_Surgery\csvFiles\\'+file,'r') as csvFile:
			file_reader = csv.reader(csvFile)
			#for line in file_reader:
				#print line
#dict1 = {}
#iterate through sections
print dict1

