import requests,time,threading,math,numpy as np
results = []
highest_major = 0
highest_minor = 0
highest_patch = 0

lock = threading.Lock()
results = []

def process_version(data):
    global results,highest_major,highest_minor,highest_patch
    local = threading.local()
    local.highest_major = 0
    local.highest_minor = 0
    local.highest_patch = 0
    for i in data:
        x = i.split(".")
        current_major = int(x[0])
        if current_major >= highest_major and current_major >= local.highest_major:
            current_minor = int(x[1])
            local.highest_major = current_major
            if current_minor >= highest_minor and current_minor >= local.highest_minor:
                current_patch = int(x[2])
                local.highest_minor = current_minor
                if current_patch >= highest_patch and current_patch >= local.highest_patch:
                    local.highest_patch = current_patch
    results.append([local.highest_major,local.highest_minor,local.highest_patch])




data = requests.get("http://127.0.0.1:8000/versions").text
t_1 = time.perf_counter()
data = data.strip("\"").split("\\nV")
data.pop(0)
print(len(data))
t_3 = time.perf_counter()
for i in data[0:10]:
    x = i.split(".")
    current_major = int(x[0])
    current_minor = int(x[1])
    current_patch = int(x[2])
    if current_major >= highest_major:
        highest_major = current_major
        if current_minor >= highest_minor:
            highest_minor = current_minor
            if current_patch >= highest_patch:
                highest_patch = current_patch
t_4 = time.perf_counter()
print("Time for 10 is",t_4-t_3)
print(highest_major,highest_minor,highest_patch)
data = data[10:-1]
data_len = len(data)
list_size = math.ceil(data_len / 100)
threads = []
second_lenghts = 0
for i in np.arange(0,data_len,list_size):
    t = threading.Thread(target=process_version, args=[data[i:i+list_size]])
    t.start()
    threads.append(t)

while True:
    if t.is_alive() == True:
        continue
    else:
        t_2 = time.perf_counter()
        print(results)
        print("Time Taken is",t_2-t_1)
        break