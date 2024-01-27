from fastapi import FastAPI

app = FastAPI()


@app.get("/fibonacci/number")
def read_root():
    return {"status": "to be implemented"}


@app.get("/fibonacci/number/{index}")
def read_item(index: int):
    return {"status": "to be implemented"}


@app.get("/fibonacci/blacklist")
def read_root():
    return {"status": "to be implemented"}


@app.post("/fibonacci/blacklist")
def create_item():
    return {"status": "to be implemented"}