from typing import Optional, Awaitable
from tornado.web import RequestHandler
from weather import *
import json


class HelloWorld(RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        tair = temperature()
        wspd = speed()
        rain = precipitation()
        pres = pressure()
        loca = location()
        self.render(
            "page.html",
            tair=json.dumps(tair),
            wspd=json.dumps(wspd),
            rain=json.dumps(rain),
            pres=json.dumps(pres),
            loca=json.dumps(loca)
        )
