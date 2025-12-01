from fastapi import FastAPI
from sandwichAPI import sandwich

app = FastAPI()


@app.get("/")
def route_root():

    response = sandwich()
    
    return {"message": response}