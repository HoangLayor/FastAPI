from fastapi import FastAPI

app = FastAPI()

# Path "parameters" or "variables" used by format string
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id la": item_id}

# Path parameters with types
@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id la": item_id}
'''  
- FastAPI gives you automatic request "parsing" and "validation" of path parameters.
    + Auto convert the string comes from the URL to an int.
    + If the parameter is not an int, the request will return a 422 status code.
- Order matters:
    + Path operations are evaluated in order
    + So if i input a path /item/foo, đường dẫn vẫn hoạt động vì function đầu tiên ko yêu cầu type int
'''

# Path parameters containing paths
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}