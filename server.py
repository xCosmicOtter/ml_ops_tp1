from fastapi import FastAPI
import joblib
# Create a FastAPI application
app = FastAPI()
 
model = joblib.load("regression.joblib")

# Define a route at the root web address ("/")
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/predict/")
async def read_item(size: float,nb_bedrooms: float,garden: bool):
    return {"response" : model.predict([[size, nb_bedrooms, garden]])[0]}
