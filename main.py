from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. 定义一个数据模型
class VehicleReport(BaseModel):
    vehicle_id: str
    speed: float
    battery: float

# 2. 保留之前的 GET 接口
@app.get("/vehicle/status")
def get_vehicle_status():
    return {"vehicle_id": "AV-01", "status": "online", "speed": 0.0}

# 3. 新增一个 POST 接口，接收上报数据
@app.post("/vehicle/report")
def receive_report(report: VehicleReport):
    # 这里我们暂时不存数据库，只返回校验后的数据
    return {
        "received": True,
        "vehicle_id": report.vehicle_id,
        "speed_kmh": report.speed,
        "battery_level": report.battery
    }

# 定义接收数据的格式
class VehicleData(BaseModel):
    vehicle_id: str
    speed: float
    battery: float

# 编写 POST 接口
@app.post("/vehicle/report")
def report_vehicle_status(data: VehicleData):
    # 这里只是把接收到的数据原样返回，用来测试
    return data