#current time

import time

currentTime = time.time()       #UNIX epoch time

totalSecond = int(currentTime)
currentSecond = totalSecond%60

totalMinute = totalSecond//60
currentMinute = totalMinute%60

totalHour = totalMinute//60
currentHour = totalHour%24

print(currentHour,':',currentMinute,':',currentSecond)
