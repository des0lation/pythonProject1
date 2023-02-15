import re
import requests
import requests, json,time,zlib
import time, numpy as np
data = requests.get("http://127.0.0.1:8000/versions").text
t_now = time.time()

pattern = r'V(\d+)\.(\d+)\.(\d+)'
versions = re.findall(pattern, data)

highest_major = 0
highest_minor = 0
highest_patch = 0
for major, minor, patch in versions:
    if int(major) > highest_major:
        highest_major = int(major)
        highest_minor = int(minor)
        highest_patch = int(patch)
    elif int(major) == highest_major and int(minor) > highest_minor:
        highest_minor = int(minor)
        highest_patch = int(patch)
    elif int(major) == highest_major and int(minor) == highest_minor and int(patch) > highest_patch:
        highest_patch = int(patch)

end_version = (highest_major, highest_minor, highest_patch)
print(end_version)

t_done = time.time()
print("Time taken is", t_done - t_now)
