import time
import json
import csv
import urllib2
import requests
import sys
import datetime
import calendar
import fileinput

timestamp = datetime.datetime.now()
h = timestamp.hour
m = timestamp.minute

time_now = str(h)+':'+str(m)
#print time_now

d = timestamp.day
mo = timestamp.month
mon = calendar.month_abbr[mo]
y = timestamp.year

date_today = '_' + str(d)+'_'+str(mon)+'_'+str(y)
#print date_today


#filename = 'sk_csv_' + timestr + '.csv'
#print timestr2
#print filename
filename =  'sk_csv_'+time_now+date_today+'.csv'
print filename

url = " " #give the url you want to take the json data from

r = requests.get(url)
data = r.json() #got all the json data from the link in data

#print data
f_master = csv.writer(open("master_csv.csv", "a"))
f = csv.writer(open(filename, "wb+"))
for row in data:
    f.writerow( [row['id'], row['post_title'], row['url'], row['category'], row['no_reads']] )
    f_master.writerow( [row['id'], row['post_title'], row['url'], row['category'], row['no_reads']]  ) 


#remove duplicates from the csv file 
f1 = csv.reader(open('master_csv.csv', 'rb'))
writer = csv.writer(open("master_csv_without_duplicates.csv", "wb"))
phone_numbers = set()
for row in f1:
    if row[1] not in phone_numbers:
        writer.writerow(row)
        phone_numbers.add( row[1] )