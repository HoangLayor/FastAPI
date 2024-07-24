from enum import Enum
from fastapi import FastAPI

class PlayerName(str, Enum):
    viktor = "Axelsen"
    chen = "Long"
    momota = "Kento"
    lee = "Chong Wei"

app = FastAPI()
@app.get("/items/{item_type}")
async def get_item(item_type: PlayerName):
    return {"item_type": item_type}

@app.get("/players/{player_name}")
async def guess_player(player_name: PlayerName):
    if player_name is PlayerName.viktor:
        return {"player_name": player_name, "message": "This is Viktor Axelsen"}
    if player_name.value == "Long":
        return {"player_name": player_name.value, "message": "This is Chen Long"}
    if player_name == PlayerName.momota:
        return {"player_name": player_name, "message": "This is Kento Momota"}
    if player_name == PlayerName.lee:
        return {"player_name": player_name, "message": "This is Lee Chong Wei"}
    return {"player_name": player_name, "message": "Who is this player?"}

'''
> Nếu bạn gọi /players/Long, FastAPI sẽ:
    - Xác thực rằng "Long" là một giá trị hợp lệ của Enum PlayerName.
    - Chuyển đổi chuỗi "Long" thành giá trị Enum tương ứng.
    - Truyền giá trị Enum đó vào hàm get_model.
> Nếu bạn cố gắng sử dụng một giá trị không có trong Enum 
(ví dụ: /players/unknown), FastAPI sẽ tự động trả về lỗi 422 Unprocessable Entity.
'''