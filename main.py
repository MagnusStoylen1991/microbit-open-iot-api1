from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# lagring i minne – greit for demo / mange brukere
sensor_data = []

class MicrobitPayload(BaseModel):
    user: str
    value: float
    timestamp: float

@app.post("/submit")
def submit_data(payload: MicrobitPayload):
    sensor_data.append(payload.dict())
    return {"status": "ok", "entries": len(sensor_data)}

@app.get("/data")
def get_data():
    return sensor_data