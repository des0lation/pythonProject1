import requests
import time
import numpy as np

data = requests.get("http://127.0.0.1:8000/versions").text
t_1 = time.perf_counter()

# Split the data into major, minor, and patch version numbers using numpy
data = np.array(data.strip("\"").split("\\nV"))
data = data[data != '']
data = np.array([list(map(int, x.split('.'))) for x in data])
major, minor, patch = np.split(data, 3, axis=1)

# Find the highest major, minor, and patch version numbers using numpy's max function
highest_major = np.max(major)
highest_minor = np.max(minor[major == highest_major])
highest_patch = np.max(patch[(major == highest_major) & (minor == highest_minor)])

t_2 = time.perf_counter()
print(highest_major, highest_minor, highest_patch)
print(f"Time taken: {t_2 - t_1:.2f}s")
