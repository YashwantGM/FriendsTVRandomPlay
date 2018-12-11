import pandas as pd 
df = pd.read_csv("D:\\MyProjects\\Backup\\AmazonBasic\\IN\\ARABasic_IN_20180902.csv")
df1 = pd.read_csv("D:\\MyProjects\\Backup\\AmazonBasic\\IN\\ARABasic_IN_20180902.csv")

df2 = pd.concat([df,df1])
print(df2)
# print(df['ASIN'])#,df1)
# if (df == df1).all().all():
# 	print("True")
# else:
# 	print("Flase")
df2.to_csv("output3.csv", sep=',')
