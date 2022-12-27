from pyjsonio.jsonio import JsonIO
from pyjsonio.jsoniomodel import JsonIOModel

class TestModel(JsonIOModel):
    id: int
    name: str


test = JsonIO("testfile.json", TestModel, key = "id")
test.sort()
print(test)