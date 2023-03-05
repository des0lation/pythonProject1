import time,math
from requests import get
import threading

data = list(set(get("http://127.0.0.1:8000/versions").text[1:-1].split("\\nV")[1:]))

t1 = time.perf_counter()
maxs = []
versions = {}
def form_sorted_dict(data_x):
    for version in data_x:
        version_tuple = tuple(map(int, version.split(".")))
        versions[version_tuple] = version
    maxs.append(max(versions.keys()))

x = 1
data_len = len(data)
threads = []

for i in range(0,x):
    start,end = math.floor(i*len(data)/x),min(math.floor((i+1)*len(data)/x),data_len)
    thread = threading.Thread(target = form_sorted_dict ,args = [data[start:end]])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

t2 = time.perf_counter()

print(max(maxs), t2 - t1)
