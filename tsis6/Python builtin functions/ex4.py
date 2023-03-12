import math
a=int(input())
time=int(input())
millitime=time/1000
root=math.sqrt(a)
from threading import Timer
def timeroot():
    print ("Square root of", a, "after", time, "miliseconds is", root )
abc=Timer(millitime, timeroot)
abc.start()