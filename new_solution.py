import requests,time, re, threading, numpy as np, math

data = requests.get("http://127.0.0.1:8000/versions").text
pattern = r"\d+\.\d+\.\d+"
data = re.findall(pattern, data)
t_1 = time.perf_counter()
majors = []
minors = []
patches = []
data_new = []
def splits(data):
    for i in data:
        i = i.split(i)
        data_new.append(i)

data_len = len(data)

list_size = math.ceil(data_len / 20)
threads = []
t_1 = time.perf_counter()
for i in np.arange(0, data_len, list_size):
    t = threading.Thread(target=splits, args=[data[i:i + list_size]])
    t.start()
    threads.append(t)
t_2 = time.perf_counter()
print("Time Taken is", t_2 - t_1)