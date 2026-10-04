from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]


def hottest(devices):
    best = devices[0]
    for d in devices:
        if d["temp"] > best["temp"]:
            best = d
    return best


def average_temp(devices):
    total = 0
    for d in devices:
        total += d["temp"]
    return total / len(devices)


@app.get("/devices")
def get_devices():
    return readings

@app.get("/devices/hottest")
def get_hottest():
    return hottest(readings)

@app.get("/devices/online")
def get_online():
    return [d for d in readings if d["online"]]