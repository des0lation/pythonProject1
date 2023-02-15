import numpy as np
import requests
import threading
import time,math

lock = threading.Lock()
end_version = []

highest_major = 0
highest_minor = 0
highest_patch = 0

data = requests.get("http://127.0.0.1:8000/versions").text
t_now = time.time()
data = data.replace("V", "").split("\\n")[1:-1]
data_len = len(data)

versions = np.array([list(map(int, x.split("."))) for x in data])

def process_version(highest_major, highest_minor, highest_patch):
    global end_version
    indices = np.where((versions[:,0] >= highest_major) &
                       (versions[:,1] >= highest_minor) &
                       (versions[:,2] >= highest_patch))
    if len(indices[0]) > 0:
        index = indices[0][-1]
        highest_version = ".".join(map(str, versions[index]))
        if highest_version not in end_version:
            with lock:
                end_version.append(highest_version)

for i in range(0, 8):
    list_size = math.ceil(data_len / 8)
    start_index = i * list_size
    end_index = min(start_index + list_size, data_len)
    thread_data = versions[start_index:end_index]
    t = threading.Thread(target=process_version, args=(highest_major, highest_minor, highest_patch))
    t.start()

for t in threading.enumerate():
    if t != threading.current_thread():
        t.join()

print(end_version)
t_done = time.time()
print("Time taken is", t_done - t_now)
