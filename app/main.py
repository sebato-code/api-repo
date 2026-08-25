from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
async def list_users():
    return {"message": "Users API", "count": 1}