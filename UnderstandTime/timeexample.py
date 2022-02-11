from datetime import date,datetime
import time

# TIME EXAMPLE 001
# while True:
#   localtime = time.localtime()
#   result = time.strftime("%I:%M:%S %p", localtime)
#   print(result)
#   time.sleep(1)

#TIME EXAMPLE 002
# while True:
#     from datetime import datetime
#     now = datetime.now()  
#     print ("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)) 
#     time.sleep(1)

#TIME EXAMPLE 003 แสดงให้เห็นการเปลี่ยนแปลงของเวลาในบรรทัดเดียวกัน 
while True:
    localtime = time.localtime()
    result = time.strftime("%m/%d/%Y %H:%M:%S",localtime)
    print (result, end="", flush=True)
    print("\r", end="", flush=True) # use this code to freeze time message
    time.sleep(1)

