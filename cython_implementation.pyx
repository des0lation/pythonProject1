# cython: language_level=3
import requests
import time
import threading
import math
import numpy as np
cimport numpy as np

# Declare typed memoryviews for performance improvements
cdef int[:,:] datas
cdef int[:, ::1] end_version

# Use the GIL-releasing nogil directive for multithreading
cdef process_version(data, int highest_major, int highest_minor, int highest_patch, int[:, ::1] end_version) nogil:
    cdef str x
    cdef int major, minor, patch
    cdef str[:] version
    cdef int[:] highest_version
    with nogil, end_version.not_none():
        for x in data:
            version = x.split('.')
            major = int(version[0])
            minor = int(version[1])
            patch = int(version[2])
            if major >= highest_major and minor >= highest_minor and patch >= highest_patch:
                highest_major = major
                highest_minor = minor
                highest_patch = patch
                highest_version = np.array([major, minor, patch], dtype=np.int32)
        end_version[0] = highest_version

def main():
    cdef str data = requests.get("http://127.0.0.1:8000/versions").text
    cdef double t_now = time.time()
    data = data.replace("V", '').split("\\n")[1:-1]
    cdef int data_len = len(data)
    cdef int list_size = math.ceil(data_len / 8)
    cdef int i
    datas = np.zeros((8, list_size), dtype=np.int32)
    for i in np.arange(0, data_len, list_size):
        datas[i // list_size] = [int(v) for v in data[i:i+list_size][-1].split('.')]
    global end_version
    end_version = np.zeros((1, 3), dtype=np.int32)
    cdef int highest_major = 0
    cdef int highest_minor = 0
    cdef int highest_patch = 0
    cdef list threads = []
    for i in range(8):
        threads.append(threading.Thread(target=process_version, args=(datas[i], highest_major, highest_minor, highest_patch, end_version)))
        threads[i].start()
    for i in range(8):
        threads[i].join()
    print(end_version[0])
    cdef double t_done = time.time()
    print("Time taken is", t_done - t_now)

if __name__ == "__main__":
    main()
