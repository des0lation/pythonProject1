import concurrent.futures
import math

import requests,time,threading,math, multiprocessing as mp


highest_major = 0
highest_minor = 0
highest_patch = 0
end_version = []
lock = threading.Lock()

dict = {
    "highest_major": 0,
    "highest_minor": 0,
    "highest_patch": 0
}
def process_version(data,highest_major,highest_minor,highest_patch):
    highest_version = None
    for version in data:
        x = version.split('.')
        if int(x[0]) >= dict['highest_major']:
            dict['highest_major'] = int(x[0])
            if int(x[1]) >= dict['highest_minor']:
                dict['highest_minor'] = int(x[1])
                if int(x[2]) >= dict['highest_patch']:
                    dict['highest_patch'] = int(x[2])
                    highest_version = x
    if highest_version not in end_version:
        end_version.append(highest_version)
    print(end_version)
    return

data = requests.get("http://127.0.0.1:8000/versions").text
data = data.replace("V", '').split("\\n")
data.pop(0)
data_len = len(data)
list_size = math.ceil(len(data) / 5)
datas = [data[i:i+list_size] for i in range(0, len(data), list_size)]

if __name__ == '__main__':
    t_now = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(process_version,[datas[0],highest_major,highest_minor,highest_patch],[datas[1],highest_major,highest_minor,highest_patch],[datas[2],highest_major,highest_minor,highest_patch],[datas[3],highest_major,highest_minor,highest_patch],[datas[4],highest_major,highest_minor,highest_patch])
    t_done = time.time()
    print("Finished in", t_done-t_now)
