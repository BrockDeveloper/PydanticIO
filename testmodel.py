from pydantic import BaseModel

class TestModel(BaseModel):
    id: int
    name: str

    # support item assignment
    def setattribute(self, key, value):
        self.__setattr__(key, value)