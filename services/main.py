import sys

from fastapi import FastAPI, Header
from typing import Union, List

import socket   
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname) 

app = FastAPI()


@app.get("/")
async def read_root(
    x_custom: Union[List[str], None] = Header(default=None)
    ):
    return {"Reverse proxy address": x_custom,"Server address": IPAddr}