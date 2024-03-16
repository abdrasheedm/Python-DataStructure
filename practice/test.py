import datetime
import time

s = time.time()
print(s)
time.sleep(5)
b = datetime.datetime.now()

print(b-s)