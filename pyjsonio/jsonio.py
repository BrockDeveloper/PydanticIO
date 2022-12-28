import json
from pyjsonio.jsoniomodel import JsonIOModel



class JsonIO:



    def __init__(self, json_file: str, model: JsonIOModel, key: str = None) -> None:

        self.model = None
        self.file = None
        self.items = []
        self.key = None

        if not issubclass(model, JsonIOModel):
            raise Exception("model must be a JsonIOModel") from None

        try:
            with open(json_file, "r") as f:
                f.close()
        except:
            raise Exception("file not found: " + json_file) from None

        self.model = model
        self.file = json_file

        with open(json_file, "r") as f:

            # check if file is empty
            if f.read(1) == "":
                _dict = []
            else:
                f.seek(0)
                _dict = json.load(f)
            f.close()
            
        try:
            self.items = [self.model(**element) for element in _dict]
        except:
            raise Exception("file does not match model") from None
        
        del _dict

        # key must be a key in the model
        if key is not None:
            if key not in self.model.__fields__:
                raise Exception("key must be a field in the model") from None
        
        self.key = key


    
    def write(self, json_file: str = None) -> None:

        if json_file is None:
            json_file = self.file

        try:
            with open(json_file, "w") as f:
                # datas are validated, so no need to check if they are valid
                json.dump([element.dict() for element in self.items], f, indent=4)
                f.close()
        except:
            raise Exception("error writing to file: " + json_file) from None



    def sort(self) -> None:
        if self.key is None:
            raise Exception("key not set")
        self.items.sort(key=lambda x: x[self.key])


    def dict(self) -> list:
        return [element.dict() for element in self.items]



    def append(self, item: JsonIOModel) -> None:

        if not issubclass(item, self.model):
            raise Exception("item does not match model") from None

        try:
            self.items.append(item)
        except:
            raise Exception("item does not match model") from None


    def remove(self, item: JsonIOModel) -> None:

        if item in self.items:
            self.items.remove(item)
    
    def remove(self, key) -> None:
        if self.key is None:
            raise Exception("key not set")
        for i in range(len(self.items)):
            if self.items[i][self.key] == key:
                del self.items[i]
                break



    def __getitem__(self, key):

        if self.key is None:
            raise Exception("key not set")
        else:
            for i in range(len(self.items)):
                if self.items[i][self.key] == key:
                    return self.items[i]
            raise Exception("item not found") from None



    def __iter__(self):    # remove an item by index
        return iter(self.items)


    
    def __len__(self):
        return len(self.items)



    def __str__(self):
        return str(self.items)