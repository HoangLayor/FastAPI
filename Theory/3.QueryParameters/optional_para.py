from fastapi import FastAPI

app = FastAPI()

# The same way, you can declare optional query parameters,
# by setting their default to None
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    # Dấu | mang ý nghĩa chia TH nếu q : None thì setup = None
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# q ko phải 1 tham số đường dẫn mà là 1 query para
## http://localhost:8000/items/Hoangdeptrai?q=10&short=False
'''
 Type Conversion:
- Nếu nhập đường dẫn tham số truy vấn 'short' :
    + Thì có thể nhập các TH sau : yes, 1, true, True và hàm sẽ đưa về giá trị bool là True
    + Ngược lại thì đưa về giá trị của bool là False
'''

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# Required Query Para -> Yêu cầu nhập biến query bằng cách bỏ TH None và ko đưa vào gtri default
