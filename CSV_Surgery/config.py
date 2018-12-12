import configparser as cp

config = cp.ConfigParser()
dict1 = {}
config.read('G:\CSV_Surgery\csvFiles\column.ini')
sections = config.sections()
for section in sections:
	if section == 'columns':
		options = config.options(section)
		for option in options:
			dict1[option] = config.get(section,option)

print dict1
t = tuple(tb_column for tb_column in dict1.values())
v = tuple(tb_column for tb_column in dict1.keys())
print t
print v