import pandas as pd 

#get the data
column_names=['user_id','item_id','rating','timestamp']
df=pd.read_csv('file.tsv',sep='\t',names=column_names)
df.head()