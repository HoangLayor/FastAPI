from typing import Annotated

from fastapi import Cookie, FastAPI
# Import Cookie

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = "default"):
    # Cookie Parameter
    return {"ads_id": ads_id}

# Cookie is a "sister" class of Path and Query. It also inherits from the same common Param class.