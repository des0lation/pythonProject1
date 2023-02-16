import requests,time,threading,math,numpy as np,cProfile,pstats
results = []
highest_major = 0
highest_minor = 0
highest_patch = 0

def process_version(data):
    global results
    local = threading.local()
    local.highest_major = 0
    local.highest_minor = 0
    local.highest_patch = 0
    local.current_major = 0
    local.current_minor = 0
    local.current_patch = 0
    local.new_data = []
    local.new_data2 = []
    counter = 0
    for x in data[0:5]:
        x = x.split(".")
        local.current_major = int(x[0])
        local.current_minor = int(x[1])
        local.current_patch = int(x[2])
        if local.current_major >= local.highest_major:
            local.highest_major = local.current_major
            if local.current_minor >= local.highest_minor:
                local.highest_minor = local.current_minor
                if local.current_patch >= local.highest_patch:
                    local.highest_patch = local.current_patch
    for x in data:
        x = x.split(".")
        if int(x[0]) > local.highest_major:
            local.highest_major = int(x[0])
            local.new_data.append(x)
    for x in local.new_data:
        counter += 1
        if int(x[1]) > local.highest_minor:
            local.highest_minor = int(x[1])
            local.new_data2.append(x)
    for x in local.new_data2:
        if int(x[2]) > local.highest_patch:
            local.highest_patch = int(x[2])




data = requests.get("http://127.0.0.1:8000/versions").text
data = data.strip("\"").split("\\nV")
data.pop(0)
data_len = len(data)
list_size = math.ceil(data_len / 100)

t_1 = time.perf_counter()

with cProfile.Profile() as pr:
    for i in np.arange(0,data_len,list_size):
        t = threading.Thread(target=process_version, args=[data[i:i+list_size]])
        t.start()
    while t.is_alive() == True:
        continue

t_2 = time.perf_counter()


stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()
print(t_2-t_1)