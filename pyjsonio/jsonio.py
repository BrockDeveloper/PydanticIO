import json
from pydantic import BaseModel



class JsonIO:



    def __init__(self, json_file: str, model: BaseModel) -> None:

        '''
        Initialize the JsonIO class
        
        :param json_file: The json file to read from
        :param model: The pydantic model to use for validation
        
        :return: None
        '''

        self.model = model
        self.file = json_file

        with open(json_file, "r") as f:
            _dict = json.load(f)
            f.close()

        self.items = [self.model(**element) for element in _dict]
        del _dict
    


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


    def dict(self) -> list:
        return [element.dict() for element in self.items]

    def append(self, item: BaseModel) -> None:
        self.items.append(item)

    def remove(self, item: BaseModel) -> None:
        self.items.remove(item)
    
    def remove(self, index: int) -> None:
        del self.items[index]


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