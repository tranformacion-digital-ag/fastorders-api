from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """
   This method says hello to the person name from the fastapi course
   :param name: The person's name
   :type name: str
   :return: The greetings message
   :rtype: dict[str, s
    """
    return {"message": f"Hello {name}"}