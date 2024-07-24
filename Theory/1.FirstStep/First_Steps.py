from fastapi import FastAPI

# create a FastAPI "instance"
app = FastAPI()

# create a path operation starting from '/'
@app.get("/hello/")
async def root():
    return {"message": "Hello World"}

''' HTTP methods (Operations)
- post : create data
- get : read data
- put : update data
- delete : delete data
- options, head, patch, trace

@something : decorator
- function can return a dict, list, str, int ... 
'''