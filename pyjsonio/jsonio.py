import json
from pydantic import BaseModel



class JsonIO:



    def __init__(self, json_file: str, model: BaseModel, key: str = None) -> None:

        self.model = model
        self.file = json_file

        with open(json_file, "r") as f:
            _dict = json.load(f)
            f.close()

        self.items = [self.model(**element) for element in _dict]
        del _dict

        self.key = key

        # key must be a key in the model
        if key is not None:
            if key not in self.model.__fields__:
                raise Exception("key must be a key in the model")



    def read(self, json_file: str) -> None:

        with open(json_file, "r") as f:
            _dict = json.load(f)
            f.close()

        self.items = [self.model(**element) for element in _dict]
        del _dict


    
    def write(self, json_file: str = None) -> None:

        if json_file is None:
            json_file = self.file

        with open(json_file, "w") as f:
            json.dump([element.dict() for element in self.items], f, indent=4)
            f.close()



    def sort(self) -> None:
        if self.key is None:
            raise Exception("key not set")
        self.items.sort(key=lambda x: x[self.key])


    def dict(self) -> list:
        return [element.dict() for element in self.items]



    def append(self, item: BaseModel) -> None:
        self.items.append(item)

        # sort by key


    def remove(self, item: BaseModel) -> None:
        self.items.remove(item)
        # sort by key


    
    def remove(self, key) -> None:
        if self.key is None:
            raise Exception("key not set")
        for i in range(len(self.items)):
            if self.items[i][self.key] == key:
                del self.items[i]
                break



    def __getitem__(self, key):
        return self.items[key]



    def __iter__(self):    # remove an item by index
        return iter(self.items)


    
    def __len__(self):
        return len(self.items)



    def __str__(self):
        return str(self.items)
    


    def __del__(self):
        del self.items
        del self.model
        del self.file
        del self