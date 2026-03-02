from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return{"mesage":"Backend working"}

