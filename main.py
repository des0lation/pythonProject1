from fastapi import FastAPI
import os,io,random

app = FastAPI()

#file_path = "C:\\Users\\61426\\Desktop\\previous_versions.txt"
#Mac
file_path = '/Users/abishekshome/previous_versions.txt'
@app.get('/')
def index():
    return {'heyy':{'name':'Abishek'}}


@app.get('/versions')
def versions():
    return {'data':[{'0':'previous'},{0:'current'}]}

@app.get('/versions/current')
def current():
    with open("C:\\Users\\61426\\Desktop\\latest_version.txt", "r") as file:
        contents = file.read()
        size = os.path.getsize("C:\\Users\\61426\\Desktop\\latest_version.txt")
    return contents


@app.get('/versions/previous')
def current():
    with open(file_path, "r") as file:
        contents = file.read()
        size = os.path.getsize(file_path)
    return contents
