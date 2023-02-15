import requests
import time
import numpy as np
import multiprocessing as mp

def process_version(data_chunk):
    highest_version = None
    for version_str in data_chunk:
        version = np.array(version_str.split('.')).astype(np.int32)
        if highest_version is None or np.greater(version, highest_version).any():
            highest_version = version
    return highest_version

if __name__ == '__main__':
    data = requests.get("http://127.0.0.1:8000/versions").text
    data = data.replace("V", '').split("\\n")[1:-1]
    data = np.array(data)

    chunk_size = len(data) // mp.cpu_count()
    datas = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with mp.Pool() as pool:
        start_time = time.monotonic()
        results = pool.map(process_version, datas)
        end_time = time.monotonic()

        # Find the highest version across all results
        max_index = np.argmax(np.array(results))
        highest_version = results[max_index]

        print(f"Found highest version: {'.'.join(highest_version.astype(str))}")
        print(f"Time taken is {end_time - start_time} seconds")
