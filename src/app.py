import imp
from multiprocessing.spawn import import_main_path
from fastapi import FastAPI
import jsonify 

app = FastAPI()

@app.get("/")
def create_user():
    response = {"message": "success"}
    return response
