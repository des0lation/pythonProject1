import requests
import time

data = requests.get("http://127.0.0.1:8000/versions").text
versions = data.strip("\"").split("\\nV")[1:]
new_versions = []

t_1 = time.perf_counter()
versions = set(versions)
print("Searching set reduced to",len(versions))
previous_version = tuple([0,0,0])
for i in versions:
    i = tuple(map(int, i.split(".")))
    if i > previous_version:
        new_versions.append(i)
        previous_version = i

maxs = max(new_versions)
t_2 = time.perf_counter()
print(maxs,"Time Taken is",t_2 - t_1)
