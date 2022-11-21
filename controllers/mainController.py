#optional
from fastapi import Request

class mainController():
    def index(request: Request):
        return {
            'msg': 'hellow worldsz'
        }

controller = mainController()
#optional