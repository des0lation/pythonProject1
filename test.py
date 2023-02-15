import math

import requests,time,threading,math

end_version = []
lock = threading.Lock()

dict = {
    "highest_major": 0,
    "highest_minor": 0,
    "highest_patch": 0
}
def process_version(data,dict):
    highest_version = None
    with lock:
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
        return end_version

data = requests.get("http://127.0.0.1:8000/versions").text


t_now = time.time()
data = data.replace("V", '').split("\\n")
data.pop(0)
data_len = len(data)
list_size = math.ceil(len(data) / 8)
datas = [data[i:i+list_size] for i in range(0, len(data), list_size)]

t1 = threading.Thread(target=process_version,args =(datas[0],dict))
t2 = threading.Thread(target=process_version, args =(datas[1],dict))
t3 = threading.Thread(target=process_version, args =(datas[2],dict))
t4 = threading.Thread(target=process_version, args =(datas[3],dict))
t5 = threading.Thread(target=process_version, args =(datas[4],dict))
t6 = threading.Thread(target=process_version, args =(datas[5],dict))
t7 = threading.Thread(target=process_version, args =(datas[6],dict))
t8 = threading.Thread(target=process_version, args =(datas[7],dict))

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
