import pandas as pd 
import pyodbc as po 
import os
import configparser 

CSV_FILES_FOLDER = 'G:\CSV_Surgery\csvFiles'
INSERT_STATEMENT = """INSERT INTO NameCSV(col1,col2) values(\'fnameValue\',\'lnameValue\')"""
# CONNECTION_STRING = """Driver={SQL Server Native Client 11.0};
# 							Server=LAPTOP-STDN3CBM; Database= Names;
# 							trusted_connection=yes;"""

def executeQuery(query):
	print query
	cnxn = po.connect("driver={SQL Server Native Client 11.0};"
							"server=LAPTOP-STDN3CBM;" "Database=Names;"
							"trusted_connection=yes;")
	cur = cnxn.cursor()
	cur.execute(query)
	cnxn.close()

def createQuery(firstname,lastname,column1,column2):
	#print column1
	query = INSERT_STATEMENT
	query = query.replace('col1',str(column1))
	query = query.replace('col2',str(column2))
	query = query.replace('fnameValue',str(firstname))
	query = query.replace('lnameValue',str(lastname))
	executeQuery(query)

def readDF(dataFrame, column1, column2):
	#print dataFrame
	for index,row in dataFrame.iterrows():
		firstname = row['firstname']
		lastname = row['lastname']
		createQuery(firstname,lastname,column1,column2)

def readIni_CSV(fileList):
	column1 = ''
	column2 = ''
	df = ''
	for eachFile in fileList:
		if eachFile.endswith('.ini'):
			config = configparser.ConfigParser()
			config.read(CSV_FILES_FOLDER+'\\'+eachFile)
			column2 = config.get('columns','lastname')
			column1 = config.get('columns','firstname')
		else:
			df = pd.read_csv(CSV_FILES_FOLDER+'\\'+eachFile)
			readDF(df,column1,column2)
def getFileList():
	return [f for f in os.listdir(CSV_FILES_FOLDER) if os.path.isfile(os.path.join(CSV_FILES_FOLDER, f))]

def main():
	fileList = getFileList()
	print fileList
	readIni_CSV(fileList)

if __name__ == '__main__':
	main()