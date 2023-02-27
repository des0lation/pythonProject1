import time
from requests import get
import threading,math,time
data = list(set(get("http://127.0.0.1:8000/versions").text[1:-1].split("\\nV")[1:]))
t_1 = time.perf_counter()
maxs = []
def sort_versions(data_chunk):
    maxs.append(max(tuple(tuple(int(x) for x in version.split(".")) for version in data_chunk)))
    return

data_len = len(data)
x = 300
threads = []

for i in range(0,x):
    start = math.floor(i*len(data)/x)
    end = min(math.floor((i+1)*len(data)/x),data_len)
    thread = threading.Thread(target = sort_versions ,args = [data[start:end]])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print(max(set(maxs)))
t_2 = time.perf_counter()
print("Time Taken is",t_2 - t_1)

