

from com.epislab.utils.creational.abstract.abstract_service import AbstractService


class Login(AbstractService):
    async def handle(self, **kwargs):
        try:
            return "success"
        except Exception as e:
            return "fail"

class Logout(AbstractService):
    async def handle(self, **kwargs):
        try:
            return "success"
        except Exception as e:
            return "fail"
        