from typing import Annotated
from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: str
    # url: HttpUrl
    name: str

# List fields
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = [] # subtype : list
    # tags: list[str] = [] # list of string
    # tags: set[str] = [] # list of unique strings
    # tags: dict[str, str] = [] # list of key-value pairs
    image: Image | None = None # Nested Model
    images: list[Image] | None = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

''' JSON Body
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags": [
            "rock",
            "metal",
            "bar"
        ],
        "images": [
            {
                "url": "http://example.com/baz.jpg",
                "name": "The Foo live"
            },
            {
                "url": "http://example.com/dave.jpg",
                "name": "The Baz"
            }
        ]
    }
}
'''

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights

'''
{
  "additionalProp1": 0,
  "additionalProp2": 0,
  "additionalProp3": 0
}
'''