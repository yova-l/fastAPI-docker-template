from typing import Union
from configparser import ConfigParser
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

def _config(filename=None, section='postgresql'):
    # Use the correct file path
    if filename is None:
        filename = os.path.join(os.path.dirname(__file__), '..', 'database.ini')
        
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

@app.get("/")
def read_root():
    return {"secret": f"{os.getenv('SECRET')}"}

@app.get("/dbInfo")
def read_db():
    return _config()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}