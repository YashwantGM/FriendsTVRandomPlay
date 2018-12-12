#Code written on 30/09/2018
#
import pyodbc as po
import os
import pandas as pa
import configparser as cp

def sqlOperation(dataframe,dict_of_columns):
	con = po.connect("driver={SQL Server Native Client 11.0};"
							"server=LAPTOP-STDN3CBM;" "Database=CSV_SQL;"
							"trusted_connection=yes;")
	cur = con.cursor()
	question_mark = '?'
	#Parameter markers in insert query
	paramMarker = str(tuple([question_mark for tb_column in range(0,len(dict_of_columns))]))
	q = paramMarker.split('\'')
	paramMarker = ''.join(q)
	#Table columns in insert query
	tbColumns = str(tuple(tb_column for tb_column in dict_of_columns.values()))
	c = tbColumns.split('u')
	b = ''.join(c)
	d = b.split('\'')
	tbColumns = ''.join(d)
	#Insert query
	query = "insert into NameCSV"+tbColumns+"values"+paramMarker
	list_data = []
	cols = []
	#iterate through the dataframes
	for col in dict_of_columns.keys():
		cols.append(col)
	#Iterating through dataframes
	for index,row in dataframe.iterrows():
		#print row
		list_data.append(tuple(row[col] for col in cols))
	#execute query for insertion
	cur.executemany(query,list_data)
	print 'successful insertion'
	cur.commit()
	con.close()

def getCSV():
	file_list = [f for f in os.listdir('G:\CSV_Surgery\csvFiles') if os.path.isfile(os.path.join('G:\CSV_Surgery\csvFiles', f))]
	for file in file_list:
		if file.endswith('.ini'):
			config = cp.ConfigParser()
			dict1 = {}
			config.read('G:\CSV_Surgery\csvFiles\\'+file)
			sections = config.sections()
			for section in sections:
				if section == 'columns':
					options = config.options(section)
					for option in options:
						dict1[option] = config.get(section,option)
			continue
		else:
			df = pa.read_csv('G:\CSV_Surgery\csvFiles\\'+file)
		sqlOperation(df,dict1)
			#print df

#def getOption():

if __name__ == '__main__':
	getCSV()
