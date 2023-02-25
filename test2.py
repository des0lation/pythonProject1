import requests
import threading
import time
import numpy as np

def process_versions(versions, new_versions, lock,prev_tuple):
    local = threading.local()
    local.versions = []
    for i in versions:
        i = tuple(map(int, i.split(".")))
        local.versions.append(i)
    local.versions.sort()
    new_versions.append(local.versions)

data = requests.get("http://127.0.0.1:8000/versions").text
versions = data.strip("\"").split("\\nV")[1:]
versions = list(set)
for i in versions:
    versions.append(map())
num_threads = 10
chunk_size = int(np.ceil(len(versions) / num_threads))
new_versions = []
lock = threading.Lock()

t_1 = time.perf_counter()
prev_tuple = tuple([0,0,0])
threads = []
for i in range(num_threads):
    start_idx = i * chunk_size
    end_idx = min((i + 1) * chunk_size, len(versions))
    thread = threading.Thread(target=process_versions, args=(versions[start_idx:end_idx], new_versions, lock, prev_tuple))
    threads.append(thread)
    thread.start()

while thread.is_alive():
    continue

t_2 = time.perf_counter()
print("Done in",t_2 - t_1,"seconds")
