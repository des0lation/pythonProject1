import os,io,random,zlib
file_size = 0
file_path = "C:\\Users\\61426\\Desktop\\previous_versions.txt"
#Mac
#file_path = '/Users/abishekshome/previous_versions.txt'
try:
    with open(file_path, "wb") as f:
        bf = io.BufferedWriter(f)
        max_size = 100 * 1024 * 1024
        while file_size < max_size:
            string = 'V'+str(random.randint(1, 100))+'.'+str(random.randint(1, 100))+'.'+str(random.randint(1, 100))
            data = bytes('\n'+string, "utf-8")
            bf.write(data)
            file_size += len(data)
        bf.flush()
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")