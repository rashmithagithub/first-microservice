import random
from config import app

@app.get('/message')
def greetnow():
    return "This is home page...Hi How arey you?"

@app.get('/number')
def fun():
    num = random.randint(0,100)
    return f"{num} is returned"