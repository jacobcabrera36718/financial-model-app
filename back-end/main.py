from fastapi import FastAPI


from src.models import data_models as pydantic_data_models


app = FastAPI()


@app.get("/")
def root():
    return { "message": "/docs to show full endpoints"}