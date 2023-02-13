import requests, json,time,zlib
import time, numpy as np

def lz77_decode(data):
    text = zlib.decompress(data).decode()
    return text


t_now = time.time()
data = requests.get("http://127.0.0.1:8000/versions").text
data = data.replace("V","").replace('"','').split("\\n")
data.pop(0)


values = []
for i in data:
    form = np.array([10000, 99, 0.99])
    x = i.split(".")
    x2 = np.array([int(i) for i in x])
    values.append(np.dot(x2,form))

index = values.index(max(values))
print(data[index])


t_done = time.time()
print("Time taken is",t_done - t_now)



