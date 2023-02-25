from fastapi import FastAPI
import os,io,random
#http://127.0.0.1:8000/
app = FastAPI()

#file_path = "C:\\Users\\61426\\Desktop\\previous_versions.txt"
#Mac
file_path = '/Users/abishekshome/previous_versions.txt'
@app.get('/')
def index():
    return


@app.get('/versions')
def current():
    with open(file_path, "r") as file:
        contents = file.read()
    return contents

