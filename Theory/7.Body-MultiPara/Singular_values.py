from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

'''
Dấu * phân biệt positional arguments và keyword arguments
    - Tất cả tham số trước * là tham số theo vị trí hoặc từ khóa
    - Tất cả tham số sau * là tham số phải theo từ khóa
 + Tham số theo từ khóa là tham số không quan tâm tới vị trí khai báo mà chỉ quan tâm tới tên biến
'''

@app.put("/put_items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

# Embed a single body parameter : 
# item: Item = Body(embed=True) or item: Annotated[Item, Body(embed=True)]
