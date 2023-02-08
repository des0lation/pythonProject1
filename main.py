from fastapi import FastAPI
import os,io

app = FastAPI()


@app.get('/')
def index():
    return {'heyy':{'name':'Abishek'}}


@app.get('/versions')
def versions():
    return {'data':[{'0':'previous'},{0:'current'}]}


file_size = 0
file_path = "C:\\Users\\61426\\Desktop\\previous_versions3.txt"
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


@app.get('/versions/current')
def current():
    with open("C:\\Users\\61426\\Desktop\\latest_version.txt", "r") as file:
        contents = file.read()
        size = os.path.getsize("C:\\Users\\61426\\Desktop\\latest_version.txt")
    return contents,size/(1024 * 1024)

@app.get('/versions/previous')
def current():
    with open(file_path, "r") as file:
        contents = file.read()
        size = os.path.getsize("C:\\Users\\61426\\Desktop\\latest_version.txt")
    return contents,size/ (1024 * 1024)
