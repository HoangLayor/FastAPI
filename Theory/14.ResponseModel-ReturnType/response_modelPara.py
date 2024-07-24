from typing import Any
# Import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: str

class UserIn(UserBase):
    password: str

class UserOut(UserBase):
    id: int

@app.post("/users/", response_model=UserOut)
async def create_user(user: UserIn):
    # Giả sử tạo user và trả về
    return {"username": user.username, "email": user.email, "id": 1}

'''
- Xác thực dữ liệu:
    + FastAPI sẽ tự động xác thực dữ liệu trả về dựa trên model đã định nghĩa.
- Lọc dữ liệu:
    + Nếu hàm trả về dữ liệu dư thừa, FastAPI sẽ tự động lọc bỏ các trường không có trong model.
- Chuyển đổi kiểu dữ liệu:
    + FastAPI sẽ tự động chuyển đổi dữ liệu sang định dạng phù hợp với model.
- Bảo mật:
    + Giúp ngăn chặn việc vô tình tiết lộ dữ liệu nhạy cảm.
'''