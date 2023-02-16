import requests,time,threading,math,numpy as np,cProfile,pstats
from functools import cache,lru_cache
results = []
highest_major = 0
highest_minor = 0
highest_patch = 0



data = requests.get("http://127.0.0.1:8000/versions").text
t_1 = time.perf_counter()
data = data.strip("\"").split("\\nV")
data.pop(0)
data_len = len(data)
list_size = math.ceil(data_len / 100)
data_new = []
@lru_cache(maxsize=10)
def find_max(data):
    data = tuple(data)
    highest_major = 0
    highest_minor = 0
    highest_patch = 0
    for x in data:
        x = x.split(".")
        current_major = int(x[0])
        current_minor = int(x[1])
        current_patch = int(x[2])
        if current_major >= highest_major:
            highest_major = current_major
            if current_minor >= highest_minor:
                highest_minor = current_minor
                if current_patch >= highest_patch:
                    highest_patch = current_patch
    return highest_major, highest_patch, highest_minor

find_max(data)
stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()