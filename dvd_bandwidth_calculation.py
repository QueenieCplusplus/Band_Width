# 4/01, am 8:45 - 9:10 (duration: 25 mins)
# DVD numbers calculation
# COL : 7 lines
# we define time in sec unit, and speed in Mbps unit.

from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from datetime import timedelta

# Constant ---->
DVD_speed = 5 #Mbit/s # MPEG2 Compression

BandWidth_speed = 100 #Mbit/s

# month = time.strptime('00:01: 00,000'.split(',')[0],'%H:%M:%S'
# may_end = date.today() + relativedelta(months=+1)
# april_start = date.today()
# Time parser ---->

days_passed= datetime(2020, 5, 1) - datetime(2020, 4, 1)

month2day = days_passed.days

day2sec = month2day * 3600 * 24
print(day2sec) # 2592000

DVD_played_numbers= day2sec * BandWidth_speed / DVD_speed
print(DVD_played_numbers) #51840000 DVD numbers can be played in this Bandwith for 1 month