import os,io

file_size = 0
file_path = "C:\\Users\\61426\\Desktop\\previous_versions.txt"
try:
    with open(file_path, "wb") as f:
        bf = io.BufferedWriter(f)
        max_size = 100 * 1024 * 1024
        while bf.tell() < max_size:
            data = bytes("a" * 1024 * 1024, "utf-8")
            bf.write(bytes("a" * 1024 * 1024, "utf-8"))
            file_size += len(data)
        bf.flush()
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")


