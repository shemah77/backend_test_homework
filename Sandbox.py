
import datetime as dt

i = input('Enter date',)


d = dt.datetime.strptime(i,'%d-%m-%Y')

print (d)

