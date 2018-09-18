import shlex
import json
from collections import Counter
import argparse
from tabulate import tabulate
import pandas as pd

print("Fields : ip | timestamp | version | status_code | size | url | browser")
parser=argparse.ArgumentParser(description='Apache Log Parser')
parser.add_argument('field',type=str,help='apache log field')
parser.add_argument('aggregate',nargs='?',type=str,help='Enter aggregation')
args = parser.parse_args()
data=[]

f=open('testlog.txt','r')
for line in f:
	x=shlex.split(line)
	ip_address=x[0]
	ts=x[3]+x[4]
	version=x[5]
	status_code=x[6]
	size=x[7]
	url=x[8]
	browser=x[9]
	data.append({"ip":ip_address,"timestamp":ts,"version":version,"status_code":status_code,"size":size,"url":url,"browser":browser})



field=args.field	
aggs=[]
for i in data:
	aggs.append(i[field])
#print("Fields:"+field)
#print(aggs)
table=[]
if(args.aggregate=="count"):
	c=Counter(aggs)
	for key,value in c.items():
		Col1=key
		Col2=value
		column=Col1,Col2
		table.append(column)	
print(tabulate(table,headers=['Field', 'Occurance'], tablefmt='orgtbl'))

df=pd.DataFrame(data)
df.to_csv('apache.csv', sep=',', encoding='utf-8')


	

	

	
