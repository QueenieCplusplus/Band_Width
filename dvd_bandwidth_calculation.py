# 4/01, am 8:45 - 9:10 (duration: 25 mins)
# DVD numbers calculation
# COL : 17 lines
# we define time in sec unit, and speed in Mbps unit.

from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from datetime import timedelta

# Constant ---->
DVD_speed = 5 #Mbit/s # MPEG2 Compression
BandWidth_speed = 100 #Mbit/s
DVD_storage_bytes = 700 # not bit

# month = time.strptime('00:01: 00,000'.split(',')[0],'%H:%M:%S'
# may_end = date.today() + relativedelta(months=+1)
# april_start = date.today()
# Time parser ---->

days_passed= datetime(2020, 5, 1) - datetime(2020, 4, 1)

month2day = days_passed.days

day2sec = month2day * 3600 * 24
print(day2sec) # 2592000

DVD_played_arregate_bits= day2sec * BandWidth_speed / DVD_speed
print(DVD_played_arregate_bits) #51840000 DVD numbers can be played in this Bandwith for 1 month

def convertor(bytes):
    bits = bytes / 0.125
    return bits

DVD_storage_bits= convertor(DVD_storage_bytes)
print(DVD_storage_bits) # 5600

def dvd_number_checker(in_total_bits):
    out_num = in_total_bits /DVD_storage_bits
    return out_num

dvd_consumed_amount = dvd_number_checker(DVD_played_arregate_bits)
print(dvd_consumed_amount) # 9257

