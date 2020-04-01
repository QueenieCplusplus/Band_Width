# 4/01, am 8:45 - 10:00 (duration: 75 mins)
# DVD numbers calculation
# COL : 17 lines
# we define time in sec unit, and speed in Mbps unit.

from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from datetime import timedelta

# Constant ---->
BandWidth_speed = 100000000 #bit/s
DVD_storage_bytes = 4.7 #GB

# month = time.strptime('00:01: 00,000'.split(',')[0],'%H:%M:%S'
# may_end = date.today() + relativedelta(months=+1)
# april_start = date.today()
# Time parser ---->

days_passed= datetime(2020, 5, 1) - datetime(2020, 4, 1)

month2day = days_passed.days

day2sec = month2day * 3600 * 24
print(day2sec) # 2592000

arregate_bits= day2sec * BandWidth_speed 
print(arregate_bits) #51840000 DVD in bits can be played in this Bandwith for 1 month

def GB2Bytes (gb_figure):
    dvd_bytes = gb_figure * 1000 * 1000000
    print(dvd_bytes)
    return(dvd_bytes) # 4700000000

DVD_storage_in_bytes= GB2Bytes(DVD_storage_bytes)

def convertor(bytes):
    bits = bytes * 0.125
    return bits

DVD_storage_in_bits= convertor(DVD_storage_in_bytes)
print(DVD_storage_in_bits) # 587500000

def DVD_number_checker(in_total_bits):
    out_num = in_total_bits /DVD_storage_in_bits
    return out_num

dvd_consumed_amount = DVD_number_checker(arregate_bits)
print("we played ",dvd_consumed_amount ,"DVD in this bandwidth for a month.") # 441191

