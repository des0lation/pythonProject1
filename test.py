import requests,time,threading,math,numpy as np
results = []
def process_version(data):
    global results
    local = threading.local()
    local.highest_major = 0
    local.highest_minor = 0
    local.highest_patch = 0
    for i in data:
        x = i.split(".")
        current_major = int(x[0])
        if current_major >= local.highest_major:
            current_minor = int(x[1])
            local.highest_major = current_major
            if current_minor >= local.highest_minor:
                current_patch = int(x[2])
                local.highest_minor = current_minor
                if current_patch >= local.highest_patch:
                    local.highest_patch = current_patch
    results.append([local.highest_major,local.highest_minor,local.highest_patch])

data = requests.get("http://127.0.0.1:8000/versions").text
t_1 = time.perf_counter()
data = data.strip("\"").split("\\nV")
data.pop(0)
data_len = len(data)
list_size = math.ceil(data_len / 3)
t_2 = time.perf_counter()
threads = []
for i in np.arange(0,data_len,list_size):
    t = threading.Thread(target=process_version, args=[data[i:i+list_size]])
    t.start()
    threads.append(t)

for thread in threads:


print("Total Time Taken",t_4-t_1)