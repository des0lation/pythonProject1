import math

import requests,time,threading,math,numpy as np

end_version = []
lock = threading.Lock()


highest_major = 0
highest_minor = 0
highest_patch = 0
values = []

def process_version(data,highest_major,highest_minor,highest_patch):
    highest_version = None
    with lock:
        for x in data:
            x = x.split('.')
            if int(x[0]) >= highest_major:
                highest_major = int(x[0])
                if int(x[1]) >= highest_minor:
                    highest_minor = int(x[1])
                    if int(x[2]) >= highest_patch:
                        highest_patch = int(x[2])
                        highest_version = x
        end_version.append(highest_version)
        return end_version


data = requests.get("http://127.0.0.1:8000/versions").text
t_now = time.time()
data = data.replace("V", '').split("\\n")[1:-1]
data_len = len(data)
list_size = math.ceil(len(data) / 8)
datas = []
for i in np.arange(0,len(data),list_size):
    datas.append(data[i:i+list_size])



t1 = threading.Thread(target=process_version,args =(datas[0],highest_major,highest_minor,highest_patch))
t2 = threading.Thread(target=process_version, args =(datas[1],highest_major,highest_minor,highest_patch))
t3 = threading.Thread(target=process_version, args =(datas[2],highest_major,highest_minor,highest_patch))
t4 = threading.Thread(target=process_version, args =(datas[3],highest_major,highest_minor,highest_patch))
t5 = threading.Thread(target=process_version, args =(datas[4],highest_major,highest_minor,highest_patch))
t6 = threading.Thread(target=process_version, args =(datas[5],highest_major,highest_minor,highest_patch))
t7 = threading.Thread(target=process_version, args =(datas[6],highest_major,highest_minor,highest_patch))
t8 = threading.Thread(target=process_version, args =(datas[7],highest_major,highest_minor,highest_patch))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()

print(end_version)
t_done = time.time()
print("Time taken is", t_done - t_now)
