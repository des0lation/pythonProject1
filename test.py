import requests, json,time,zlib
import time, numpy as np


data = requests.get("http://127.0.0.1:8000/versions").text
t_now = time.time()
data = data.replace("V",'').split("\\n")
data.pop(0)
highest_major = 7
highest_minor = 7
highest_patch = 7
for i in data:
    x = i.split('.')
    if int(x[0]) >= highest_major:
        highest_major = int(x[0])
        if int(x[1]) >= highest_minor:
            highest_minor = int(x[1])
            if int(x[2]) >= highest_patch:
                highest_patch = int(x[2])
                end_version = x
print(end_version)
t_done = time.time()
print("Time taken is",t_done - t_now)



