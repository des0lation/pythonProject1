import requests
import time
import numpy as np
import multiprocessing as mp

highest_major = 0
highest_minor = 0
highest_patch = 0
def process_version(data_chunk):
    highest_version = None
    for version_str in data_chunk:
        version = np.array(version_str.split('.')).astype(np.int32)
        if version[0] > highest_major:
            highest_major = version[0]
            if version[1] > highest_minor:
                highest_minor = version[1]
                if version[2] > highest_patch:
                    highest_patch = version[2]
                    highest_version = version
    return highest_version


if __name__ == '__main__':
    data = requests.get("http://127.0.0.1:8000/versions").text
    data = data.replace("V", '').split("\\n")[1:-1]
    data = np.array(data)

    chunk_size = len(data) // mp.cpu_count()
    data_chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with mp.Pool() as pool:
        start_time = time.monotonic()
        results = pool.map(process_version, data_chunks)
        end_time = time.monotonic()
        print(f"Found highest version: {'.'.join(results[-1].astype(str))}")
        print(f"Time taken is {end_time - start_time} seconds")
