import requests, json,time
import time
t_now = time.time()
data = requests.get("http://127.0.0.1:8000/versions/previous").text
t_done = time.time()
print(t_done-t_now)



