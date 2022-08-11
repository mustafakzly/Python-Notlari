from datetime import datetime
from datetime import timedelta
#from datetime improt time
#from datetime improt date

simdi = datetime.now()
simdi = datetime.today()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second
result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')
result = datetime.strftime(simdi,'%X')
result = datetime.strftime(simdi,'%d')
result = datetime.strftime(simdi,'%A')
result = datetime.strftime(simdi,'%B')
result = datetime.strftime(simdi,'%Y %B %A')

t = '15 April 2019 hour 10:12:30'
result = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

birthday = datetime(2000,11,16,12,11,10)
result = datetime.timestamp(birthday) #saniye
result = datetime.fromtimestamp(result) #saniye to datetime
result = datetime.fromtimestamp(0)

result = simdi - birthday
#result = result.days
#result = result.seconds
#result = result.microseconds
result = simdi + timedelta(days = 10)
print(result)